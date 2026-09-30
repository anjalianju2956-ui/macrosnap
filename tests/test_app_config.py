import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
APP_PATH = ROOT / 'app.py'


class AppConfigTests(unittest.TestCase):
    def test_model_name_is_supported(self):
        spec = importlib.util.spec_from_file_location('macro_snap_app', APP_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertIn(module.MODEL_NAME, {'gemini-2.0-flash', 'gemini-2.5-flash'})


if __name__ == '__main__':
    unittest.main()
