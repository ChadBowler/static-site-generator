import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph element", None, None)
        node2 = HTMLNode("a", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_leaf_eq(self):
        leaf_node = LeafNode("h1", "This is a header", {"color": "red"})
        self.assertEqual(leaf_node.to_html(), '<h1 color="red">This is a header</h1>')

    def test_parent_with_leaf_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_with_parent_eq(self):
        node = ParentNode(
            "p",
            [
                ParentNode("span", [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]),
                
            ],
        )
        self.assertEqual(node.to_html(), "<p><span>Normal text<i>italic text</i>Normal text</span></p>")

    def test_multiple_nests_eq(self):
        node = ParentNode(
            "p",
            [
                ParentNode("span", [
                    ParentNode("span", [
                        ParentNode("span", [
                            LeafNode("b", "Bold text")
                        ]),
                        LeafNode(None, "Normal text"),
                    ]),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]),
                
            ],
        )
        self.assertEqual(node.to_html(), "<p><span><span><span><b>Bold text</b></span>Normal text</span><i>italic text</i>Normal text</span></p>")

    def test_parent_with_props_eq(self):
        node = ParentNode(
            "p",
            [
                ParentNode("span", [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]),
                
            ],
            {"color": "red"}
        )
        self.assertEqual(node.to_html(), '<p color="red"><span>Normal text<i>italic text</i>Normal text</span></p>')

    def test_parent_no_children_err(self):
        node = ParentNode("p",None,{"color": "red"})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: Parent node must have children")


if __name__ == "__main__":
    unittest.main()
