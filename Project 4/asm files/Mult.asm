// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// @value sets A=value and selects RAM[A] (means M=RAM[A])
// another form of instructions: dest=comp;jump

// Set output register to zero
@R2
M=0

// Load value in R0 to determine how many times to loop
@R0
D=M

// Copy R0 value to temp
@temp
M=D

(LOOP)
	// Load temp register value
	@temp
	D=M

	// Check if temp value is zero and if so, jump to end 
	@END
	D;JLE

	// Load previous R2 result
	@R2
    D=M

    // Add previous result to R1 value
	@R1
	D=D+M

	// Write the new result back to R2
	@R2
	M=D

	// Decrement temp register
	@temp
	M=M-1

	// Loop while value at that mem location is zero
	@LOOP
	0;JMP

	// Infinite loop 
(END)
	@END
	0;JMP
