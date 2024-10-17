from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type
from parentnode import ParentNode
from textnode import *
from texttotextnode import text_to_textnodes
from textnodetohtmlnode import text_node_to_html_node

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)

    node_children = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        match (block_type):
            case 'quote':
                block_unquoted = "".join(list(map(str.lstrip, block.split('>'))))
                paragraph_children = []
                paragraph_children.append(ParentNode("p", text_to_children(block_unquoted)))
                node_children.append(ParentNode("blockquote", paragraph_children))
            case 'unordered_list':
                block_unlined = ""
                if block[0] == '*':
                    block_unlined = "".join(list(map(str.lstrip, block.split('*'))))
                elif block[0] == '-':
                    block_unlined = "".join(list(map(str.lstrip, block.split('-'))))
                line_children = []
                split_block = block_unlined.split("\n")
                for item in split_block:
                    line_children.append(ParentNode("li", text_to_children(item)))
                node_children.append(ParentNode("ul", line_children))
            case 'ordered_list':
                line_children = []
                split_block = block.split("\n")
                for item in split_block:
                    n_item = item[2:].lstrip()
                    line_children.append(ParentNode("li", text_to_children(n_item)))
                node_children.append(ParentNode("ol", line_children))
            case 'code':
                pre_children = []
                split_block = block.split("\n")
                for item in split_block:
                    n_item = item[3:len(item)-3]
                    pre_children.append(ParentNode("code", text_to_children(n_item)))
                node_children.append(ParentNode("pre", pre_children))
            case 'heading':
                header = block.split(" ")[0]
                header_len = len(header)
                text_no_header = ""
                for line in block.split('\n'):
                    if text_no_header == "":
                        text_no_header += line[header_len+1:]
                    else:
                        text_no_header += "\n"+line[header_len+1:]
                node_children.append(ParentNode(f"h{header_len}", text_to_children(text_no_header)))
            case 'paragraph':
                node_children.append(ParentNode("p", text_to_children(block)))
    return ParentNode("div", node_children)

def text_to_children(text):
    html_nodes = []
    for item in text_to_textnodes(text):
        html_nodes.append(text_node_to_html_node(item))
    return html_nodes