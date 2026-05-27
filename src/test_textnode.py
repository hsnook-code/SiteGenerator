import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from splitdelimiter import text_to_textnodes


node = TextNode("This is a text node", TextType.TEXT)
node2 = TextNode("This is a text node", TextType.TEXT)
node3 = TextNode("This is a text", TextType.ITALIC)
node4 = TextNode("This is code", TextType.CODE)
node5 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
node6 = TextNode("This is a link", TextType.LINK, None)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node5, node6)
     
    def test_text_node_to_html_node(self):
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_textnodes(self):
        text = ("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertEqual([
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
],text_to_textnodes(text)
)