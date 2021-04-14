// push constant 7

@7
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 8

@8
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

