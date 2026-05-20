from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes_list.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Invalid delimiter, unclosed markdown")
        for i in range(len(split_node)):
            if i % 2 == 0:
                new_nodes_list.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_nodes_list.append(TextNode(split_node[i], text_type))
    return new_nodes_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes_list.append(node)
            continue
        images_list = extract_markdown_images(node.text)
        if not images_list:
            new_nodes_list.append(node)
            continue
        remaining_text = node.text
        for image in images_list:
            split_node = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_node[0]) != 0:
                new_nodes_list.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            remaining_text = split_node[1]
        if len(split_node[1]) != 0:
            new_nodes_list.append(TextNode(split_node[1], TextType.TEXT))
    return new_nodes_list

def split_nodes_link(old_nodes):
    new_nodes_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes_list.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes_list.append(node)
            continue
        current_text = node.text
        for link in links:
            split_node = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if split_node[0]:
                new_nodes_list.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes_list.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = split_node[1]
        if current_text:
            new_nodes_list.append(TextNode(current_text, TextType.TEXT))
    return new_nodes_list

def text_to_textnodes(text):
    first_node = [(TextNode(text, TextType.TEXT))]
    with_bold = split_nodes_delimiter(first_node, "**", TextType.BOLD)
    with_code = split_nodes_delimiter(with_bold, "`", TextType.CODE)
    with_italics = split_nodes_delimiter(with_code, "_", TextType.ITALIC)
    with_images = split_nodes_image(with_italics)
    with_links_final = split_nodes_link(with_images)
    return with_links_final