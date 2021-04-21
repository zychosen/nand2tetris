
// function Sys.init 0
(Sys.init)
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

// push constant 4000
@4000
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop pointer 0
@THIS
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

// push constant 5000
@5000
D=A
@SP
AM=M+1
A=A-1
M=D 

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

// call Sys.main 0
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
@Sys.main
0;JMP
($ret.0)

// pop temp 1
@1
D=A
@5
D=A+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D
(LOOP)

// goto LOOP
@LOOP
0;JMP

// function Sys.main 5
(Sys.main)
@5
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

// push constant 4001
@4001
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop pointer 0
@THIS
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

// push constant 5001
@5001
D=A
@SP
AM=M+1
A=A-1
M=D 

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

// push constant 200
@200
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop local 1
@1
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

// push constant 40
@40
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop local 2
@2
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

// push constant 6
@6
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop local 3
@3
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

// push constant 123
@123
D=A
@SP
AM=M+1
A=A-1
M=D 

// call Sys.add12 1
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
@Sys.add12
0;JMP
($ret.1)

// pop temp 0
@0
D=A
@5
D=A+D
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D

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

// push local 1
@1
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

// push local 2
@2
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

// push local 3
@3
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

// push local 4
@4
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

// add
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=D+M

// add
@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
MD=D+M

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

// function Sys.add12 0
(Sys.add12)
@0
D=A
@R13
M=D
@SKIP.2
D;JEQ
(SETUP.2)
@SP
M=M+1
A=M-1
M=0
@R13
M=M-1
D=M
@SETUP.2
D;JNE
(SKIP.2)

// push constant 4002
@4002
D=A
@SP
AM=M+1
A=A-1
M=D 

// pop pointer 0
@THIS
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

// push constant 5002
@5002
D=A
@SP
AM=M+1
A=A-1
M=D 

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

// push constant 12
@12
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
