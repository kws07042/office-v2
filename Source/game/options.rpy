init -2 python:
    gui.init(1280, 720)
define config.name = "퇴근 후, 우리 — 대본 시험판"
define config.version = "0.35.2-player-flow"
define config.save_directory = "afterwork-us-script-prototype-v1"
define config.window = "auto"
define config.check_conflicting_properties = True
define config.has_sound = False
define config.has_music = False
define config.has_voice = False
define config.history_length = 300
define build.name = "afterwork_script_prototype"
default preferences.text_cps = 0
define renpy_agent_variables = ("chapter", "location", "speech_informal", "active_route", "affinity", "completed", "memory", "trust_ria", "dating", "prepared", "first_kiss", "kiss_proposed", "ending", "c06_person", "c06_topic", "c07_person", "c07_method", "r02_plan", "r02_expression", "r03_reply")
init python:
    build.classify("**.rpy", None)
    build.classify("**/renpy_agent.rpyc", None)
    build.classify("game/images/characters/ria/ui_master.png", None)
    build.classify("game/images/characters/ria/expressions/face_reference.png", None)
    build.classify("**/testcases.rpyc", None)
    build.classify("**/progression_smoke.rpyc", None)
    build.classify("**/*_tests.rpyc", None)
    build.classify("**/three_choice_cases.json", None)
    build.classify("**/saves/**", None)
    build.classify(".renpy-agent/**", None)
    build.classify("art/**", None)
    build.classify("story/**", None)
    build.classify("tools/**", None)
    build.classify("review-output/**", None)
    build.classify("testing/**", None)
    build.classify("opening-traces/**", None)
    build.classify("tests/**", None)
    build.classify("log.txt", None)
    build.classify("errors.txt", None)
    build.classify("traceback.txt", None)
    build.classify("*-success.json", None)
