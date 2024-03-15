import sys
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
parent_folder = os.path.abspath(os.path.join(current_folder, ''))
sys.path.append(parent_folder+"\definitions")
print(parent_folder+"\definitions")


from definitions.dor_definitions import *
from definitions.dor_errors import *
import json

# PĘTLA PO TOKENACH

with open("tokens.json", "r") as file:
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
    elif code in comments: value = Comment(AtomType.COMMENT, code)
    elif code in breakline: value = Atom(AtomType.BREAKLINE, code)

    return value

def Scan(scanTarget):
    token_table = []
    for i,line in  enumerate(scanTarget):
        tokens_line = []
        token = None
        text = ""
        for j,c in enumerate(line):
            #print(c,end="")
            text += c
            token = Scanner(text)
            if token is None: continue
            else: text = ""
            if token.type == AtomType.COMMENT: break
            tokens_line.append(token)
            # print(f"(\"{token.value}\",{token.type})")

        if token.type == AtomType.COMMENT:
            token.text = line[line.find(token.value):]
            #print(token.text)
            tokens_line.append(token)

        if token is None and text != "": raise LexicalError((text, i))
        #print()
        token_table.append(tokens_line)
    return token_table

def ColorHtml(table):
    with open("kolorowanie_dane/result.html", "w") as file:
        file.write("""
        <!DOCTYPE html>
            <html lang="en">
            <head>
            <title>CodeDor</title>
            <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <div id="background">
                <div id="inputText">
        """)
        for row in table:
            file.write("<div class=\"inputLine\">")
            for token in row:
                if token.type == AtomType.BREAKLINE: continue
                file.write("<div class=\"")
                if token.type in (AtomType.OPEN_BRACKET, AtomType.CLOSE_BRACKET): file.write("brackets")
                else: file.write(token.type.value)
                file.write("\">")
                file.write(token.value)
                if token.type == AtomType.COMMENT: file.write(token.text)
                file.write("</div>")
            file.write("</div>")
            file.write("\n")

        file.write("""
                </div>
                </div>
            </body>
        </html>
        """)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as file:
            tokens_table = Scan(file)
            ColorHtml(tokens_table)