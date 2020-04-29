.data

N: .word 10

.text
main:
	daddi r1,r0,0
	daddi r2,r2,1
    ld r3,N(r0)
loop:
 	beq r2,r3,done
    dadd r1,r1,r2
    daddi r2,r2,1

done:
	halt
