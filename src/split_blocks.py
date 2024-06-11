import re
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node, CODE
from inline_markdown import text_to_textnodes

PARAGRAPH = "paragraph"
HEADING = "heading"
QUOTE = "quote"
UNORDERED_LIST = "unordered_list"
ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = re.split(r"[\n]{2}", markdown)
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        stripped_blocks.append(block.strip())
    return stripped_blocks

def block_to_block(block):
    block_type = ""
    lines = block.split("\n")
    if (block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")):
        block_type = HEADING
    elif block[:3] == "```" and block[-3:] == "```":
        block_type = CODE
    elif block.startswith(">"):
        block_type = QUOTE
        for line in lines:
            if not line.startswith(">"):
                block_type = PARAGRAPH   
    elif block.startswith("* "):
        block_type = UNORDERED_LIST
        for line in lines:
            if not line.startswith("* "):
                block_type = PARAGRAPH
    elif block.startswith("- "):
        block_type = UNORDERED_LIST
        for line in lines:
            if not line.startswith("- "):
                block_type = PARAGRAPH
    elif block.startswith("1. "):
        block_type = ORDERED_LIST
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                block_type = PARAGRAPH
            i += 1
    else:
        block_type = PARAGRAPH

    return block_type

def parse_text(text):
    text_nodes = text_to_textnodes(text)
    nodes = []
    for node in text_nodes:
        nodes.append(text_node_to_html_node(node))
    return nodes

def md_to_blockquote(block):
    lines = block.split("\n")
    new_lines = []
    new_block = ""
    for line in lines:
        line = line.replace(">", "")
        new_lines.append(line)
    new_block = "\n".join(new_lines)
    nodes = parse_text(new_block)
    return ParentNode("quoteblock", nodes)
def md_to_u_list(block):
    lines = block.split("\n")
    children = []
    new_block = []
    for line in lines:
        if line == "":
            continue
        line = line.split(" ", 1)[1]
        line_node = text_to_textnodes(line)
        children.append(ParentNode("li", [text_node_to_html_node(line_node[0])]))
        new_block.append(line)
    block = "\n".join(new_block)
    list_head = ParentNode("ul", children)
    return list_head
def md_to_o_list(block):
    lines = block.split("\n")
    children = []
    new_block = []
    for line in lines:
        if line == "":
            continue
        line = line.split(" ", 1)[1]
        line_node = text_to_textnodes(line)
        children.append(ParentNode("li", [text_node_to_html_node(line_node[0])]))
        new_block.append(line)
    block = "\n".join(new_block)
    list_head = ParentNode("ol", children)
    return list_head
def md_to_codeblock(block):
    block = block.replace("```", "")
    nodes = parse_text(block)
    elements = []
    elements.append(ParentNode(CODE, nodes))
    return ParentNode("pre", elements)
def md_to_heading(block):
    tag = ""
    if block.startswith("# "):
        tag = "h1"
    elif block.startswith("## "):
        tag = "h2"
    elif block.startswith("### "):
        tag = "h3"
    elif block.startswith("#### "):
        tag = "h4"
    elif block.startswith("##### "):
        tag = "h5"
    elif block.startswith("###### "):
        tag = "h6"
    block = block.split(" ", 1)[1]
    nodes = parse_text(block)
    return ParentNode(tag, nodes)
def md_to_paragraph(block):
    nodes = parse_text(block)
    return ParentNode("p", nodes)

def markdown_to_html(markdown):
    split_blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in split_blocks:
        type_of_block = block_to_block(block)
        if type_of_block == PARAGRAPH:
            block = md_to_paragraph(block)
        elif type_of_block == HEADING:
            block = md_to_heading(block)
        elif type_of_block == QUOTE:
            block = md_to_blockquote(block)
        elif type_of_block == UNORDERED_LIST:
            block = md_to_u_list(block)
        elif type_of_block == ORDERED_LIST:
            block = md_to_o_list(block)
        elif type_of_block == CODE:
            block = md_to_codeblock(block)
        else:
            raise ValueError("Type of block not valid markdown")    
        nodes.append(block)
    top_lvl_element = ParentNode("div", nodes)
    return top_lvl_element
