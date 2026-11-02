"""Read-only repository review. Never import or execute inspected project code."""
import ast, collections, dis, hashlib, io, json, marshal, os, pathlib
import pickletools, re, struct, subprocess, sys, types, urllib.request, zipfile, zlib

BASE = "b6cfe9358e55deb5f0606d1c9a4ce7360dbbd39d"
SDK_URL = "https://www.renpy.org/dl/8.5.3/renpy-8.5.3-sdk.zip"
SDK_SHA256 = "ff57648f9c04f27e381c48af6d8e3ee3cdec296bed4d3831f47f09b0a71b505e"
MAX = 64 * 1024 * 1024

class Inert:
    def __init__(self, kind, args=None):
        self.kind, self.args, self.state = kind, args, None

def inspect_pickle(data):
    """Interpret structure only. GLOBAL/REDUCE/BUILD never import/call anything."""
    stack, memo, mark, globals_used = [], {}, object(), set()
    def marked():
        pos = len(stack) - 1
        while pos >= 0 and stack[pos] is not mark:
            pos -= 1
        if pos < 0:
            raise ValueError("missing MARK")
        values = stack[pos+1:]
        del stack[pos:]
        return values
    def mapping(obj):
        if isinstance(obj, dict):
            return obj
        if isinstance(obj, Inert):
            if not isinstance(obj.state, dict):
                obj.state = {}
            return obj.state
        raise ValueError("invalid mapping")
    for op, arg, pos in pickletools.genops(data):
        name = op.name
        if name in ("PROTO", "FRAME"):
            continue
        if name == "MARK": stack.append(mark)
        elif name == "NONE": stack.append(None)
        elif name in ("NEWTRUE", "NEWFALSE"): stack.append(name == "NEWTRUE")
        elif name in ("BININT", "BININT1", "BININT2", "INT", "LONG", "LONG1", "LONG4",
                      "FLOAT", "BINFLOAT", "UNICODE", "BINUNICODE", "SHORT_BINUNICODE",
                      "BINUNICODE8", "STRING", "BINSTRING", "SHORT_BINSTRING",
                      "BINBYTES", "SHORT_BINBYTES", "BINBYTES8", "BYTEARRAY8"):
            stack.append(arg)
        elif name == "EMPTY_LIST": stack.append([])
        elif name == "EMPTY_DICT": stack.append({})
        elif name == "EMPTY_TUPLE": stack.append(())
        elif name == "EMPTY_SET": stack.append(set())
        elif name in ("TUPLE1", "TUPLE2", "TUPLE3"):
            n = int(name[-1]); vals = stack[-n:]; del stack[-n:]; stack.append(tuple(vals))
        elif name == "TUPLE": stack.append(tuple(marked()))
        elif name == "LIST": stack.append(list(marked()))
        elif name == "DICT":
            vals = marked(); stack.append(dict(zip(vals[::2], vals[1::2])))
        elif name == "FROZENSET": stack.append(frozenset(marked()))
        elif name == "APPEND":
            value = stack.pop(); stack[-1].append(value)
        elif name == "APPENDS":
            values = marked(); stack[-1].extend(values)
        elif name == "ADDITEMS":
            values = marked(); stack[-1].update(values)
        elif name == "SETITEM":
            value, key = stack.pop(), stack.pop(); mapping(stack[-1])[key] = value
        elif name == "SETITEMS":
            vals = marked(); mapping(stack[-1]).update(zip(vals[::2], vals[1::2]))
        elif name in ("BINPUT", "LONG_BINPUT", "PUT"): memo[int(arg)] = stack[-1]
        elif name == "MEMOIZE": memo[len(memo)] = stack[-1]
        elif name in ("BINGET", "LONG_BINGET", "GET"): stack.append(memo[int(arg)])
        elif name == "GLOBAL":
            mod, cls = arg.split(" ", 1); ref = mod + "." + cls
            globals_used.add(ref); stack.append(Inert("global", ref))
        elif name == "STACK_GLOBAL":
            cls, mod = stack.pop(), stack.pop(); ref = str(mod) + "." + str(cls)
            globals_used.add(ref); stack.append(Inert("global", ref))
        elif name in ("REDUCE", "NEWOBJ"):
            args, cls = stack.pop(), stack.pop()
            stack.append(Inert(name, (cls, args)))
        elif name == "NEWOBJ_EX":
            kwargs, args, cls = stack.pop(), stack.pop(), stack.pop()
            stack.append(Inert(name, (cls, args, kwargs)))
        elif name == "BUILD":
            state = stack.pop()
            if not isinstance(stack[-1], Inert): raise ValueError("BUILD on non-object")
            stack[-1].state = state
        elif name == "POP": stack.pop()
        elif name == "POP_MARK": marked()
        elif name == "DUP": stack.append(stack[-1])
        elif name == "STOP":
            return stack[-1], sorted(globals_used)
        else:
            raise ValueError("unsupported pickle opcode: " + name)
        if len(stack) > 200000:
            raise ValueError("pickle stack limit")
    raise ValueError("missing STOP")

def walk(obj):
    seen, pending = set(), [obj]
    while pending:
        value = pending.pop()
        if id(value) in seen: continue
        seen.add(id(value))
        yield value
        if isinstance(value, Inert): pending.extend([value.args, value.state])
        elif isinstance(value, dict):
            pending.extend(value.keys()); pending.extend(value.values())
        elif isinstance(value, (tuple, list, set, frozenset)): pending.extend(value)

def inflate(data):
    decoder = zlib.decompressobj()
    out = decoder.decompress(data, MAX + 1)
    if len(out) > MAX or not decoder.eof or decoder.unused_data:
        raise ValueError("invalid/oversized compressed stream")
    return out

def rpyc_streams(data):
    if data.startswith(b"RENPY RPC2"):
        streams, offset = [], 10
        for _ in range(32):
            slot, start, length = struct.unpack_from("<III", data, offset)
            offset += 12
            if not slot: return streams
            if start + length > len(data): raise ValueError("rpyc bounds")
            streams.append((slot, inflate(data[start:start+length])))
        raise ValueError("rpyc slot limit")
    return [(1, inflate(data))]

def pyc_info(data):
    if len(data) < 16 or data[:4] != b"\xcb\r\r\n":
        raise ValueError("not Python 3.12 bytecode")
    # marshal constructs code objects, but no exec/eval/import of the code follows.
    reader = io.BytesIO(data[16:])
    code = marshal.load(reader)
    if reader.tell() != len(data) - 16 or not isinstance(code, types.CodeType):
        raise ValueError("invalid/trailing marshal payload")
    pending, names, strings, instructions, objects = [code], set(), [], 0, 0
    while pending:
        c = pending.pop(); objects += 1
        names.update(c.co_names)
        instructions += sum(1 for _ in dis.get_instructions(c))
        for item in c.co_consts:
            if isinstance(item, types.CodeType): pending.append(item)
            elif isinstance(item, str): strings.append(item)
        if objects > 100000: raise ValueError("too many code objects")
    return {"names": sorted(names), "code_objects": objects, "instructions": instructions}, strings

