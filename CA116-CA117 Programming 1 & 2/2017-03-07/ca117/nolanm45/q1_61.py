import sys

def main():
   s=sys.argv[1]
   ls=list(s)
   for i in range(1,len(s),2):
       ls[i-1],ls[i]=ls[i],ls[i-1] 
   print("".join(ls))



if __name__=="__main__":
     main()
