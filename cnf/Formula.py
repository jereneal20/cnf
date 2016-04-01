class Formula:
	operator = ""
	left = ""
	right = ""


	def __init__(self, tokens):
		if tokens is None:
			return
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
		else:
			return string + self.left