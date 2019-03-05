import sys
import string

def main():
    for line in sys


 
def main():
    for line in sys.stdin:
        line=line.strip().split()
        for word in line:
              if "@" in word:
                  word=word.strip(string.punctuation).split()
                  print(word[0].capitalize()+" "+word[1].capitalize())  
             
                  
            
 
 if __name__=="__main__":
     main()
