#!/usr/bin/python
import os, sys
from collections import deque

from Formula import Formula
import ConvertToCNF as CNF

varDictionary = {}
sampleInput = "> & - p q & p > r q"
sampleInput2 = "- = - a1 b2"


def getMiniSATString(infixForm):
    minisatStr = "c convert to CNF\np cnf " + str(len(varDictionary))
    minisatContent = ""
    iterNum = 0
    for token in infixForm.split():
        if token in varDictionary:
            minisatContent += str(varDictionary[token]) + " "
        if token == "&":
            minisatContent += "0\n"
            iterNum += 1
        if token == "-":
            minisatContent += "-"
    minisatContent += "0"
    minisatStr += " " + str(iterNum) + "\n" + minisatContent
    return minisatStr

def main(argv):
    print(sampleInput)

    originalFormula = Formula(deque(sampleInput.split()))
    print(originalFormula.formulaAsString())

    conjNormForm = CNF.convertToCNF(originalFormula)
    print("ConjNorm: " + conjNormForm.formulaAsString())

    infix = conjNormForm.formulaAsInfixString()
    print ("Infix "+infix)


    iterNum = 1
    for token in conjNormForm.formulaAsString().split():
        if token == "&" or token == "|" or token == "-":
            continue
        elif token not in varDictionary:
            varDictionary[token] = iterNum
            iterNum += 1
        else:
            pass

    print(getMiniSATString(infix))


    for a in varDictionary:
        print(a)

    # implFreeFormula = CNF.implicationFree(CNF.equivalanceFree(originalFormula))
    # print("ImplFree: "+ implFreeFormula.formulaAsString())
	#
    # negFreeForm = CNF.negationNormalForm(implFreeFormula)
    # print("NegFree:  "+ negFreeForm.formulaAsString())
	#
    # conjNorm = CNF.conjunctiveNormalForm(negFreeForm)
    # print("ConjNorm: " + conjNorm.formulaAsString())


if __name__ == "__main__":
    main(sys.argv[1:])