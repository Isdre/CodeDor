from enum import Enum
class AtomType(Enum):
    DIGIT = "digit"
    ACTION = "action"
    CLOSE_BRACKET = "close_bracket"
    OPEN_BRACKET = "open_bracket"
    WHITE = "white"
    COMMENT = "comment"
    BREAKLINE = "breakline"

class Atom:
    def __init__(self, type: AtomType, value: chr):
        self.type = type
        self.value = value
    def __str__(self):
        return self.value

class Comment(Atom):
    def __init__(self, type: AtomType, value: chr, text:str = ""):
        self.type = type
        self.value = value
        self.text = text