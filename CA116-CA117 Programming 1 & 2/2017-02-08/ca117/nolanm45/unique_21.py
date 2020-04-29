import sys 
import string 


words=[]
for line in sys.stdin:
	for w in line.strip().lower().split():
		w=w.strip(string.punctuation)
		if w not in words:
			words.append(w)
print(len(words)-1)