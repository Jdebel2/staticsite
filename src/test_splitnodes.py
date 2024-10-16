import unittest

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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


class TestSplitNodesImagesAndLinks(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,  [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ])
    

    def test_split_nodes_link_at_start(self):
        node = TextNode(
            "[Here](https://www.boot.dev) is the location of the One Piece",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes,  [
            TextNode("Here", TextType.LINK, "https://www.boot.dev"),
            TextNode(" is the location of the One Piece", TextType.TEXT)
        ])


    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes,  [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ])
    

    def test_split_nodes_image_at_start(self):
        node = TextNode(
            "![Here](https://www.boot.dev) is the location of the One Piece",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes,  [
            TextNode("Here", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" is the location of the One Piece", TextType.TEXT)
        ])
    

    def test_split_nodes_image_and_links(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and a link [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes,  [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and a link [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
        ])
        new_nodes = split_nodes_link(new_nodes)
        self.assertEqual(new_nodes,  [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and a link ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ])
        

if __name__ == "__main__":
    unittest.main()