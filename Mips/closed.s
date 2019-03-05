.data

N: .word 100

.text
main:
	daddi r3,r0,2
	ld r1,N(r1)
	daddi r2,r1,1
    dmul r2,r2,r1
    ddiv r3,r2,r3