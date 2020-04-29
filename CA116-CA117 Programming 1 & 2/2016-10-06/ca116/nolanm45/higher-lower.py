i=0
tmp= input()
j=tmp

while i<5:
    n=input()
    if n==j:
       print "equal"
       j=n
    elif n>j:
       print "higher"
       j=n
    elif n<j :
       print "lower"
       j=n
    i=i+1
 

