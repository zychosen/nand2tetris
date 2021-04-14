import sys
import Parser

def main():
	with open(sys.argv[1], 'r') as file, open(sys.argv[2], 'w') as save:
		fileName = sys.argv[1].split(".", 1)[0]
		for line in file:
			if (line.strip()).startswith("//") or not line.strip():
				continue
			else:
				translatedLine = Parser.parser(line, fileName)
				save.write(translatedLine)
				save.write("\n")

main()