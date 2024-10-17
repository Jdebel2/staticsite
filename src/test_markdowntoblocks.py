import unittest

from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_multiple_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(markdown_to_blocks(text), [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ])
    
    def test_singular_block(self):
        text = "# This is a heading\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(markdown_to_blocks(text), [text])
    

    def test_multiple_blocks_oversplit(self):
        text = "# This is a heading\n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(markdown_to_blocks(text), [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ])

if __name__ == "__main__":
    unittest.main()