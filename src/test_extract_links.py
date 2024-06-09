import unittest

from extract_links import (
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_image,
    split_nodes_link,
    TextNode, 
    TEXT,
    IMAGE,
    LINK)

class TestTextNode(unittest.TestCase):
    def test_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted = extract_markdown_images(text)
        output = [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')]
        self.assertEqual(extracted, output)
        
    def test_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extracted = extract_markdown_links(text)
        output = [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]
        self.assertEqual(extracted, output)

    def test_node_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            TEXT,
        )
        new_nodes = split_nodes_image([node])
        output = [
                TextNode("This is text with an ", TEXT),
                TextNode("image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", TEXT),
                TextNode(
                    "second image", IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                    ),
                ]
        self.assertEqual(new_nodes, output)

    def test_node_split_link(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png) with some extra text at the end.",
            TEXT,
        )
        new_nodes = split_nodes_link([node])
        output = [
                TextNode("This is text with a ", TEXT),
                TextNode("link", LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and another ", TEXT),
                TextNode(
                    "second link", LINK, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
                    ),
                TextNode(" with some extra text at the end.", TEXT)
                ]
        self.assertEqual(new_nodes, output)

if __name__ == "__main__":
    unittest.main()