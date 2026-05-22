import unittest
from blocknode import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = ("""
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""")
        self.assertEqual([
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
              markdown_to_blocks(markdown))
        
    def test_block_to_block_type(self):
        block = "# heading"
        block2 = "This is just a paragraph"
        block3 = "```\nthis is code\n```"
        block4 = "- list item 1\n- item whocares!"
        block5 = "1. item 1\n2. item 2!"
        block6 = "> this is code\n> and this is more code"

        self.assertEqual(BlockType.HEAD, block_to_block_type(block))
        self.assertEqual(BlockType.PARA, block_to_block_type(block2))
        self.assertEqual(BlockType.CODE, block_to_block_type(block3))
        self.assertEqual(BlockType.UNORDERED, block_to_block_type(block4))
        self.assertEqual(BlockType.ORDERED, block_to_block_type(block5))
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block6))
