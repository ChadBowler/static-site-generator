import unittest

from textnode import (
    TextNode,
    TEXT,
    BOLD,
    ITALIC,
    CODE,
    LINK,
    IMAGE,
    delimiters
)
from inline_markdown import split_nodes_delimiter, text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TEXT)
        new_nodes = split_nodes_delimiter([node], "`", CODE)
        test_nodes = [
            TextNode("This is text with a ", TEXT),
            TextNode("code block", CODE),
            TextNode(" word", TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)

    def test_bold(self):
        node = TextNode("For simplicity's sake, **we won't allow it!** We will only support a single level of...", TEXT)
        new_nodes = split_nodes_delimiter([node], "**", BOLD)
        test_nodes = [
            TextNode("For simplicity's sake, ", TEXT),
            TextNode("we won't allow it!", BOLD),
            TextNode(" We will only support a single level of...", TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)


    def test_italic(self):
        node = TextNode("Markdown parsers often support the *nesting* of inline elements. For example, you can have a bold word inside of italics:", TEXT)
        new_nodes = split_nodes_delimiter([node], "*", ITALIC)
        test_nodes = [
            TextNode("Markdown parsers often support the ", TEXT),
            TextNode("nesting", ITALIC),
            TextNode(" of inline elements. For example, you can have a bold word inside of italics:", TEXT),
        ]
        self.assertEqual(new_nodes, test_nodes)          

    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        test_nodes = [
                        TextNode("This is ", TEXT),
                        TextNode("text", BOLD),
                        TextNode(" with an ", TEXT),
                        TextNode("italic", ITALIC),
                        TextNode(" word and a ", TEXT),
                        TextNode("code block", CODE),
                        TextNode(" and an ", TEXT),
                        TextNode("image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                        TextNode(" and a ", TEXT),
                        TextNode("link", LINK, "https://boot.dev"),
                    ]
        self.assertEqual(new_nodes, test_nodes)

if __name__ == "__main__":
    unittest.main()
