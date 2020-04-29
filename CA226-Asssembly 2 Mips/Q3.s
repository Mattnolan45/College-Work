.data 
N: .word 11
CONTROL: .word 0x10000
DATA:   .word 0x10008

.text
main:
ld r20,CONTROL(r0)
ld r21,DATA(r0)

daddi r1,r0,2
daddi r2,r0,0
ld r4,N(r0)
loop:

slt r3,r1,r4 ; will set r3 to 1 if r1<r4 else sets it to 0
beqz r3,end 
nop
dadd r2,r2,r1
daddi r1,r1,2
j loop

end:

sd r2,0(r21)

daddi r2,r0,2
sd r2,0(r20)
halt