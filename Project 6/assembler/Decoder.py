import allocate
# Function to decode parsed instruction into it's binary equivalents 
def decoder(field1, field2, field3, labels):
	binString = ""

	if field1.isdigit() and field2 == "" and field3 == "":
		binString = toBinary(field1)

	elif (field2.isalnum() and field3.isalpha()) or (field1.isalpha() and field2 != "" and field3 == ""):
		s = lookUP(field1, field2, field3)
		binString = "111" + s

	else:
		try:
			s = lookUPsymbol(field1)
		except KeyError:
			if field1 in labels:
				binString = toBinary(labels[field1])
			else:
				binString = toBinary(allocate.variable(field1))
		except:
			binString = "some other error"
		else:
			binString = s
	return binString


# Convert a string value into binary with zero padding
def toBinary(x):
	if isinstance(x, str):
		intVal = (int)(x)
	else:
		intVal = x
	inbin = "{0:b}".format(intVal)
	inbin = inbin.zfill(16)
	return inbin

# LOOKUP tables

# JUMP look up table
def lookUPj(jump):
	table = { "":   "000",
			 "JGT": "001",
			 "JEQ": "010",
			 "JGE":	"011",
			 "JLT": "100",
			 "JNE":	"101",
			 "JLE":	"110",
			 "JMP": "111"}	
	return table[jump]

# COMP look up table
def lookUPc(comp):
	table = {"0"   : "0101010",
			 "1"   : "0111111",
			 "-1"  : "0111010",
			 "D"   : "0001100",
			 "A"   : "0110000",
			 "!D"  : "0001101",
			 "!A"  : "0110001",
			 "-D"  : "0001111",
			 "-A"  : "0110011",
			 "D+1" : "0011111",  
			 "A+1" : "0110111",
			 "D-1" : "0001110",
			 "A-1" : "0110010",
			 "D+A" : "0000010",
			 "D-A" : "0010011",
			 "A-D" : "0000111",
			 "D&A" : "0000000",
			 "D|A" : "0010101",
			 "M"   : "1110000",
			 "!M"  : "1110001",
			 "-M"  : "1110011",
			 "M+1" : "1110111",
			 "M-1" : "1110010",
			 "D+M" : "1000010",
			 "D-M" : "1010011",
			 "M-D" : "1000111",
			 "D&M" : "1000000",
			 "D|M" : "1010101",}

	return table[comp]

# DEST look up table
def lookUPd(dest):
	table = { "":   "000",
			 "M"  : "001",
			 "D"  : "010",
			 "MD" :	"011",
			 "A"  : "100",
			 "AM" :	"101",
			 "AD" :	"110",
			 "AMD": "111"}	
	return table[dest]

# Symbol look up table
def lookUPsymbol(symbol):

	table = {"R0"     : "0000000000000000",
	         "R1"     : "0000000000000001",
	         "R2"     : "0000000000000010",
	         "R3"     : "0000000000000011",
	         "R4"     : "0000000000000100",
	         "R5"     : "0000000000000101",
	         "R6"     : "0000000000000110",
	         "R7"     : "0000000000000111",
	         "R8"     : "0000000000001000",
	         "R9"     : "0000000000001001",
	         "R10"    : "0000000000001010",
	         "R11"    : "0000000000001011",
	         "R12"    : "0000000000001100",
	         "R13"    : "0000000000001101",
	         "R14"    : "0000000000001110",
	         "R15"    : "0000000000001111",
	         "SCREEN" : "0100000000000000",
	         "KBD"    : "0110000000000000",
	         "SP"     : "0000000000000000",
	         "LCL"    : "0000000000000001",
	         "ARG"    : "0000000000000010",
	         "THIS"   : "0000000000000011",
	         "THAT"   : "0000000000000100"}

	return table[symbol]

# Function to return correct sequence of binary strings
def lookUP(dest, comp, jump):
	dest = lookUPd(dest)
	comp = lookUPc(comp)
	jump = lookUPj(jump)

	return comp+dest+jump
