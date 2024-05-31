import unittest

from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph element", None, None)
        node2 = HTMLNode("a", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_leaf_eq(self):
        leaf_node = LeafNode("h1", "This is a header", {"color": "red"})
        self.assertEqual(leaf_node.to_html(), '<h1 color="red">This is a header</h1>')


if __name__ == "__main__":
    unittest.main()
