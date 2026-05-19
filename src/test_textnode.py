import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text", TextType.ITALIC)
        node4 = TextNode("This is code", TextType.CODE)
        node5 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node6 = TextNode("This is a link", TextType.LINK, None)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()