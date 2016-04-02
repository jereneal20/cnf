#!/usr/bin/python
import os, sys, subprocess
from collections import deque

from Formula import Formula
import ConvertToCNF as CNF

sampleInput = "> & - p q & p > r q"
sampleInput2 = "- = - a1 b2"
sampleInput3 = "= - a1 a1"

def createVarDictionary(cnfForm):
    varDictionary = {}
    iterNum = 1
    for token in cnfForm.formulaAsString().split():
        if token == "&" or token == "|" or token == "-":
            continue
        elif token not in varDictionary:
            varDictionary[token] = iterNum
            iterNum += 1
        else:
            pass
    return varDictionary

def getMiniSATString(infixForm, varDictionary):
    minisatStr = "c convert to CNF\np cnf " + str(len(varDictionary))
    minisatContent = ""
    iterNum = 1
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

def getMiniSATResult(miniSATStr):
    f = open("miniSAT.in", 'w')
    f.write(miniSATStr)
    f.close()

    miniSATLog = open("err.log", "w")
    subprocess.call(['minisat', 'miniSAT.in', 'miniSAT.out'], stdout=miniSATLog, stderr=miniSATLog)
    miniSATLog.close()

    f = open("miniSAT.out", 'r')
    result = f.readline()
    f.close()

    if result == "SAT\n":
        return "Not Valid"
    elif result == "UNSAT\n":
        return "Valid"
    else:
        return "Neither SAT nor UNSAT"



def main(argv):
    if len(argv) >= 2:
        print ("Use \" \" to the propositional formula: Syntax Example: cnf \"> & - p q & p > r q\"")
        exit(0)
    elif len(argv) == 0:
        print ("Input format error: Syntax Example: cnf \"> & - p q & p > r q\"")
        exit(0)

    print("Input: "+ argv[1])
    originalFormula = Formula(deque(argv[1].split()))

    conjNormForm = CNF.convertToCNF(originalFormula)
    print("CNF Form  : " + conjNormForm.formulaAsString())

    infix = conjNormForm.formulaAsInfixString()
    print ("Infix Form: "+infix)

    varDictionary = createVarDictionary(conjNormForm)
    miniSATStr = getMiniSATString(infix, varDictionary)
    print(getMiniSATResult(miniSATStr))


    # for a in varDictionary:
    #     print(a)

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