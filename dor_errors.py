class LexicalError(Exception):
    def __init__(self, leks:tuple[str,int]): #leks[0] - znak, leks[1] - liniam
        self.message = f'Nieprawidłowy znak \'{leks[0]}\' linia {leks[1]}'
    def __str__(self):
        return self.message

class BraketCountError(Exception):
    def __init__(self, braket_control:int, line:int):
        if braket_control > 0: side = "closing"
        else: side = "openning"
        message = f'There aren\'t enough {side} brackets in line number {line+1}'
        self.message = message
    def __str__(self):
        return self.message

class CloseBraketStackError(Exception):
    def __init__(self, braket:str, line:int):
        message = f'Wrong closing bracket gender (\'{braket}\' at line {line})'
        self.message = message
    def __str__(self):
        return self.message

class EndLineError(Exception):
    def __init__(self, action:str): #( + - / *
        message = f'Line can\'t be ended by {action}'
        self.message = message
    def __str__(self):
        return self.message

class StartLineError(Exception):
    def __init__(self, action:str): #) + - / *
        message = f'Line can\'t be started by {action}'
        self.message = message
    def __str__(self):
        return self.message

class OtherSynteaxError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message