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


head = "# BLOCK TO HTML"
para = "Now you need to take a block and its 'type' and convert it into an HTMLNode (I recommend a separate function for each type of block)."
quote = """
>This is a quote block
>Second line of quote block
>Let's do 3 lines
"""
code = f"print('hello world')"
un_list = """
* You can split a markdown document into blocks.
* You can determine the type of a block.
* You can create HTMLNodes that know how to render themselves as HTML strings
"""
ord_list = """
1 .Quote blocks should be surrounded by a <blockquote> tag.
2. Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag.
3. Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
4 .Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
5. Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters.
6. Paragraphs should be surrounded by a <p> tag.
"""

blocks = """
# This is a header

This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

```
This is a code block
with more code
```

>This is a quote block
>Second line of **quote** block
>Let's do 3 lines

>This is a pseudo quote block
Because the *second line* doesn't start with a >

1. This is an ordered list
2. It should say so in the block type function

* This is a list
* with items
"""
print(markdown_to_html(blocks).to_html())
# print(md_to_blockquote(quote).to_html())
# print(md_to_heading(head).to_html())
# print(md_to_paragraph(para).to_html())
# print(md_to_codeblock(code).to_html())
# print(md_to_u_list(un_list).to_html())
# print(md_to_o_list(ord_list).to_html())



