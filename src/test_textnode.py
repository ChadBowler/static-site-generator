import unittest

from textnode import TextNode


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
        # node = TextNode("This is a text node", "bold")
        # node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        node3 = TextNode("This is a text node", "italics", "https://www.google.com")
        self.assertEqual("TextNode(This is a text node, italics, https://www.google.com)", repr(node3))


if __name__ == "__main__":
    unittest.main()
