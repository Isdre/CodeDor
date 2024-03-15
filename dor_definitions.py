from enum import Enum
class AtomType(Enum):
    DIGIT = 1
    ACTION = 2
    CLOSE_BRACKET = 3
    OPEN_BRACKET = 4
    WHITE = 5
    COMMENT = 6
    BREAKLINE = 7

class Atom:
    def __init__(self, type: AtomType, value: chr):
        self.type = type
        self.value = value
    def __str__(self):
        return self.value