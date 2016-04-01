#!/usr/bin/python
import os, sys
from collections import deque
from Formula import Formula

sampleInput = "> & - p q & p > r q"
sampleInput2 = "- = - a1 b2"

def wrapNotFormula(formula):
    notFormula = Formula(None)
    notFormula.operator = "-"
    notFormula.left = formula
    return notFormula

def wrapBinFormula(operator,formula1,formula2):
    orFormula = Formula(None)
    orFormula.operator = operator
    orFormula.left = formula1
    orFormula.right = formula2
    return orFormula

def equivalanceFree(formula):
    if formula.operator == "=":
        leftFormula = wrapBinFormula(">", formula.left, formula.right)
        rightFormula = wrapBinFormula("<", formula.left, formula.right)
        return wrapBinFormula("&", leftFormula, rightFormula)
    elif formula.operator == "<" or formula.operator == ">" or \
            formula.operator == "|" or formula.operator == "&":
        leftFormula = equivalanceFree(formula.left)
        rightFormula = equivalanceFree(formula.right)
        return wrapBinFormula(formula.operator, leftFormula, rightFormula)
    elif formula.operator == "-":
        return wrapNotFormula(equivalanceFree(formula.left))
    else:
        return formula

def implicationFree(formula):
    if formula.operator == ">":
        leftFormula = wrapNotFormula(implicationFree(formula.left))
        rightFormula = implicationFree(formula.right)
        return wrapBinFormula("|", leftFormula, rightFormula)
    elif formula.operator == "<":
        leftFormula = implicationFree(formula.left)
        rightFormula = wrapNotFormula(implicationFree(formula.right))
        return wrapBinFormula("|", leftFormula, rightFormula)
    elif formula.operator == "-":
        return wrapNotFormula(implicationFree(formula.left))
    elif formula.operator == "&" or formula.operator == "|":
        leftFormula = implicationFree(formula.left)
        rightFormula = implicationFree(formula.right)
        return wrapBinFormula(formula.operator, leftFormula, rightFormula)
    elif formula.operator == "=":
        print("Invalid Operator = on Implication free")
        leftFormula = implicationFree(formula.left)
        rightFormula = implicationFree(formula.right)
        return wrapBinFormula(formula.operator, leftFormula, rightFormula)
    else:
        return formula

def negationNormalForm(formula):
    if formula.operator == "-" and formula.left.operator == "-":
        return negationNormalForm(formula.left.left)
    elif formula.operator == "&" or formula.operator == "|":
        leftFormula = negationNormalForm(formula.left)
        rightFormula = negationNormalForm(formula.right)
        return wrapBinFormula(formula.operator, leftFormula, rightFormula)
    elif formula.operator == "-" and formula.left.operator == "&":
        leftFormula = wrapNotFormula(formula.left.left)
        rightFormula = wrapNotFormula(formula.left.right)
        orFormula = wrapBinFormula("|", leftFormula, rightFormula)
        return negationNormalForm(orFormula)
    elif formula.operator == "-" and formula.left.operator == "|":
        leftFormula = wrapNotFormula(formula.left.left)
        rightFormula = wrapNotFormula(formula.left.right)
        andFormula = wrapBinFormula("&", leftFormula, rightFormula)
        return negationNormalForm(andFormula)
    else:
        return formula

def conjunctiveNormalForm(formula):
    if formula.operator == "&":
        leftFormula = conjunctiveNormalForm(formula.left)
        rightFormula = conjunctiveNormalForm(formula.right)
        return wrapBinFormula(formula.operator, leftFormula, rightFormula)
    elif formula.operator == "|":
        leftFormula = conjunctiveNormalForm(formula.left)
        rightFormula = conjunctiveNormalForm(formula.right)
        return distributeFormula(leftFormula, rightFormula)
    else:
        return formula

def distributeFormula(formula1,formula2):
    if formula1.operator == "&":
        leftFormula = distributeFormula(formula1.left,formula2)
        rightFormula = distributeFormula(formula1.right, formula2)
        return wrapBinFormula("&", leftFormula, rightFormula)
    elif formula2.operator == "&":
        leftFormula = distributeFormula(formula1, formula2.left)
        rightFormula = distributeFormula(formula1, formula2.right)
        return wrapBinFormula("&", leftFormula, rightFormula)
    else:
        return wrapBinFormula("|", formula1, formula2)


def main(argv):
    print(sampleInput)

    # Equivalance Free
    # Implication Free
    # Negation Normal Form
    # Conjunctive Normal Form

    originalFormula = Formula(deque(sampleInput.split()))
    print(originalFormula.formulaAsString())

    implFreeFormula = implicationFree(equivalanceFree(originalFormula))
    print("ImplFree: "+ implFreeFormula.formulaAsString())

    negFreeForm = negationNormalForm(implFreeFormula)
    print("NegFree:  "+negFreeForm.formulaAsString())

    conjNorm = conjunctiveNormalForm(negFreeForm)
    print("ConjNorm: " + conjNorm.formulaAsString())




if __name__ == "__main__":
    main(sys.argv[1:])