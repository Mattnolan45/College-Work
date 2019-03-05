i=0
tmp= input()
j=tmp
n=""

while n!=0:
    n=input()
    if n==j:
       print "equal"
       j=n
    elif n>j:
       print "higher"
       j=n
    elif n<j and n!=0:
       print "lower"
       j=n
    
 

