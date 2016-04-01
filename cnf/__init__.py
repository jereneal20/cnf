#!/usr/bin/python
import os, sys
from collections import deque

sampleInput = "> & - p q & p > r q"

class Formula:
    operator = ""
    left = ""
    right = ""

    def __init__(self, tokens):
        token = tokens.popleft()
        if Formula.isBinaryToken(token):
            self.operator = token
            self.left = Formula(tokens)
            self.right = Formula(tokens)
        elif token == "-":
            self.operator = token
            self.left = Formula(tokens)
        else:
            self.left = token #Atomic
            # print("Invalid operator or syntax.\n")
            # exit(1)

    def isBinaryToken(token):
        if token == "&" or token == "|" or \
           token == ">" or token == "<" or token == "=":
            return True
        else:
            return False

    def formulaAsString(self):
        # Make formula string as polish notation
        string = ""
        if Formula.isBinaryToken(self.operator):
            return string+self.operator+" "+self.left.formulaAsString()+" "+self.right.formulaAsString()
        elif self.operator == "-":
            return string + self.operator + " " + self.left.formulaAsString()
            pass
        else:
            return string + self.left
            pass


def main(argv):
    print(sampleInput)

    originalFormula = Formula(deque(sampleInput.split()))

    print(originalFormula.formulaAsString())


if __name__ == "__main__":
    main(sys.argv[1:])
