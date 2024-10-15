from textnode import *
from leafnode import LeafNode


def validate_text_node_text(text_node):
    if text_node.text == None:
        raise Exception("Missing text in text node")


def validate_text_node_url(text_node):
    if text_node.url == None:
        raise Exception("Missing url in text node")


def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT.value:
            validate_text_node_text(text_node)
            return LeafNode(None, text_node.text)
        case TextType.BOLD.value:
            validate_text_node_text(text_node)
            return LeafNode("b", text_node.text)
        case TextType.ITALIC.value:
            validate_text_node_text(text_node)
            return LeafNode("i", text_node.text)
        case TextType.CODE.value:
            validate_text_node_text(text_node)
            return LeafNode("code", text_node.text)
        case TextType.LINK.value:
            validate_text_node_text(text_node)
            validate_text_node_url(text_node)
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE.value:
            validate_text_node_text(text_node)
            validate_text_node_url(text_node)
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})