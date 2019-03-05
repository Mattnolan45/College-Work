from stack_92 import Stack

def matcher(line):
    s=Stack()
    lefties="({["
    if len(line) %2 !=0:
       return False
    
    d={ "(":")" , "{":"}" , "[":"]" }
 
    for w in line:
        if w in lefties:
           s.push(w)
        elif d[s.top()] == w:
             s.pop()
    return s.is_empty()
