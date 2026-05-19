from textnode import TextNode, TextType

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



