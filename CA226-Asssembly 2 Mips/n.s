.data 
Array1:	.word 1
		.word 2
		.word 3
		.word 4
		.word 5
C: .word 0x10000
D: .word 0x10000

.text
	main:
	ld r20,C(r0)
	ld r21,D(r0)
	
	daddi r1,r0,0
	ld r4, Array1(r1)
	daddi r2,r0,40
	daddi r3,r0,0

	loop:
	beq r1,r2,done
	dsll r5,r4,1
	dadd r5,r5,r4
	sd r5, Array1(r1)
	daddi r1,r1,8
	ld r4,Array1(r1)
	j loop
	nop

	done:
	beq r3,r2,end
	ld r6,Array1(r3)
	
	sd r6,0(r21)
	
	daddi r6,r0,2
	sd r6,0(r20)
	daddi r3,r3,8
	j done
	
	end:
	
	halt
