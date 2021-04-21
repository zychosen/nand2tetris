return_count = 0
skip_count = 0
setup_count = 0


def arithmetic_logicalHandler(command, out_label_num):
    commandComment = " ".join(("//", command))
    asmTranslation = lookUParithmetic_logical(command, out_label_num).replace(" ", "\n")
    return "".join(("\n", commandComment, asmTranslation))


def pushpopHandler(command, segment, val, fileName):
    commandComment = " ".join(("//", command, segment, val))
    asmTranslation = lookUPsegment(segment, val, fileName)
    if command == "push":
        if segment != "constant":
            asmTranslation = " ".join((asmTranslation, "A=D", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1 "))
            asmTranslation = asmTranslation.replace(" ", "\n")
        else:
            asmTranslation = " ".join((asmTranslation.replace(" ", "\n"), "\n"))
    elif command == "pop":
        asmTranslation = " ".join((asmTranslation, "@R15", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R15", "A=M", "M=D "))
        asmTranslation = asmTranslation.replace(" ", "\n")

    else:
        asmTranslation = "null"
    return "".join(("\n", commandComment, asmTranslation))


def labelHandler(label):
    asmTranslation = ("({l}) ".format(l=label))
    return asmTranslation.replace(" ", "\n")


def ifgotoHandler(command, label, labels):
    commandComment = " ".join(("//", command, label))
    if label in labels:
        if command == "goto":
            asmTranslation = " ".join((" @{l}".format(l=label), "0;JMP "))
            return "".join(("\n", commandComment, asmTranslation.replace(" ", "\n")))
        else:
            asmTranslation = " ".join((" @SP", "AM=M-1", "D=M", "@{l}".format(l=label), "D;JNE "))
            return "".join(("\n", commandComment, asmTranslation.replace(" ", "\n")))


def functionHandler(name, num_vars):
    global skip_count, setup_count
    commandComment = " ".join(("//", "function", name, num_vars))
    asmTranslation = " ".join((" ({name})".format(name=name), "@{var}".format(var=int(num_vars)), "D=A", "@R13", "M=D",
                     "@SKIP.{}".format(skip_count), "D;JEQ", "(SETUP.{})".format(setup_count), "@SP", "M=M+1", "A=M-1", "M=0", "@R13", "M=M-1", "D=M",
                     "@SETUP.{}".format(setup_count), "D;JNE", "(SKIP.{}) ".format(skip_count)))

    skip_count += 1
    setup_count += 1
    return "".join(("\n", commandComment, asmTranslation.replace(" ", "\n")))


def callHandler(f_name, args):
    global return_count
    commandComment = " ".join(("//", "call", "{}".format(f_name), "{}".format(args))) 
    asmTranslation = " ".join((" @{return_label}".format(return_label="$ret.{val}".format(val=return_count)), "D=A", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@LCL", "D=M", "@SP", "M=M+1", "A=M-1", "M=D", "@ARG", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@THIS", "D=M", "@SP", "M=M+1", "A=M-1", "M=D", "@THAT", "D=M", "@SP", "M=M+1", "A=M-1", "M=D",
                     "@SP", "D=M", "@5", "D=D-A", "@{val}".format(val=args), "D=D-A", "@ARG", "M=D", "@SP", "D=M", "@LCL", "M=D", "@{name}".format(name=f_name), "0;JMP",
                     "({return_label}) ".format(return_label="$ret.{val}".format(val=return_count))))
    return_count += 1
    return "".join(("\n", commandComment, asmTranslation.replace(" ", "\n")))


def returnHandler():
    commandComment = " ".join(("//", "return"))
    asmTranslation = " ".join((" @LCL", "D=M", "@R13", "M=D", "@5", "A=D-A", "D=M", "@R14", "M=D",
                     "@SP", "AM=M-1", "D=M", "@ARG", "A=M", "M=D", "D=M+1", "@ARG", "D=M+1", "@SP", "M=D", "@1", "D=A", "@R13", "A=M-D", "D=M", "@THAT", "M=D",
                     "@2", "D=A", "@R13", "A=M-D", "D=M", "@THIS", "M=D", "@3", "D=A", "@R13", "A=M-D", "D=M", "@ARG", "M=D",
                     "@4", "D=A", "@R13","A=M-D", "D=M", "@LCL", "M=D", "@R14", "A=M", "0;JMP "))

    return "".join(("\n", commandComment, asmTranslation.replace(" ", "\n")))


def lookUParithmetic_logical(command, out_label_num):
    table = {"add": " ".join((" @SP", "A=M-1", "D=M", "@SP", "M=M-1", "A=M-1", "MD=D+M ")),
             "sub": " ".join((" @SP", "A=M-1", "D=M", "@SP", "M=M-1", "A=M-1", "MD=M-D ")),
             "neg": " ".join((" @SP", "A=M-1", "M=-M ")),
             "eq":  " ".join((" @SP", "AM=M-1", "D=M", "@SP", "AM=M-1", "D=M-D", f"@TRUE.{{val}}".format(val=out_label_num), "D;JEQ", "@SP", "M=M+1", "A=M-1", "M=0", f"@FALSE.{{val}}".format(val=out_label_num), "0;JMP", f"(TRUE.{{val}})".format(val=out_label_num), "@SP", "M=M+1", "A=M-1", "M=-1", f"(FALSE.{{val}}) ".format(val=out_label_num))),
             "gt":  " ".join((" @SP", "AM=M-1", "D=M", "@SP", "AM=M-1", "D=M-D", f"@TRUE.{{val}}".format(val=out_label_num), "D;JGT", "@SP", "M=M+1", "A=M-1", "M=0", f"@FALSE.{{val}}".format(val=out_label_num), "0;JMP", f"(TRUE.{{val}})".format(val=out_label_num), "@SP", "M=M+1", "A=M-1", "M=-1", f"(FALSE.{{val}}) ".format(val=out_label_num))),
             "lt":  " ".join((" @SP", "AM=M-1", "D=M", "@SP", "AM=M-1", "D=M-D", f"@TRUE.{{val}}".format(val=out_label_num), "D;JLT", "@SP", "M=M+1", "A=M-1", "M=0", f"@FALSE.{{val}}".format(val=out_label_num), "0;JMP", f"(TRUE.{{val}})".format(val=out_label_num), "@SP", "M=M+1", "A=M-1", "M=-1", f"(FALSE.{{val}}) ".format(val=out_label_num))),
             "and": " ".join((" @SP", "A=M-1", "D=M", "@SP", "M=M-1", "A=M-1", "D=D&M", "@SP", "A=M-1", "M=D ")),
             "or":  " ".join((" @SP", "A=M-1", "D=M", "@SP", "M=M-1", "A=M-1", "D=D|M", "@SP", "A=M-1", "M=D ")),
             "not": " ".join((" @SP", "A=M-1", "M=!M "))}

    return table[command]


def lookUPsegment(segment, value, name):
    thisORthat = ""
    if segment == "pointer":
        if value == "0":
            thisORthat = "THIS"
        else:
            thisORthat = "THAT"

    table = {"argument": " ".join((f" @{{addr}}".format(addr=value), "D=A", "@ARG", "D=M+D")),
             "local":    " ".join((f" @{{addr}}".format(addr=value), "D=A", "@LCL", "D=M+D")),
             "this":     " ".join((f" @{{addr}}".format(addr=value), "D=A", "@THIS", "D=M+D")),
             "that":     " ".join((f" @{{addr}}".format(addr=value), "D=A", "@THAT", "D=M+D")),
             "static":   " ".join((f" @{{n}}.{{i}}".format(n=name, i=value), "D=A")),
             "constant": " ".join((f" @{{val}}".format(val=value), "D=A", "@SP", "AM=M+1", "A=A-1", "M=D")),
             "pointer":  " ".join((f" @{{this_that}}".format(this_that=thisORthat), "D=A")),
             "temp":     " ".join((f" @{{addr}}".format(addr=value), "D=A", "@5", "D=A+D"))}

    return table[segment]


def lookUPCommand(command):
    AorL = ["add", "sub", "neg", "eq", "lt", "gt", "and", "or", "not"]
    pushorpop = ["push", "pop"]
    label = ["label"]
    ifgoto = ["goto", "if-goto"]
    function = ["function"]
    call = ["call"]
    Return = ["return"]

    if command in AorL:
        return "1"
    elif command in pushorpop:
        return "2"
    elif command in label:
        return "3"
    elif command in ifgoto:
        return "4"
    elif command in function:
        return "5"
    elif command in call:
        return "6"
    elif command in Return:
        return "7"
    else:
        return "0"
