import unittest
from generate_page import extract_title

class TestTextNode(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual("Hello", extract_title(markdown))

    def test_extract_title_with_white_space(self):
        markdown = "# Hello "
        self.assertEqual("Hello", extract_title(markdown))