total_neg=0
total_pos=0
i=0

while i<5:
    n=input()
    if n<0:
       total_neg += n
    elif n>0:
       total_pos += n


    i=i+1
 
print total_neg,total_pos
    
