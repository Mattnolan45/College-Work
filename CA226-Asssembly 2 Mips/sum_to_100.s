.text
main:
    daddi r1,r0,0
	daddi r2,r0,1
	daddi r3,r0,101
loop:
	beq r2,r3,done
	dadd r1,r1,r2
	daddi r2,r2,1
	j loop
done:
	halt


