import unittest
from splitdelimiter import split_nodes_delimiter
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