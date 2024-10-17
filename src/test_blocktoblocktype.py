import unittest

from blocktoblocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        md = "This is a paragraph block\nThis shouldn't be anything except for a paragraph block."
        self.assertEqual(block_to_block_type(md), "paragraph")
    
    def test_heading(self):
        md = "# This is a heading block\n# This shouldn't be anything except for a heading block."
        self.assertEqual(block_to_block_type(md), "heading")
    
    def test_heading_6(self):
        md = "###### This is a h6 block\n###### This shouldn't be anything except for a h6 block."
        self.assertEqual(block_to_block_type(md), "heading")
    
    def test_code(self):
        md = "```\nprint(\"this is a code block\")\n```"
        self.assertEqual(block_to_block_type(md), "code")
    
    def test_quote(self):
        md = "> Be me\n> 24 year old bootdev programmer"
        self.assertEqual(block_to_block_type(md), "quote")
    
    def test_unordered_list_asterisk(self):
        md = "* This is an unordered list\n* We can put any element in any order here"
        self.assertEqual(block_to_block_type(md), "unordered_list")

    def test_unordered_list_hyphen(self):
        md = "- This is an unordered list\n- We can put any element in any order here"
        self.assertEqual(block_to_block_type(md), "unordered_list")
    
    def test_ordered_list(self):
        md = "1. This is an ordered list\n2. We can put any element in here\n3. As long as they are in order numerically"
        self.assertEqual(block_to_block_type(md), "ordered_list")
    
    def test_broken_ordered_list(self):
        md = "1. This is an ordered list\n2. We can put any element in here\n2. As long as they are in order numerically"
        self.assertEqual(block_to_block_type(md), "paragraph")


if __name__ == "__main__":
    unittest.main()