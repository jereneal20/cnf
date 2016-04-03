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
	# if len(argv) >= 2:
	#     print ("Use \" \" to the propositional formula: Syntax Example: cnf \"> & - p q & p > r q\"")
	#     exit(0)
	# elif len(argv) == 0:
	#     print ("Input format error: Syntax Example: cnf \"> & - p q & p > r q\"")
	#     exit(0)

	print("Input: "+ sampleInput)
	originalFormula = Formula(deque(sampleInput.split()))

	conjNormForm = CNF.convertToCNF(originalFormula)
	print("CNF Form  : " + conjNormForm.formulaAsString())

	infix = conjNormForm.formulaAsInfixString()
	print ("Infix Form: "+infix)

	varDictionary = minisat.createVarDictionary(conjNormForm)
	miniSATStr = minisat.getMiniSATString(infix, varDictionary)
	print(minisat.getMiniSATResult(miniSATStr))

	f = open("miniSAT.out", 'r')
	f.readline()
	result = f.readline().split()
	intResult = []
	for iter in result:
		intIter = int(iter)
		if intIter != 0:
			intResult.append(intIter)
			pass


	dictionary2 = minisat.getResultDictionary(sampleInput,varDictionary)

	print(varDictionary)
	print(result)
	print(dictionary2)


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