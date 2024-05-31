import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph element", None, None)
        node2 = HTMLNode("a", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')



if __name__ == "__main__":
    unittest.main()
