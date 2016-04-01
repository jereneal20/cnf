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
        if token == "&" or token == "|" or \
           token == ">" or token == "<" or token == "=":
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


def main(argv):
    print(sampleInput)

    originalFormula = Formula(deque(sampleInput.split()))


if __name__ == "__main__":
    main(sys.argv[1:])
