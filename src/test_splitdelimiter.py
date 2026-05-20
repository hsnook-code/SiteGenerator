import unittest
from splitdelimiter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, \
split_nodes_image, split_nodes_link, text_to_textnodes

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    old_nodes = [
TextNode("I have `code` in my text", TextType.TEXT),
TextNode("My text has **bold** in it", TextType.TEXT),
TextNode("_Just italics_", TextType.ITALIC)
    ]
    def test_code(self):
        new_nodes = split_nodes_delimiter(self.old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
    TextNode("I have ", TextType.TEXT),
    TextNode("code", TextType.CODE),
    TextNode(" in my text", TextType.TEXT),
    TextNode("My text has **bold** in it", TextType.TEXT),
    TextNode("_Just italics_", TextType.ITALIC),
])
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_textract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_nodes_image(self):
        old_nodes = [
            TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
        ]
        self.assertEqual([
    TextNode("This is text with an ", TextType.TEXT),
    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
],
            split_nodes_image(old_nodes))
        
    def test_split_nodes_link(self):
        old_nodes = [
            TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
        ]
        self.assertEqual([
    TextNode("This is text with a link ", TextType.TEXT),
    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
],
split_nodes_link(old_nodes)

        )

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