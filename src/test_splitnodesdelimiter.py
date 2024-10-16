import unittest

from splitnodesdelimiter import split_nodes_delimiter, split_nodes_solution

from textnode import *

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_one_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_multiple_same_delimiters(self):
        node = TextNode("Hello `World`! This is `python`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("World", TextType.CODE),
            TextNode("! This is ", TextType.TEXT),
            TextNode("python", TextType.CODE)
        ])
    
    def test_multiple_different_delimiters(self):
        node = TextNode("Hello *World*! This is `python`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("Hello *World*! This is ", TextType.TEXT),
            TextNode("python", TextType.CODE)
        ])
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("Hello ", TextType.TEXT),
            TextNode("World", TextType.ITALIC),
            TextNode("! This is ", TextType.TEXT),
            TextNode("python", TextType.CODE)
        ])
    
    def test_delimiter_at_start(self):
        node = TextNode("`This` is text with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This", TextType.CODE),
            TextNode(" is text with a code block word", TextType.TEXT)
        ])

    def test_bold_with_italics(self):
        node = TextNode("**bold** text and *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("bold", TextType.BOLD),
            TextNode(" text and *italic* text", TextType.TEXT)
        ])

    def test_italics_with_bold(self):
        node = TextNode("**bold** text and *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("**bold** text and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_italics_with_bold_against_solution(self):
        node = TextNode("**bold** text and *italic* text", TextType.TEXT)
        new_nodes = split_nodes_solution([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("**bold** text and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_italics_no_bold(self):
        node = TextNode("bold text and *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("bold text and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ])
    
    def test_incorrect_number_of_delimiters(self):
        node = TextNode("bold text and *italic text", TextType.TEXT)
        with self.assertRaises(Exception) as err:
            new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(str(err.exception), "Invalid markdown, missing delimiter")


if __name__ == "__main__":
    unittest.main()