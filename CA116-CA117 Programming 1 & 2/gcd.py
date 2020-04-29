a=int(input())
b=int(input())


while b!=0:
    
    tmp=b
    b=a%b
    a=tmp
    print(a)
    print(b)