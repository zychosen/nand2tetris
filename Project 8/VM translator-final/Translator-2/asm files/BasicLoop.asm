
// push constant 0
@0
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop local 0
@0
D=A
@LCL
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
(LOOP_START)

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

// push local 0
@0
D=A
@LCL
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

// pop local 0
@0
D=A
@LCL
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

// if-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE

// push local 0
@0
D=A
@LCL
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
