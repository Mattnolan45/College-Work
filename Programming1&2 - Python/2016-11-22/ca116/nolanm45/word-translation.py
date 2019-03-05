import sys
b={}



with open("translation.txt","r") as f:
     a=f.readlines() 
     i=0
     while i < len(a):
        a[i]=a[i].split(" ")
        b[a[i][0]]=a[i][1].strip()
        i+=1
     
lines=sys.stdin.readlines()
j=0
while j<len(lines):
     print b[lines[j].strip()]
     j+=1
       
   
    
