import importlib.util
import tempfile
import unittest
from pathlib import Path
from PIL import Image
spec=importlib.util.spec_from_file_location('audit',Path(__file__).resolve().parents[1]/'check_image_assets.py')
audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)
class AuditTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
  self.root=Path(self.tmp.name);audit.ROOT=self.root
  self.p=self.root/'valid.png';Image.new('RGBA',(2,1),(10,20,30,0)).save(self.p)
 def test_transparency_pixels(self):
  r=audit.inspect(self.p);self.assertEqual((r['width'],r['transparent_pixels'],r['status']),(2,2,'PASS_TECHNICAL'))
 def test_corrupt_image_rejected(self):
  self.p.write_bytes(self.p.read_bytes()[:30]);self.assertEqual(audit.inspect(self.p)['status'],'FAIL')
 def test_hash_mismatch_rejected(self):self.assertEqual(audit.inspect(self.p,'0'*64)['status'],'FAIL')
 def test_escape_symlink_rejected(self):
  p=self.root/'escape.png';p.symlink_to('/etc/hosts');self.assertEqual(audit.inspect(p)['status'],'FAIL')
 def test_non_png_rejected(self):
  self.p.write_text('not a png');self.assertEqual(audit.inspect(self.p)['status'],'FAIL')
if __name__ == '__main__':
 unittest.main(verbosity=2)
