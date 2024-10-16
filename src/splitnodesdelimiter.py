from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        split_text = []
        
        if delimiter == '*' and node.text.count("**") > 0:
            split_bold = node.text.split("**")
            split_bold_and_italic = list(map(lambda elt: elt.split(delimiter) if len(elt.split(delimiter)) > 1 else elt, split_bold))
            for i in range(1, len(split_bold_and_italic), 2):
                split_bold_and_italic[i] = f"**{split_bold_and_italic[i]}**"
            entry = ""
            for item in split_bold_and_italic:
                if not isinstance(item, list):
                    entry += item
                else:
                    split_text.append(entry + item[0])
                    split_text.append(item[1])
                    entry = item[2]
            if entry != "":
                split_text.append(entry)
        else:
            split_text = node.text.split(delimiter)
        
        if len(split_text) % 2 == 0:
            raise Exception("Invalid markdown, missing delimiter")
        
        if split_text[len(split_text)-1] == '':
            split_text = split_text[:len(split_text)-1]
        
        converted_nodes = []
        for i in range(len(split_text)):
            item = split_text[i]
            if i % 2 == 0:
                converted_nodes.append(TextNode(item, TextType.TEXT))
            else:
                converted_nodes.append(TextNode(item, text_type))
        if converted_nodes[0].text == '':
            converted_nodes = converted_nodes[1:]
        new_nodes.extend(converted_nodes)
    return new_nodes

def split_nodes_solution(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes