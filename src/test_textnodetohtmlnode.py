import unittest

from textnodetohtmlnode import text_node_to_html_node
from textnode import *
from leafnode import LeafNode

class TestTextnodeToHTMLNode(unittest.TestCase):
    def test_text_case(self):
        node = TextNode("I am a text node", TextType.TEXT)
        leafnode = text_node_to_html_node(node)
        expected = LeafNode(None, "I am a text node")
        self.assertEqual(leafnode.tag, expected.tag)
        self.assertEqual(leafnode.value, expected.value)
        self.assertEqual(leafnode.props, expected.props)

    def test_bold_case(self):
        node = TextNode("I am a text node", TextType.BOLD)
        leafnode = text_node_to_html_node(node)
        expected = LeafNode("b", "I am a text node")
        self.assertEqual(leafnode.tag, expected.tag)
        self.assertEqual(leafnode.value, expected.value)
        self.assertEqual(leafnode.props, expected.props)
    
    def test_italics_case(self):
        node = TextNode("I am a text node", TextType.ITALIC)
        leafnode = text_node_to_html_node(node)
        expected = LeafNode("i", "I am a text node")
        self.assertEqual(leafnode.tag, expected.tag)
        self.assertEqual(leafnode.value, expected.value)
        self.assertEqual(leafnode.props, expected.props)
    
    def test_code_case(self):
        node = TextNode("I am a text node", TextType.CODE)
        leafnode = text_node_to_html_node(node)
        expected = LeafNode("code", "I am a text node")
        self.assertEqual(leafnode.tag, expected.tag)
        self.assertEqual(leafnode.value, expected.value)
        self.assertEqual(leafnode.props, expected.props)
    
    def test_link_case(self):
        node = TextNode("I am a text node", TextType.LINK, "https://boot.dev")
        leafnode = text_node_to_html_node(node)
        expected = LeafNode("a", "I am a text node", {"href": "https://boot.dev"})
        self.assertEqual(leafnode.tag, expected.tag)
        self.assertEqual(leafnode.value, expected.value)
        self.assertEqual(leafnode.props, expected.props)

    def test_image_case(self):
        node = TextNode("I am a text node", TextType.IMAGE, "https://boot.dev")
        leafnode = text_node_to_html_node(node)
        expected = LeafNode("img", "", {"src": "https://boot.dev", "alt": "I am a text node"})
        self.assertEqual(leafnode.tag, expected.tag)
        self.assertEqual(leafnode.value, expected.value)
        self.assertEqual(leafnode.props, expected.props)

    def test_invalid_text_case(self):
        node = TextNode(None, TextType.TEXT)
        with self.assertRaises(Exception) as err:
            leafnode = text_node_to_html_node(node)
        self.assertEqual(str(err.exception), "Missing text in text node")
    
    def test_invalid_url_case(self):
        node = TextNode("Text exists", TextType.LINK, None)
        with self.assertRaises(Exception) as err:
            leafnode = text_node_to_html_node(node)
        self.assertEqual(str(err.exception), "Missing url in text node")

if __name__ == "__main__":
    unittest.main()

    