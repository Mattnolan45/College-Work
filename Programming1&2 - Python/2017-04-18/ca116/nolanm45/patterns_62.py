import re
import sys

def main():
    lines=sys.stdin.read() 
    print(re.findall(r"\b\d{1,2}[/]\d{1,2}\d{2,4}\b",lines))



if __name__=="__main__":
   main()
