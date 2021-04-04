import re

label = ""
labels = {}

# Parser implementation for an instruction
def parser(instruction):
	instruction = re.sub(r'\s+', '', instruction)
	isA = re.search("@", instruction) 
	isLabel = re.search("[()]", instruction)
	noEQ = re.search("[=]", instruction)
	if isLabel:
		return "1", "1", "1"
	else:
		if isA == None:
			if noEQ == None:
				half = instruction.split(";", 1)
				dest = ""
				comp = half[0]
				jmp = half[1]
			else:
				half = instruction.split("=", 1)
				dest = half[0]
				jump = re.search(";", half[1]) 
				if jump == None:
					comp = half[1]
					jmp = ""
				else:
					x = re.split(";", half[1], 1)
					comp = x[0]
					jmp = x[1]

			return dest, comp, jmp

		else:
			inst_split = instruction.split("@", 1)
			loadVal = inst_split[1]
			return loadVal, "", ""

# Function to extract all labels 
def extract(fileObj, line_num=0):
	for line_ in fileObj:
		y = re.search("[()]", line_)
		isComment = (line_.strip()).startswith("//")
		hasComment = re.search("[//]", line_)
		isLabel = (line_.strip()).startswith("(")
		if y != None and isComment == False and hasComment == False or isLabel:
			label = line_[line_.find("(")+1:line_.find(")")]
			labels[label] = str(line_num)	
		if isLabel == False and isComment == False and line_.strip():
			line_num += 1

	line_num = 0
	return labels