import re
import Handler
out_label_num = 0
asm = ""
labels = {}
label_count = 0


def save_labels(file):
    global label_count
    for line in file:
        if (line.strip()).startswith("//") or not line.strip():
            continue
        else:
            isLabel = re.search("label", line)
            label_count += 1
            if isLabel:
                label_ = line.split()
                labels[label_[1]] = str(label_count)


def parser(line, fileName):
    global label_num, out_label_num
    hasComment = re.search("//", line)
    if hasComment:
        line = line.split("//", 1)[0]
    line = line.split()

    n = len(line)
    command = str(line[0])
    commandType = Handler.lookUPCommand(command)
    if commandType == "0":
        asm = "command doesn't exist"

    elif commandType == "1":
        asm = Handler.arithmetic_logicalHandler(command, out_label_num)
        if command == "eq" or command == "gt" or command == "lt":
            out_label_num += 1

    elif commandType == "2" and n > 1:
        asm = Handler.pushpopHandler(command, line[1], line[2], fileName)

    elif commandType == "3":
        asm = Handler.labelHandler(line[1])

    elif commandType == "4" and n > 1:
        asm = Handler.ifgotoHandler(command, line[1], labels)

    elif commandType == "5" and n > 1:
        asm = Handler.functionHandler(line[1], line[2])

    elif commandType == "6" and n > 1:
        asm = Handler.callHandler(line[1], line[2])

    elif commandType == "7" and n == 1:
        asm = Handler.returnHandler()

    else:
        asm = "error"

    return asm
