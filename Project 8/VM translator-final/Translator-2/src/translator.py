import sys, Parser, os


def bootstrap():
    comment = "// BOOTSTRAP"
    asm = " ".join((" @{}".format(256), "D=A", "@SP", "M=D ")) 
    return "".join((comment, asm.replace(" ", "\n"), Parser.parser("call Sys.init 0", "Sys.vm")))

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
    owd = os.getcwd()
    path = os.path.abspath(sys.argv[1])

    if os.path.isfile(path) and sys.argv[1].endswith(".vm"):
        main(True)

    elif os.path.isdir(path):
        os.chdir(path)
        f = os.listdir('.')
        if f:
            k = 0
            for file in f:
                if file.endswith(".vm"):
                    k = 1
                    break

            if k == 1:
                os.chdir(owd)
                main(False, True)
            else:
                os.chdir(owd)
                main(False, False)  
    else:
        print("Error: {} is not a valid file/directory".format(sys.argv[1]))