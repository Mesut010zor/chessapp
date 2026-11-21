import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LauncherTest(unittest.TestCase):
    def test_opens_official_site_with_separate_persistent_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            browser = Path(tmp, 'chromium')
            browser.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n')
            browser.chmod(0o755)
            result = subprocess.run(['/bin/sh', ROOT / 'chess-desktop'], env={**os.environ, 'PATH': tmp + ':/usr/bin', 'XDG_CONFIG_HOME': tmp}, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('--app=https://www.chess.com/tr', result.stdout.splitlines())
            self.assertIn('--user-data-dir=' + tmp + '/chess-com-desktop', result.stdout.splitlines())
