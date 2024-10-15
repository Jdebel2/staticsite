from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag in parent node")
        if self.children == None or len(self.children) == 0:
            raise ValueError("Missing children in children list")
        
        output = ""
        output += f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"
        return output