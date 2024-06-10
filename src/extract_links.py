import re
from textnode import (
    TextNode,
    TEXT,
    BOLD,
    ITALIC,
    CODE,
    LINK,
    IMAGE,
)

def extract_markdown_images(text):
    reg_pattern = r"!\[(.*?)\]\((.*?)\)"
    images = re.findall(reg_pattern, text)
    return images

def extract_markdown_links(text):
    reg_pattern = r"\[(.*?)\]\((.*?)\)"
    images = re.findall(reg_pattern, text)
    return images


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
        else:
            for image in images:
                sections = old_node.text.split(f"![{image[0]}]({image[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                split_nodes.append(TextNode(sections[0], TEXT))
                split_nodes.append(TextNode(image[0], IMAGE, image[1]))
                old_node.text = sections[-1]
            if old_node.text:
                split_nodes.append(TextNode(old_node.text, TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
        else:
            for link in links:
                sections = old_node.text.split(f"[{link[0]}]({link[1]})", 1)
                split_nodes.append(TextNode(sections[0], TEXT))
                split_nodes.append(TextNode(link[0], LINK, link[1]))
                old_node.text = sections[-1]
            if old_node.text:
                split_nodes.append(TextNode(old_node.text, TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes
