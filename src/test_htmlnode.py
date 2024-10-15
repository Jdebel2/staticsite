import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_props_to_html_no_props(self):
        node = HTMLNode(None, None, None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_multiple_props_to_html(self):
        node = HTMLNode("p", "car attributes", None, {
            "brand": "Ford",
            "model": "F150",
            "color": "black",
            "type": "truck"
        })
        self.assertEqual(node.props_to_html(), " brand=\"Ford\" model=\"F150\" color=\"black\" type=\"truck\"")
    
    def test_to_html(self):
        node = HTMLNode(None, None, None, None)
        with self.assertRaises(NotImplementedError) as cm:
            node.to_html()

if __name__ == "__main__":
    unittest.main()