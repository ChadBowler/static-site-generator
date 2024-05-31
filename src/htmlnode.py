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
    def __init__(self, tag, value, props):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value==None:
            raise ValueError("Leaf node must have a value.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        return super().props_to_html()

