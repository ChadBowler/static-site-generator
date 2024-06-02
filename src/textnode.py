from htmlnode import LeafNode

# class Text_types():
#     text = "text"
#     bold = "bold"
#     italic = "italic"
#     code = "code"
#     link = "link"
#     image = "image"

TEXT = "text"
BOLD = "bold"
ITALIC = "italic"
CODE = "code"
LINK = "link"
IMAGE = "image"
delimiters = {"**": BOLD, "*": ITALIC, "`": CODE}

# text_type_text = "text"
# text_type_bold = "bold"
# text_type_italic = "italic"
# text_type_code = "code"
# text_type_link = "link"
# text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text, None).to_html()
        case "bold":
            return LeafNode("b", text_node.text, None).to_html()
        case "italic":
            return LeafNode('i', text_node.text, None).to_html()
        case "code":
            return LeafNode("code", text_node.text, None).to_html()
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url}).to_html()
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}).to_html()
        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")
        
# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for node in old_nodes:
#         if node.text_type != TEXT:
#             new_nodes.append(node)
#         else:
#             split_node = node.text.split(delimiter)
        
# def split_nodes(node_string):
#     outgoing_type = ""
#     node_array = node_string.split(" ")
#     return node_array



