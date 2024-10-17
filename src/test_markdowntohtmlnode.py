import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from markdowntohtmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph_block(self):
        markdown = "This is a **basic** paragraph block, *nothing* fancy.\nJust be sure that `markdown_to_html_node()` works as intended."
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>This is a <b>basic</b> paragraph block, <i>nothing</i> fancy.\nJust be sure that <code>markdown_to_html_node()</code> works as intended.</p></div>"
        self.assertEqual(html, expected)
    
    def test_quote_block(self):
        markdown = "Script of The Bee Movie:\n\n> According to all known laws of aviation, there is no way a bee should be able to fly.\n> Its little round body should be too big to move its weight.\n> The bee flies anyway, for it does not care for the laws of physics."
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>Script of The Bee Movie:</p><blockquote><p>According to all known laws of aviation, there is no way a bee should be able to fly.\nIts little round body should be too big to move its weight.\nThe bee flies anyway, for it does not care for the laws of physics.</p></blockquote></div>"
        self.assertEqual(html, expected)

    def test_unordered_list_block_hyphen(self):
        markdown = "People I don't really like\n\n- You\n- Myself\n- Simon Cowell\n- I really hate Simon Cowell"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>People I don't really like</p><ul><li>You</li><li>Myself</li><li>Simon Cowell</li><li>I really hate Simon Cowell</li></ul></div>"
        self.assertEqual(html, expected)
    
    def test_unordered_list_block_asterisk(self):
        markdown = "People I don't really like\n\n* You\n* Myself\n* Simon Cowell\n* I really hate Simon Cowell"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>People I don't really like</p><ul><li>You</li><li>Myself</li><li>Simon Cowell</li><li>I really hate Simon Cowell</li></ul></div>"
        self.assertEqual(html, expected)
    
    def test_unordered_list_block_asterisk(self):
        markdown = "People I don't really like\n\n1. You\n2. Myself\n3. Simon Cowell\n4. I really hate Simon Cowell"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>People I don't really like</p><ol><li>You</li><li>Myself</li><li>Simon Cowell</li><li>I really hate Simon Cowell</li></ol></div>"
        self.assertEqual(html, expected)
    
    def test_code_block(self):
        markdown = "Look at this code block:\n\n```print('hello world!')```\n\nIt prints hello world - that's so cool!"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>Look at this code block:</p><pre><code>print('hello world!')</code></pre><p>It prints hello world - that's so cool!</p></div>"
        self.assertEqual(html, expected)
    
    def test_heading_one_block(self):
        markdown = "Here are the rules of the bar:\n\n# All bubble blowing bubble babies will be beaten\n# mercilessly by every able-bodied patron of the bar\n\nAny questions?"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>Here are the rules of the bar:</p><h1>All bubble blowing bubble babies will be beaten\nmercilessly by every able-bodied patron of the bar</h1><p>Any questions?</p></div>"
        self.assertEqual(html, expected)
    
    def test_heading_six_block(self):
        markdown = "Here are the rules of the bar:\n\n###### All bubble blowing bubble babies will be beaten\n###### mercilessly by every able-bodied patron of the bar\n\nAny questions?"
        html_node = markdown_to_html_node(markdown)
        html = html_node.to_html()
        expected = "<div><p>Here are the rules of the bar:</p><h6>All bubble blowing bubble babies will be beaten\nmercilessly by every able-bodied patron of the bar</h6><p>Any questions?</p></div>"
        self.assertEqual(html, expected)

if __name__ == "__main__":
    unittest.main()