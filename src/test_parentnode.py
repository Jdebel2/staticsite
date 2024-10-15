import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_to_html_with_leaf_node_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("a", "Link text", {"href": "https://boot.dev"}),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i><a href=\"https://boot.dev\">Link text</a></p>")


    def test_to_html_with_parent_node_props(self):
        node = ParentNode(
            "a",
            [
                LeafNode("p", "You should "),
                LeafNode("i", "definitely "),
                LeafNode("p", "click me <3"),
            ],
            {"href": "https://notascamwebsite.com"}
        )
        self.assertEqual(node.to_html(), "<a href=\"https://notascamwebsite.com\"><p>You should </p><i>definitely </i><p>click me <3</p></a>")

    def test_to_html_nested_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode(None, "Testing "),
                ParentNode("b", [
                    LeafNode(None, "just bold text "),
                    LeafNode("i", "bold and italic text")
                ])
            ]
        )
        self.assertEqual(node.to_html(), "<p>Testing <b>just bold text <i>bold and italic text</i></b></p>")

    
    def test_to_html_multiple_nested_parent(self):
        node = ParentNode(
            "p",
            [
                ParentNode("b", [
                    ParentNode("i", [
                        LeafNode(None, "Dramatic much?")
                    ])
                ]),
                ParentNode("i", [
                    LeafNode(None, "I for one "),
                    ParentNode("b", [
                        LeafNode(None, "love overcomplicating things!!!")
                    ])
                ])
            ]
        )
        self.assertEqual(node.to_html(), "<p><b><i>Dramatic much?</i></b><i>I for one <b>love overcomplicating things!!!</b></i></p>")

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode(None, "Test failure")])
        with self.assertRaises(ValueError) as err:
            node.to_html()
        self.assertEqual(str(err.exception), "Missing tag in parent node")
    
    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError) as err:
            node.to_html()
        self.assertEqual(str(err.exception), "Missing children in children list")
    
    def test_to_html_empty_children_list(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError) as err:
            node.to_html()
        self.assertEqual(str(err.exception), "Missing children in children list")

if __name__ == "__main__":
    unittest.main()