import sys
import Handler

def main():
	# Command line arguments for input and output files
	fileObject = open(sys.argv[1], 'r')
	saveObject = open(sys.argv[2], 'w')

	labels = Handler.save_labels(fileObject)  # Obtaining list of labels in asm file
	fileObject.seek(0)    # reset file object read pointer
	Handler.handle(fileObject, saveObject, labels)

	# Closing file objects
	fileObject.close()
	saveObject.close()

main() # Calling main function
