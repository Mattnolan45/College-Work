import sys
import string


def main():
    for line in sys.stdin:
        line=line.strip().split()
        for word in line:
             name=""
             if "@" in word:
                word=word.strip().split(".")
                word=" ".join(word).split("@")
                name=word[0].split()
                print(name[0].capitalize()+" "+name[1].capitalize())
                  
           

if __name__=="__main__":
     main()
