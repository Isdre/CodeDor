import sys
from dor_definitions import Atom
from dor_definitions import AtomType
import dor_errors
import json

# PĘTLA PO TOKENACH

with open("tokens.json","r") as file:
    tokens_file = json.load(file)
    digits = tokens_file["DIGIT"]
    actions = tokens_file["ACTION"]
    white_chars = tokens_file["WHITE"]
    open_brackets = tokens_file["OPEN_BRACKET"]
    close_brackets = tokens_file["CLOSE_BRACKET"]
    comments = tokens_file["COMMENT"]
    breakline = tokens_file["BREAKLINE"]

def Scanner(code):
    value = None
    if code in digits: value = Atom(AtomType.DIGIT, code)
    elif code in actions: value = Atom(AtomType.ACTION, code)
    elif code in white_chars: value = Atom(AtomType.WHITE, code)
    elif code in open_brackets: value = Atom(AtomType.OPEN_BRACKET, code)
    elif code in close_brackets: value = Atom(AtomType.CLOSE_BRACKET, code)
    elif code in comments: value = Atom(AtomType.COMMENT, code)
    elif code in breakline: value = Atom(AtomType.BREAKLINE, code)

    return value


def Scan(file):
    token_table = []
    for i,line in  enumerate(file):
        tokens_line = []
        token = None
        text = ""
        for j,c in enumerate(line):
            print(c,end="")
            text += c
            token = Scanner(text)
            if token is None: continue
            else: text = ""
            if token.type == AtomType.COMMENT: break
            tokens_line.append(token)
            #print(f"(\"{token.value}\",{token.type})")
        if token is None and text != "": raise dor_errors.LexicalError((text,i))
        print()
        token_table.append(tokens_line)
    return token_table

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as file:
            tokens_table = Scan(file)