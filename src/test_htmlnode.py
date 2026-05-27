import unittest
from htmlnode import *

test_prob = {
                "href": "https://www.google.com",
                "target": "_blank",
        }

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):

        node = HTMLNode("h1", "This is a prop test", None, test_prob)

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertNotEqual(node.props_to_html(), 'href="wrong.com"')

    def test_props_to_html_is_None(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_return_value(self):
        node = HTMLNode("h1","This is a test", ['node1', 'node2'], test_prob)
        self.assertEqual(node.__repr__(), 
                         "HTMLNode(h1, This is a test, children: ['node1', 'node2'], {'href': 'https://www.google.com', 'target': '_blank'})"
                         )
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",
                         )