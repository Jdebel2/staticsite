class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Has not been implemented yet")

    def props_to_html(self):
        output = ""
        if self.props != None:
            for item in self.props:
                output += f" {item}=\"{self.props[item]}\""
        return output


    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"