from enum import Enum
class AtomType(Enum):
    DIGIT = 0
    ACTION = 1
    CLOSE_BRACKET = 2
    OPEN_BRACKET = 3
    WHITE = 4
    COMMENT = 5
    BREAKLINE = 6

class Atom:
    def __init__(self, type: AtomType, value: chr):
        self.type = type
        self.value = value
    def __str__(self):
        return self.value