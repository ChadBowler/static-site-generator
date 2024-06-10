from textnode import (
    TextNode,
    TEXT,
    BOLD,
    ITALIC,
    CODE,
    LINK,
    IMAGE
)
from extract_links import split_nodes_image, split_nodes_link

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", BOLD)
    nodes = split_nodes_delimiter(nodes, "*", ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

