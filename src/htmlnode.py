class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("to_html method not implemented")
    
    def props_to_html(self):
        attributes = ""
        if self.props is not None:
            for key, value in self.props.items():
                attributes += f' {key}="{value}"'
        return attributes
    
    def __repr__(self) -> str:
        return f"HTMLNode: tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
# node2 = HTMLNode("a", "https://www.google.com", None, {"href": "https://www.google.com", "target": "_blank"})
