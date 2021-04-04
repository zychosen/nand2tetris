import re
import Parser
import Decoder

# Handler that iterates through each line, decodes and writes to save file
def handle(fileObj, saveFile, labels):
	for line in fileObj:
		x = line.split("//", 1)
		isComment = re.search("[//]", line)
		y = re.search("[()]", line)

		if x[0].strip():	             # if line isn't empty
			if x[0].endswith('\n'):
				f1,f2,f3 = Parser.parser(x[0])
				if f1 == f2 == f3 == "1":
					continue
				else:
					saveFile.write(Decoder.decoder(f1,f2,f3,labels))
					saveFile.write("\n")
					
			else:
				f1,f2,f3 = Parser.parser(x[0])
				if f1 == f2 == f3 == "1":
					continue
				else:
					saveFile.write(Decoder.decoder(f1,f2,f3,labels))
					saveFile.write("\n")

		else:
			continue

# Obtain labels ie: (XXX) in file
def save_labels(fileObj):
	labels = Parser.extract(fileObj)
	return labels