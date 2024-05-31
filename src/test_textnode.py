import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("Node here", "italics", "https://www.google.com")
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        node3 = TextNode("This is a text node", "italics", "https://www.google.com")
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node3 = TextNode("This is a text node", "italics", "https://www.google.com")
        self.assertEqual("TextNode(This is a text node, italics, https://www.google.com)", repr(node3))

    def test_text_to_html_node(self):
        node = TextNode("This is a text node", "bold")
        link_input = TextNode("To Google", "link", "https://www.google.com")
        link_node = text_node_to_html_node(link_input)
        leaf_node = text_node_to_html_node(node)
        html_node = "<b>This is a text node</b>"
        link_html = '<a href="https://www.google.com">To Google</a>'
        self.assertEqual(leaf_node, html_node)
        self.assertEqual(link_node, link_html)


if __name__ == "__main__":
    unittest.main()
