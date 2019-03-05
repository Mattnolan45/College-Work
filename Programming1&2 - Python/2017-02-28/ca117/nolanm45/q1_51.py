import sys

def main():
     word=list(sys.argv[1])
     i=0
     j=1
     if len(word)%2==0:
        while j<=len(word):
            tmp=word[i]
            word[i]=word[j]
            word[j]=tmp
            i+=2
            j+=2
     else:
         while j<=len(word)-1:
            tmp=word[i]
            word[i]=word[j]
            word[j]=tmp
            i+=2
            j+=2
     print("".join(word))        
        
 

if __name__ == "__main__":
     main()
