
// push argument 1
@1
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

// pop pointer 1
@THAT
D=A
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

// push constant 0
@0
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop that 0
@0
D=A
@THAT
D=M+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

// push constant 1
@1
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop that 1
@1
D=A
@THAT
D=M+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

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

// pop argument 0
@0
D=A
@ARG
D=M+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D
(MAIN_LOOP_START)

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

// if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE

// goto END_PROGRAM
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)

// push that 0
@0
D=A
@THAT
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push that 1
@1
D=A
@THAT
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=D+M

// pop that 2
@2
D=A
@THAT
D=M+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

// push pointer 1
@THAT
D=A
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

// add
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=D+M

// pop pointer 1
@THAT
D=A
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

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

// pop argument 0
@0
D=A
@ARG
D=M+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)