RULES = {
    "browser_credentials": re.compile(r"Login Data|Local State|CryptUnprotectData|win32crypt|\\(?:Chrome|Edge)\\User Data", re.I),
    "exfil_endpoint": re.compile(r"discord(?:app)?\.com/api/webhooks|api\.telegram\.org/bot|ngrok|pastebin\.com/raw", re.I),
    "command_execution": re.compile(r"subprocess|os\.system|os\.popen|powershell|cmd\.exe|ctypes|winreg|shell\s*=\s*True", re.I),
    "network": re.compile(r"\brequests\b|urllib|socket|https?://|WebSocket|XMLHttpRequest|sendBeacon", re.I),
}
SECRETS = {
    "private_key": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "github_token": re.compile(rb"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})"),
    "google_api_key": re.compile(rb"AIza[A-Za-z0-9_-]{35}"),
    "google_access_token": re.compile(rb"ya29\.[A-Za-z0-9_-]{20,}"),
    "google_refresh_token": re.compile(rb"1//[A-Za-z0-9_-]{30,}"),
    "openai_key": re.compile(rb"sk-(?:proj-)?[A-Za-z0-9_-]{24,}"),
    "aws_access_key": re.compile(rb"AKIA[A-Z0-9]{16}"),
}
def indicators(strings):
    text = "\n".join(strings)
    return sorted(name for name, pattern in RULES.items() if pattern.search(text))

def git(*args):
    return subprocess.check_output(["git", *args], timeout=120)

def current_tree(commit):
    rows = []
    for line in git("ls-tree", "-rz", "--full-tree", commit).split(b"\0"):
        if not line: continue
        meta, rawpath = line.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        rows.append({"path": rawpath.decode("utf-8"), "mode": mode, "type": kind, "oid": oid})
    return rows

def selftest():
    import pickle
    benign = {"list": [1, True, None, "text"], "tuple": (2, 3)}
    parsed, names = inspect_pickle(pickle.dumps(benign, protocol=5))
    assert parsed == benign and not names
    malicious = b"cos\nsystem\n(Vraise-security-sentinel\np0\ntR."
    parsed, names = inspect_pickle(malicious)
    assert names == ["os.system"] and isinstance(parsed, Inert)
    assert inflate(zlib.compress(b"hello")) == b"hello"
    try: inflate(zlib.compress(b"x") + b"trailing")
    except ValueError: pass
    else: raise AssertionError("trailing data accepted")
    c = compile("raise RuntimeError('must never execute')", "<audit-test>", "exec")
    info, _ = pyc_info(b"\xcb\r\r\n" + b"\0"*12 + marshal.dumps(c))
    assert "RuntimeError" in info["names"]
    print("SELFTEST_OK")

