def arithmetic_logicalHandler(command, label_num):
	commandComment = "// " + command + "\n" 
	asmTranslation = lookUParithmetic_logical(command, label_num).replace(" ", "\n")
	return commandComment + "\n" + asmTranslation

def pushpopHandler(command, segment, val, fileName):
	commandComment = "// " + command + " " + segment + " " + val + "\n"
	asmTranslation = lookUPsegment(segment, val, fileName)
	if command == "push":
		if segment != "constant":
			asmTranslation += "A=D " + "D=M " + "@SP " + "A=M " "M=D " + "@SP " + "M=M+1 "
			asmTranslation = asmTranslation.replace(" ", "\n")
		else:
			asmTranslation = asmTranslation.replace(" ", "\n")
	elif command == "pop":
		asmTranslation += "@R13 " + "M=D " + "@SP " + "M=M-1 " + "A=M " + "D=M " + "@R13 " + "A=M " + "M=D "
		asmTranslation = asmTranslation.replace(" ", "\n")

	else:
		asmTranslation = "null"
	return commandComment + "\n" + asmTranslation

def lookUParithmetic_logical(command, label_num):
	table = {"add" : "@SP " + "A=M-1 " + "D=M " + "@SP " + "M=M-1 " + "A=M-1 " + "MD=D+M ",
			 "sub" : "@SP " + "A=M-1 " + "D=M " + "@SP " + "M=M-1 " + "A=M-1 " + "MD=M-D ",
			 "neg" : "@SP " + "A=M-1 " + "M=-M ",
			 "eq"  : "@SP " + "AM=M-1 " + "D=M " + "@SP " + "AM=M-1 " + "D=M-D " + f"@TRUE.{{val}} ".format(val=label_num) + "D;JEQ " + "@SP " + "M=M+1 " + "A=M-1 " + "M=0 " + f"@FALSE.{{val}} ".format(val=label_num) + "0;JMP " + f"(TRUE.{{val}}) ".format(val=label_num) + "@SP " + "M=M+1 " + "A=M-1 " + "M=-1 " + f"(FALSE.{{val}}) ".format(val=label_num),
			 "gt"  : "@SP " + "AM=M-1 " + "D=M " + "@SP " + "AM=M-1 " + "D=M-D " + f"@TRUE.{{val}} ".format(val=label_num) + "D;JGT " + "@SP " + "M=M+1 " + "A=M-1 " + "M=0 " + f"@FALSE.{{val}} ".format(val=label_num) + "0;JMP " + f"(TRUE.{{val}}) ".format(val=label_num) + "@SP " + "M=M+1 " + "A=M-1 " + "M=-1 " + f"(FALSE.{{val}}) ".format(val=label_num),
			 "lt"  : "@SP " + "AM=M-1 " + "D=M " + "@SP " + "AM=M-1 " + "D=M-D " + f"@TRUE.{{val}} ".format(val=label_num) + "D;JLT " + "@SP " + "M=M+1 " + "A=M-1 " + "M=0 " + f"@FALSE.{{val}} ".format(val=label_num) + "0;JMP " + f"(TRUE.{{val}}) ".format(val=label_num) + "@SP " + "M=M+1 " + "A=M-1 " + "M=-1 " + f"(FALSE.{{val}}) ".format(val=label_num),
			 "and" : "@SP " + "A=M-1 " + "D=M " + "@SP " + "M=M-1 " + "A=M-1 " + "D=D&M " + "@SP " +"A=M-1 " + "M=D ",
			 "or"  : "@SP " + "A=M-1 " + "D=M " + "@SP " + "M=M-1 " + "A=M-1 " + "D=D|M " + "@SP " +"A=M-1 " + "M=D ",
			 "not" : "@SP " + "A=M-1 " + "M=!M "}

	return table[command]					  

def lookUPsegment(segment, value, name):
	thisORthat = ""
	if segment == "pointer":
		if value == "0":
			thisORthat = "THIS"
		else:
			thisORthat = "THAT"

	table = {"argument" : f"@{{addr}} ".format(addr=value) + "D=A " + "@ARG " + "D=M+D ",
	         "local"    : f"@{{addr}} ".format(addr=value) + "D=A " + "@LCL " + "D=M+D ", 
	         "this"     : f"@{{addr}} ".format(addr=value) + "D=A " + "@THIS " + "D=M+D ",
	         "that"     : f"@{{addr}} ".format(addr=value) + "D=A " + "@THAT " + "D=M+D ",
	         "static"   : f"@{{n}}.{{i}} ".format(n=name, i=value) + "D=A ",
	         "constant" : f"@{{val}} ".format(val=value) + "D=A " + "@SP " + "AM=M+1 " + "A=A-1 " + "M=D ",
	         "pointer"  : f"@{{this_that}} ".format(this_that=thisORthat) + "D=A ",
	         "temp"     : f"@{{addr}} ".format(addr=value) + "D=A " + "@5 " + "D=A+D "}

	return table[segment]

def lookUPCommand(command):
	AorL = ["add", "sub", "neg", "eq", "lt", "gt", "and", "or", "not"]
	pushorpop = ["push", "pop"]

	if command in AorL:
		return "1"
	else:
		return "2"