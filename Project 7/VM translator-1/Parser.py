import re
import Handler
label_num = 0
asm = ""

def parser(line, fileName):
	global label_num
	hasComment = re.search("//", line)
	if hasComment:
		line = line.split("//", 1)[0]
	line = line.split()

	n = len(line)
	command = str(line[0])	
	commandType = Handler.lookUPCommand(command)
	if commandType == "1":
		asm = Handler.arithmetic_logicalHandler(command, label_num)
		if command == "eq" or command == "gt" or command == "lt":
			label_num += 1

	elif commandType == "2" and n > 1:
		asm = Handler.pushpopHandler(command, line[1], line[2], fileName)
	else:
		asm = "error"

	return asm

