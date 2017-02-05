#!/usr/bin/python
import os, sys, subprocess
from collections import deque

from Formula import Formula
import ConvertToCNF as CNF
import MiniSATCaller as minisat

sampleInput = "> & - p q & p > r q"
sampleInput2 = "- = - a1 b2"
sampleInput3 = "= - a1 a1"


def main(argv):
	if len(argv) >= 2:
		print ("Use \" \" to the propositional formula: Syntax Example: cnf \"> & - p q & p > r q\"")
		exit(0)
	elif len(argv) == 0:
		print ("Input format error: Syntax Example: cnf \"> & - p q & p > r q\"")
		exit(0)
	input = argv[0]

	# print("Input: "+ argv[0])
	originalFormula = Formula(deque(input.split()))

	conjNormForm = CNF.convertToCNF(originalFormula)
	print(conjNormForm.formulaAsString())
	# print("CNF Form  : " + conjNormForm.formulaAsString())

	infix = conjNormForm.formulaAsInfixString()
	print (infix)
	# print ("Infix Form: "+infix)

	varDictionary = minisat.createVarDictionary(conjNormForm)
	miniSATStr = minisat.getMiniSATString(infix, varDictionary)
	minisat.getMiniSATResult(miniSATStr)


	notForm = CNF.convertToCNF(CNF.wrapNotFormula(Formula(deque(input.split()))))
	infix2 = notForm.formulaAsInfixString()
	varDictionary2 = minisat.createVarDictionary(notForm)
	miniSATStr2 = minisat.getMiniSATString(infix2, varDictionary2)
	print(minisat.getMiniSATResult(miniSATStr2))

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