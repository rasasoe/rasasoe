import tempfile
import unittest
from pathlib import Path
from PIL import Image
from check_portfolio import check


class Regressions(unittest.TestCase):
    def test_missing_media_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('![demo](missing.png)', encoding='utf-8')
            self.assertTrue(check(root)[0])

    def test_unescaped_svg_entity_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('![banner](banner.svg)', encoding='utf-8')
            (root / 'banner.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><text>Camera & Mic</text></svg>', encoding='utf-8')
            self.assertTrue(check(root)[0])

    def test_truncated_png_fails_but_complete_image_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'README.md').write_text('![demo](demo.png)', encoding='utf-8')
            path = root / 'demo.png'
            Image.new('RGB', (32, 32), 'blue').save(path)
            self.assertEqual(check(root)[0], [])
            path.write_bytes(path.read_bytes()[:40])
            self.assertTrue(check(root)[0])


if __name__ == '__main__':
    unittest.main()
