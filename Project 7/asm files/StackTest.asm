// push constant 17

@17
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 17

@17
D=A
@SP
AM=M+1
A=A-1
M=D

// eq

@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.0
D;JEQ
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

// push constant 17

@17
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 16

@16
D=A
@SP
AM=M+1
A=A-1
M=D

// eq

@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.1
D;JEQ
@SP
M=M+1
A=M-1
M=0
@FALSE.1
0;JMP
(TRUE.1)
@SP
M=M+1
A=M-1
M=-1
(FALSE.1)

// push constant 16

@16
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 17

@17
D=A
@SP
AM=M+1
A=A-1
M=D

// eq

@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.2
D;JEQ
@SP
M=M+1
A=M-1
M=0
@FALSE.2
0;JMP
(TRUE.2)
@SP
M=M+1
A=M-1
M=-1
(FALSE.2)

// push constant 892

@892
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 891

@891
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
@TRUE.3
D;JLT
@SP
M=M+1
A=M-1
M=0
@FALSE.3
0;JMP
(TRUE.3)
@SP
M=M+1
A=M-1
M=-1
(FALSE.3)

// push constant 891

@891
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 892

@892
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
@TRUE.4
D;JLT
@SP
M=M+1
A=M-1
M=0
@FALSE.4
0;JMP
(TRUE.4)
@SP
M=M+1
A=M-1
M=-1
(FALSE.4)

// push constant 891

@891
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 891

@891
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
@TRUE.5
D;JLT
@SP
M=M+1
A=M-1
M=0
@FALSE.5
0;JMP
(TRUE.5)
@SP
M=M+1
A=M-1
M=-1
(FALSE.5)

// push constant 32767

@32767
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 32766

@32766
D=A
@SP
AM=M+1
A=A-1
M=D

// gt

@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.6
D;JGT
@SP
M=M+1
A=M-1
M=0
@FALSE.6
0;JMP
(TRUE.6)
@SP
M=M+1
A=M-1
M=-1
(FALSE.6)

// push constant 32766

@32766
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 32767

@32767
D=A
@SP
AM=M+1
A=A-1
M=D

// gt

@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.7
D;JGT
@SP
M=M+1
A=M-1
M=0
@FALSE.7
0;JMP
(TRUE.7)
@SP
M=M+1
A=M-1
M=-1
(FALSE.7)

// push constant 32766

@32766
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 32766

@32766
D=A
@SP
AM=M+1
A=A-1
M=D

// gt

@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@TRUE.8
D;JGT
@SP
M=M+1
A=M-1
M=0
@FALSE.8
0;JMP
(TRUE.8)
@SP
M=M+1
A=M-1
M=-1
(FALSE.8)

// push constant 57

@57
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 31

@31
D=A
@SP
AM=M+1
A=A-1
M=D

// push constant 53

@53
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

// push constant 112

@112
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

// neg

@SP
A=M-1
M=-M

// and

@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
D=D&M
@SP
A=M-1
M=D

// push constant 82

@82
D=A
@SP
AM=M+1
A=A-1
M=D

// or

@SP
A=M-1
D=M
@SP
M=M-1
A=M-1
D=D|M
@SP
A=M-1
M=D

// not

@SP
A=M-1
M=!M

