.data
MAX: .word 25
NUM: .word 4
.text

start: ld r1,NUM(r0)
loop: andi r3,r1,1
beqz r3,even
nop

odd: daddi r2,r0,2
dmul r1,r1,r2
sd r1, NUM(r0)
j after
nop

even: daddi r1,r1,-1
sd r1, NUM(r0)

after: ld r4,MAX(r0)
slt r3,r1,r4
bnez r3,loop
nop
halt