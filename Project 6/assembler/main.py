import sys
import Handler

def main():

	with open(sys.argv[1], 'r') as fileObject, open(sys.argv[2], 'w') as saveObject:
		labels = Handler.save_labels(fileObject)
		fileObject.seek(0)   
		Handler.handle(fileObject, saveObject, labels)

main()
