import re

class format:
    def __init__(self, input):
        self.input = input

    def center(self):

        strlen = self.ret_strlen()
        size = 34 - (strlen/2)
        center = ""
        i = 0
        while i < size:
            center += " "
            i = i + 1

        self.input = center + self.input

    def ret_strlen(self):
        strip = re.compile(r"""
            \x1b     # literal ESC
            \[       # literal [
            [;\d]*   # zero or more digits or semicolons
            [A-Za-z] # a letter
        """, re.VERBOSE).sub
        temp = strip("", self.input)
        return len(temp)

    def ret(self):
        return self.input
