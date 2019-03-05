import sys

def contains(chars,s):
    for c in chars:
        if c in s:
            s = s.replace(c,'',1)
        else:
            return False
    return True 

print(contains(sys.argv[1],sys.argv[2]))
