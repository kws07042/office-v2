"""Exercise inventory behavior on a checkout with no production images."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "inventory_audit", Path(__file__).resolve().parents[1] / "check_image_assets.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.addCleanup(setattr, audit, "ROOT", audit.ROOT)
        audit.ROOT = self.root
        (self.root / "CharacterArt").mkdir()
        (self.root / "CharacterArt/CURRENT_ASSETS.json").write_text('{"sha256": {}}')
        game = self.root / "Source/game"
        game.mkdir(parents=True)
        (game / "event_cg_plan.json").write_text('{"sets": []}')
        (game / "office_phone.rpy").write_text(
            'init python:\n    PHONE_MEDIA = {"photo": {"path": "images/message.png"}}\n')

    def run_inventory(self):
        output = io.StringIO()
        with patch("sys.argv", ["check_image_assets.py"]), contextlib.redirect_stdout(output):
            result = audit.main()
        self.assertEqual(result, 0)
        return json.loads(output.getvalue())

    def test_empty_checkout_reports_missing_message_without_decode_error(self):
        result = self.run_inventory()
        self.assertEqual((result["count"], result["errors"]), (0, 0))
        self.assertEqual(result["missing_message_assets"], [
            {"id": "photo", "planned_path": "images/message.png"}])

    def test_present_message_is_not_missing(self):
        message = self.root / "Source/game/images/message.png"
        message.parent.mkdir()
        audit.Image.new("RGB", (1, 1)).save(message)
        result = self.run_inventory()
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["missing_message_assets"], [])

    def test_explicit_missing_input_is_still_an_error(self):
        with patch("sys.argv", ["check_image_assets.py", "missing"]):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as exc:
                audit.main()
        self.assertEqual(exc.exception.code, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
