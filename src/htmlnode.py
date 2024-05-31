class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = ""
        for key, value in self.props.items():
            attributes += f' {key}="{value}"'
        return attributes

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

 
# Class LeafNode inherits HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

# Class ParentNode inherits HTMLNode    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: Parent node must have a tag")
        if self.children is None:
            raise ValueError("Invalid HTML: Parent node must have children")
        node_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            if child.children is None:
                node_string += LeafNode(child.tag, child.value, child.props).to_html()
            else:
                node_string += ParentNode(child.tag, child.children, child.props).to_html()
        node_string += f"</{self.tag}>"
        return node_string
    