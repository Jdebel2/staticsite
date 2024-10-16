from splitnodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from textnode import *

def text_to_textnodes(text):
    return split_nodes_image(
        split_nodes_link(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        [TextNode(text, TextType.TEXT)], 
                        "**", 
                        TextType.BOLD
                    ),
                    "*", 
                    TextType.ITALIC
                ),
                "`", 
                TextType.CODE)
            )
        )