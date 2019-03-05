import re
import sys

def main():
    lines=sys.stdin.read() 
    print(re.findall(r"\b\d{1,2}[/]\d{1,2}[/]\d{2,4}\b",lines))
    print(re.findall(r"\b\d{1,2}[-]\d{1,2}[-]\d{2,4}\b",lines))
    print(re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",lines))
    print(re.findall(r"\b\d{2}[-\s]\d{7}\b",lines))
    print(re.findall(r"\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b",lines))
    print(re.findall(r"\b\d{1,2}\s[\w]\w{2}\s\d{2,4}\b",lines))



if __name__=="__main__":
   main()
