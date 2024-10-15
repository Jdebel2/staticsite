import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "testing text")
        self.assertEqual(node.to_html(), "<p>testing text</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "testing text")
        self.assertEqual(node.to_html(), "testing text")
    
    def test_to_html_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()