import unittest

from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello world!"
        self.assertEqual(extract_title(md), "Hello world!")
    
    def test_extract_title_fails(self):
        md = "## Hello world!"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()