def main():
    if "--selftest" in sys.argv: selftest(); return
    out = pathlib.Path(os.environ["AUDIT_OUTPUT"]).resolve()
    blobs_dir = out / "scan-blobs"
    blobs_dir.mkdir(parents=True, exist_ok=True)
    target = current_tree(BASE)
    commits = git("rev-list", "--all").decode().splitlines()
    trees = {c: current_tree(c) for c in commits}
    paths = collections.defaultdict(set)
    for rows in trees.values():
        for row in rows:
            if row["type"] == "blob": paths[row["oid"]].add(row["path"])
    # Complete all reachable history blobs, without checking out historical code.
    proc = subprocess.Popen(["git", "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    blobs = {}
    for oid in paths:
        proc.stdin.write((oid+"\n").encode()); proc.stdin.flush()
        header = proc.stdout.readline().decode().strip().split()
        if len(header) != 3 or header[1] != "blob": raise ValueError("missing blob: "+oid)
        size = int(header[2])
        data = proc.stdout.read(size)
        if proc.stdout.read(1) != b"\n" or len(data) != size: raise ValueError("short read")
        actual = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
        if actual != oid: raise ValueError("Git object hash mismatch")
        blobs[oid] = data
        (blobs_dir / (oid + pathlib.PurePosixPath(sorted(paths[oid])[0]).suffix)).write_bytes(data)
    proc.stdin.close(); proc.wait(timeout=30)
    print("ALL_BLOBS_READ", len(blobs), sum(map(len, blobs.values())), flush=True)
    sdk_bytes = urllib.request.urlopen(SDK_URL, timeout=120).read()
    if hashlib.sha256(sdk_bytes).hexdigest() != SDK_SHA256: raise ValueError("SDK checksum mismatch")
    sdk = zipfile.ZipFile(io.BytesIO(sdk_bytes))
    sdk_by_sha, sdk_by_name = collections.defaultdict(list), {}
    for member in sdk.infolist():
        if member.is_dir(): continue
        content = sdk.read(member)
        sha = hashlib.sha256(content).hexdigest()
        sdk_by_sha[sha].append(member.filename)
        sdk_by_name[member.filename] = sha
    inventory, secret_hits, compiled, parse_errors, format_checks = [], [], [], [], []
    target_oids = {r["oid"] for r in target if r["type"] == "blob"}
    for row in target:
        if row["type"] != "blob": continue
        data = blobs[row["oid"]]
        sha = hashlib.sha256(data).hexdigest()
        matches = sdk_by_sha.get(sha, [])
        inventory.append({**row, "bytes":len(data), "sha256":sha, "official_sdk_matches":matches})
    for oid, data in blobs.items():
        for name, pattern in SECRETS.items():
            for match in pattern.finditer(data):
                # Never print/store the matching secret value.
                secret_hits.append({"oid":oid,"paths":sorted(paths[oid]),"rule":name,"offset":match.start()})
        suffixes = {pathlib.PurePosixPath(p).suffix.lower() for p in paths[oid]}
        try:
            if suffixes & {".rpyc", ".rpymc"}:
                slots = []
                for slot, stream in rpyc_streams(data):
                    parsed, global_names = inspect_pickle(stream)
                    strings = [x for x in walk(parsed) if isinstance(x,str)]
                    sources = []
                    for x in walk(parsed):
                        if isinstance(x, Inert) and x.kind in ("NEWOBJ","REDUCE"):
                            cls = x.args[0]
                            if isinstance(cls,Inert) and cls.args == "renpy.ast.PyCode":
                                sources.append([s for s in walk(x.state) if isinstance(s, str)])
                    slots.append({"slot":slot,"decoded_bytes":len(stream),"globals":global_names,
                                  "indicators":indicators(strings),"pycode_strings":sources})
                compiled.append({"oid":oid,"paths":sorted(paths[oid]),"type":"rpyc","slots":slots})
            elif ".pyc" in suffixes:
                info, strings = pyc_info(data)
                compiled.append({"oid":oid,"paths":sorted(paths[oid]),"type":"pyc",
                                 **info,"indicators":indicators(strings+info["names"])})
        except Exception as exc:
            parse_errors.append({"oid":oid,"paths":sorted(paths[oid]),"error":type(exc).__name__+": "+str(exc)[:200]})
        # Validate data structures without importing/using project code.
        try:
            if ".png" in suffixes:
                if not data.startswith(b"\x89PNG\r\n\x1a\n"): raise ValueError("PNG signature")
                off, ended, chunks = 8, False, []
                while off+12 <= len(data):
                    length = struct.unpack_from(">I",data,off)[0]
                    kind = data[off+4:off+8]; payload=data[off+8:off+8+length]
                    end = off+12+length
                    if end>len(data): raise ValueError("PNG bounds")
                    crc=struct.unpack_from(">I",data,off+8+length)[0]
                    if zlib.crc32(kind+payload)&0xffffffff != crc: raise ValueError("PNG CRC")
                    chunks.append(kind.decode("ascii")); off=end
                    if kind==b"IEND": ended=True; break
                if not ended or off!=len(data): raise ValueError("PNG missing IEND/trailing data")
                format_checks.append({"oid":oid,"format":"png","chunks":chunks,"status":"parsed"})
            if suffixes & {".ttf",".otf"}:
                if data[:4] not in (b"\0\1\0\0", b"OTTO", b"true"): raise ValueError("font signature")
                count=struct.unpack_from(">H",data,4)[0]
                if len(data)<12+16*count: raise ValueError("font directory")
                for i in range(count):
                    tag,checksum,offset,length=struct.unpack_from(">4sIII",data,12+16*i)
                    if offset+length>len(data): raise ValueError("font bounds")
                format_checks.append({"oid":oid,"format":"font","tables":count,"status":"parsed"})
            if suffixes & {".json"}: json.loads(data)
            if suffixes & {".svg"}:
                import xml.etree.ElementTree as ET
                root=ET.fromstring(data)
                if any(el.tag.split("}")[-1].lower()=="script" for el in root.iter()):
                    format_checks.append({"oid":oid,"format":"svg","status":"contains_script"})
                if re.search(rb'(?:href\s*=\s*["\x27](?:https?:|javascript:)|onload\s*=)',data,re.I):
                    format_checks.append({"oid":oid,"format":"svg","status":"external_or_event_reference"})
        except Exception as exc:
            parse_errors.append({"oid":oid,"paths":sorted(paths[oid]),"error":type(exc).__name__+": "+str(exc)[:200]})
    official_oids={r["oid"] for r in inventory if r["official_sdk_matches"]}
    for item in compiled: item["official_sdk_match"]=item["oid"] in official_oids
    suspicious_globals=[]
    for item in compiled:
        if item["type"] != "rpyc" or item["official_sdk_match"]: continue
        for slot in item["slots"]:
            for name in slot["globals"]:
                if not name.startswith(("renpy.","collections.","builtins.","__builtin__.")):
                    suspicious_globals.append({"oid":item["oid"],"paths":item["paths"],"global":name})
    report={
        "target":BASE,"head":git("rev-parse","HEAD").decode().strip(),"commits":commits,
        "current_files":len(inventory),"reachable_unique_blobs":len(blobs),
        "historical_bytes":sum(map(len,blobs.values())),"current_bytes":sum(r["bytes"] for r in inventory),
        "sdk_url":SDK_URL,"sdk_sha256":SDK_SHA256,"sdk_match_files":sum(bool(r["official_sdk_matches"]) for r in inventory),
        "unmatched_runtime":[r for r in inventory if r["path"].startswith("Windows/") and not r["official_sdk_matches"]],
        "secret_pattern_hits":secret_hits,"parse_errors":parse_errors,"suspicious_pickle_globals":suspicious_globals,
        "compiled_unique_objects":len(compiled),"nonregular_entries":[r for rows in trees.values() for r in rows if r["mode"] not in ("100644","100755")],
        "limitations":["Static inspection is not proof of absence of malware.",
                       "No project/native code was executed.","Secret rules do not cover every credential.",
                       "Cloud account/host incident forensics and deleted/unreachable Git objects are outside scope.",
                       "Compiled/source semantic correspondence is not established by string scanning."]
    }
    (out/"inventory.json").write_text(json.dumps(inventory,ensure_ascii=True,indent=2))
    (out/"compiled.json").write_text(json.dumps(compiled,ensure_ascii=True,indent=2))
    (out/"formats.json").write_text(json.dumps(format_checks,ensure_ascii=True,indent=2))
    (out/"review.json").write_text(json.dumps(report,ensure_ascii=True,indent=2))
    compact={k:v for k,v in report.items() if k not in ("unmatched_runtime","secret_pattern_hits","parse_errors","suspicious_pickle_globals")}
    compact.update({"unmatched_runtime_files":len(report["unmatched_runtime"]),"secret_hits":len(secret_hits),
                    "parse_errors":len(parse_errors),"suspicious_pickle_globals":len(suspicious_globals)})
    print("AUDIT_SUMMARY_JSON="+json.dumps(compact),flush=True)
    print("UNMATCHED_RUNTIME_JSON="+json.dumps([r["path"] for r in report["unmatched_runtime"]]),flush=True)
    print("PARSE_ERRORS_JSON="+json.dumps(parse_errors),flush=True)
    print("SECRET_LOCATIONS_JSON="+json.dumps(secret_hits),flush=True)
    print("PICKLE_GLOBALS_JSON="+json.dumps(suspicious_globals),flush=True)

if __name__=="__main__":
    main()
