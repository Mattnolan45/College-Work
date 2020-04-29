import sys
import re


lines=sys.stdin.read()

print(re.findall(r"\b\d{1,2}[/]\d{1,2}[/]\d{2}\b",lines))
    
