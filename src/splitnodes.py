from textnode import *

from extractmarkdown import extract_markdown_images, extract_markdown_links

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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        images_in_text = extract_markdown_images(node.text)
        if len(images_in_text) == 0:
            new_nodes.append(node)
            continue
        
        text_to_split = node.text
        split_text = []
        for item in images_in_text:
            sections = text_to_split.split(f"![{item[0]}]({item[1]})", 1)
            text_to_split = sections.pop()
            split_text.extend(sections)
            split_text.append(f"![{item[0]}]({item[1]})")
        if text_to_split != '':
            split_text.append(text_to_split)

        image_index = 0
        converted_nodes = []
        for i in range(len(split_text)):
            item = split_text[i]
            if i % 2 == 0:
                converted_nodes.append(TextNode(item, TextType.TEXT))
            else:
                converted_nodes.append(TextNode(images_in_text[image_index][0], TextType.IMAGE, images_in_text[image_index][1]))
                image_index += 1
        if converted_nodes[0].text == '':
            converted_nodes = converted_nodes[1:]
        new_nodes.extend(converted_nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue
        links_in_text = extract_markdown_links(node.text)
        if len(links_in_text) == 0:
            new_nodes.append(node)
            continue
        
        text_to_split = node.text
        split_text = []
        for item in links_in_text:
            sections = text_to_split.split(f"[{item[0]}]({item[1]})", 1)
            text_to_split = sections.pop()
            split_text.extend(sections)
            split_text.append(f"[{item[0]}]({item[1]})")
        if text_to_split != '':
            split_text.append(text_to_split)

        links_index = 0
        converted_nodes = []
        for i in range(len(split_text)):
            item = split_text[i]
            if i % 2 == 0:
                converted_nodes.append(TextNode(item, TextType.TEXT))
            else:
                converted_nodes.append(TextNode(links_in_text[links_index][0], TextType.LINK, links_in_text[links_index][1]))
                links_index += 1
        if converted_nodes[0].text == '':
            converted_nodes = converted_nodes[1:]
        new_nodes.extend(converted_nodes)
    return new_nodes