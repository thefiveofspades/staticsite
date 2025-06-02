from enum import Enum

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.url = url
        match (text_type):
            case (TextType.BOLD.value):
                self.text_type = TextType.BOLD
            case (TextType.ITALIC.value):
                self.text_type = TextType.ITALIC
            case (TextType.CODE.value):
                self.text_type = TextType.CODE
            case (TextType.LINK.value):
                self.text_type = TextType.LINK
            case (TextType.IMAGE.value):
                self.text_type = TextType.IMAGE
            case (TextType.NORMAL.value):
                self.text_type = TextType.NORMAL
            case _:
                self.text_type = text_type
            

    def __eq__(self, comp):
        if (
            self.text == comp.text
            and self.text_type == comp.text_type
            and self.url == comp.url
        ):
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"