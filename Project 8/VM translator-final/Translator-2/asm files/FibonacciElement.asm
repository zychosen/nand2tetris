// BOOTSTRAP
@256
D=A
@SP
M=D

// call Sys.init 0
@$ret.0
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
($ret.0)

// function Main.fibonacci 0
(Main.fibonacci)
@0
D=A
@R13
M=D
@SKIP.0
D;JEQ
(SETUP.0)
@SP
M=M+1
A=M-1
M=0
@R13
M=M-1
D=M
@SETUP.0
D;JNE
(SKIP.0)

// push argument 0
@0
D=A
@ARG
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
D=A
@SP
AM=M+1
A=A-1
M=D 

// lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.0
D;JLT
@SP
M=M+1
A=M-1
M=0
@FALSE.0
0;JMP
(TRUE.0)
@SP
M=M+1
A=M-1
M=-1
(FALSE.0)

// if-goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE

// goto IF_FALSE
@IF_FALSE
0;JMP
(IF_TRUE)

// push argument 0
@0
D=A
@ARG
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// return
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=M+1
@ARG
D=M+1
@SP
M=D
@1
D=A
@R13
A=M-D
D=M
@THAT
M=D
@2
D=A
@R13
A=M-D
D=M
@THIS
M=D
@3
D=A
@R13
A=M-D
D=M
@ARG
M=D
@4
D=A
@R13
A=M-D
D=M
@LCL
M=D
@R14
A=M
0;JMP
(IF_FALSE)

// push argument 0
@0
D=A
@ARG
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
D=A
@SP
AM=M+1
A=A-1
M=D 

// sub
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=M-D

// call Main.fibonacci 1
@$ret.1
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
($ret.1)

// push argument 0
@0
D=A
@ARG
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
D=A
@SP
AM=M+1
A=A-1
M=D 

// sub
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=M-D

// call Main.fibonacci 1
@$ret.2
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
($ret.2)

// add
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=D+M

// return
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
D=M+1
@ARG
D=M+1
@SP
M=D
@1
D=A
@R13
A=M-D
D=M
@THAT
M=D
@2
D=A
@R13
A=M-D
D=M
@THIS
M=D
@3
D=A
@R13
A=M-D
D=M
@ARG
M=D
@4
D=A
@R13
A=M-D
D=M
@LCL
M=D
@R14
A=M
0;JMP

// function Sys.init 0
(Sys.init)
@0
D=A
@R13
M=D
@SKIP.1
D;JEQ
(SETUP.1)
@SP
M=M+1
A=M-1
M=0
@R13
M=M-1
D=M
@SETUP.1
D;JNE
(SKIP.1)

// push constant 4
@4
D=A
@SP
AM=M+1
A=A-1
M=D 

// call Main.fibonacci 1
@$ret.3
D=A
@SP
M=M+1
A=M-1
M=D
@LCL
D=M
@SP
M=M+1
A=M-1
M=D
@ARG
D=M
@SP
M=M+1
A=M-1
M=D
@THIS
D=M
@SP
M=M+1
A=M-1
M=D
@THAT
D=M
@SP
M=M+1
A=M-1
M=D
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
($ret.3)
(WHILE)

// goto WHILE
@WHILE
0;JMP
