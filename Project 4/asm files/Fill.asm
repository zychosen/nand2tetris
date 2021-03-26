// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@KBD
M=0

(LOOP)
	
	@SCREEN
	D=A

	@addr
	M=D

	@8192
	D=A

	@n
	M=D

	@temp
	M=0

	@KBD
	D=M

	@LOOP1			// Jump to LOOP1 if keyboard input is blank (no input)
	D;JEQ

	@LOOP2			// Jump to LOOP2 if keyboard input is valid
	D;JNE

	@LOOP           // Infinite loop, listens to keyboard input and resets register and temp
	0;JMP           // addresses for rewrite

(LOOP1)	
	(ToZero)
		@KBD
		D=M       
		@LOOP           // If keyboard input is given, go to LOOP2
		D;JNE          

		@n
		D=M

		@ToZero        // If all registers are full, continue with same contents and check for
		D;JEQ          // keyboard input changes

		@n
		M=M-1

		@addr
		D=M

		@temp
		A=D+M          // Adding base address of screen memory map with temp register value 
		M=0

		@temp
		M=M+1
		
		@LOOP1		   // Loops infinitely if other conditions fail
		0;JMP
		
(LOOP2)
	(ToOne)
		@KBD
		D=M
		@LOOP
		D;JEQ            // If keyboard input is empty, go to LOOP1
		
		@n
		D=M

		@ToOne
		D;JEQ

		@n
		M=M-1

		@addr
		D=M

		@temp
		A=D+M
		M=-1

		@temp
		M=M+1
		
		@LOOP2
		0;JMP          // Loops infinitely if other conditions fail
