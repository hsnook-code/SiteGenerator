from htmlnode import ParentNode
from blocknode import BlockType, markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node, TextNode, TextType
from splitdelimiter import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    list_of_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEAD:
            list_of_nodes.append(heading_to_html(block))
        elif block_type == BlockType.PARA:
            list_of_nodes.append(para_to_html(block))
        elif block_type == BlockType.CODE:
            list_of_nodes.append(code_to_html(block))
        elif block_type == BlockType.QUOTE:
            list_of_nodes.append(quote_to_html(block))
        elif block_type == BlockType.UNORDERED:
            list_of_nodes.append(unordered_list_to_html(block))
        elif block_type == BlockType.ORDERED:
            list_of_nodes.append(ordered_list_to_html(block))
        else:
            raise ValueError("Block does not have valid type!")
    return ParentNode("div", list_of_nodes)


def text_to_children(text):
    list_of_text_nodes = text_to_textnodes(text)
    list_of_children = []
    for text_node in list_of_text_nodes:
        new_html_node = text_node_to_html_node(text_node)
        list_of_children.append(new_html_node)
    return list_of_children

def para_to_html(block):
    tag = "p"
    value = block.replace("\n", " ")
    return ParentNode(tag, text_to_children(value))

def heading_to_html(block):
    number_of_hash = 0
    for char in block:
        if char == "#":
            number_of_hash += 1
        else:
            break
    if number_of_hash > 6 or number_of_hash == 0:
        raise ValueError("Invalid heading level")
    tag = f"h{number_of_hash}"
    value = block[number_of_hash + 1:]
    return ParentNode(tag, text_to_children(value))

def code_to_html(block):
    value = block[4:-3]
    html_node = text_node_to_html_node(TextNode(value, TextType.CODE))
    return ParentNode("pre", [html_node])

def quote_to_html(block):
    lines = []
    for line in block.split("\n"):
        lines.append(line[2:])
    value = " ".join(lines)
    return ParentNode("blockquote", text_to_children(value))

def unordered_list_to_html(block):
    tag = "ul"
    line_nodes = []
    lines = block.split("\n")
    for line in lines:
        line_nodes.append(ParentNode("li", text_to_children(line[2:])))
    return ParentNode(tag, line_nodes)

def ordered_list_to_html(block):
    tag = "ol"
    line_nodes = []
    lines = block.split("\n")
    for line in lines:
        line_nodes.append(ParentNode("li", text_to_children(line.split(". ", 1)[1])))
    return ParentNode(tag, line_nodes)