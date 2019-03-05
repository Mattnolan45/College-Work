a=input()
b=input()


while b!=0:
    
    tmp=b
    b=a%b
    a=tmp
print a
