import sys, Parser, os


# Setup code to initialize stack pointer (SP) and call Sys.init
def bootstrap():
    asm = " ".join(("@{}".format(256), "D=A", "@SP", "M=D")) 
    return "".join((asm.replace(" ", "\n"), Parser.parser("call Sys.init 0", "Sys.vm")))

def main(isFile, hasFiles=False):
    if isFile:
        with open(sys.argv[1]) as file, open(sys.argv[2], 'w') as save:
            save.write(bootstrap())
            Parser.save_labels(file)
            file.seek(0)
            fileName = (file.name).split(".vm", 1)[0]
            for line in file:
                if (line.strip()).startswith("//") or not line.strip():
                    continue
                else:
                    translatedLine = Parser.parser(line, fileName)
                    save.write(translatedLine)
                
    else:
        if hasFiles:
            with os.scandir(sys.argv[1]) as directory, open(sys.argv[2], 'w') as save:
                fileList = [i for i in directory if i.name.endswith(".vm")]
                save.write(bootstrap())
                for f in fileList:
                    with open(f) as file:
                        Parser.save_labels(file)
                        file.seek(0)
                        fileName = (f.name).split(".vm", 1)[0]
                        for line in file:
                            if (line.strip()).startswith("//") or not line.strip():
                                continue
                            else:
                                translatedLine = Parser.parser(line, fileName)
                                save.write(translatedLine)
        else:
            print("Error: .vm files not found")

if __name__ == '__main__':
    owd = os.getcwd() # Get original working directory
    path = os.path.abspath(sys.argv[1]) # Create path of input file/directory

    if os.path.isfile(path) and sys.argv[1].endswith(".vm"): # check if the input is of the form filename.vm
        main(True)

    elif os.path.isdir(path):  #check if input is a directory
        os.chdir(path)
        f = os.listdir('.')
        if f:                 #check if files exist in input directory
            k = 0
            for file in f:
                if file.endswith(".vm"):
                    k = 1
                    break

            if k == 1:
                os.chdir(owd)    #switch to original working directory
                main(False, True)
            else:
                os.chdir(owd)
                main(False, False)  
    else:
        print("Error: {} is not a valid file/directory".format(sys.argv[1]))