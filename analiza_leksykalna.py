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
    ignore = tokens_file["IGNORE"]

def Scanner(code):
    value = None
    if code in digits: value = Atom(AtomType.DIGIT, code)
    elif code in actions: value = Atom(AtomType.ACTION, code)
    elif code in white_chars: value = Atom(AtomType.WHITE, code)
    elif code in open_brackets: value = Atom(AtomType.OPEN_BRACKET, code)
    elif code in comments: value = Atom(AtomType.COMMENT, code)
    elif code in close_brackets: value = Atom(AtomType.CLOSE_BRACKET, code)
    elif code in ignore: value = Atom(AtomType.WHITE, "")

    return value

def Scan(file):
    token_table = []
    for i,line in  enumerate(file):
        tokens_line = []
        for j,c in enumerate(line):
            token = Scanner(c)
            if token is None: raise dor_errors.LexicalError((c,i,j))
            if token.type == AtomType.COMMENT: break
            tokens_line.append(token)
            print(f"(\"{token.value}\",{token.type})")
        token_table.append(tokens_line)
    return token_table

def Parser(token_table:list[list[Atom]]):
    braket_control = 0
    last_token = Atom(AtomType.WHITE," ")
    last_action = False
    last_digit = False
    for line_number, tokens_line in enumerate(token_table):
        if braket_control != 0: raise dor_errors.BraketCountError(braket_control,line_number)
        if last_action: raise dor_errors.EndLineError(last_token.value)
        # pierwszy token to działanie, nawias zamykający
        if tokens_line[0].type == AtomType.ACTION or tokens_line[0].type == AtomType.CLOSE_BRACKET: raise dor_errors.StartLineError(tokens_line[0].value)
        for token_number, t in enumerate(tokens_line):
            #gdy nawias zamykający występuje po działaniu
            if t.type == AtomType.CLOSE_BRACKET and last_action: raise dor_errors.OtherSynteaxError("Closing bracket can't stand after action")
            #gdy działanie występuje po nawiasie otwierającym
            if last_token.type == AtomType.OPEN_BRACKET and t.type == AtomType.ACTION: raise dor_errors.OtherSynteaxError("Action can't stand after opening bracket")

            last_token = t
            last_action = False
            last_digit = False

            if last_token.type == AtomType.OPEN_BRACKET: braket_control -= 1
            elif last_token.type == AtomType.CLOSE_BRACKET: braket_control += 1

            if last_token.type == AtomType.DIGIT: last_digit = True
            elif last_token.type == AtomType.ACTION: last_action = True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as file:
            tokens_table = Scan(file)
            # Parser(tokens_table)
            # with open("wynik.py","w") as result:
            #     for line in tokens_table:
            #         result.write("print(f\"")
            #         x = ""
            #         for y in line: x += str(y)
            #         result.write(x+" = {")
            #         result.write(x)
            #         result.write("}\")\n")