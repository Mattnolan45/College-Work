a=[]

i=1
while i< len(a):
    v=a[i]
    p=i 
    while 0<p and a[p-1]> v:
       a[p]=a[p-1]
       p=p-1
    a[p]=v
    
    i+=1
        
