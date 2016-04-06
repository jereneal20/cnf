from Formula import Formula
import subprocess
import time

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

	miniSATLog = open("log", "w")
	p = subprocess.Popen(['minisat', 'miniSAT.in', 'miniSAT.out'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	p.communicate()
	p.wait()


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


def getResultDictionary(f, varDictionary):
	f.readline()
	result = f.readline().split()

	dictionary2 = {}
	for iter in varDictionary:
		if str(varDictionary[iter]) in result:
			dictionary2[iter] = "1"
		else:
			dictionary2[iter] = "-1"
	return dictionary2
