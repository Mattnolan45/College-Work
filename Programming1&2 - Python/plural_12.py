import sys
lines=sys.stdin.readlines()


endings=["ch","sh","x","s","z"]
vowels=["a","e","i","o","u"]
p=""

for word in lines:
	word=word.strip()
	

	if word.endswith("y")==True and word[-2] not in vowels :
		p=word[:-1]+"ies"
	elif word.endswith("f")==True:
		p=word[:-1]+"ves"
	elif word.endswith("fe")==True:
		p=word[:-2]+"ves"
	elif word.endswith("o")==True:
		p=word+"es"
	else:
		p=word+"s"
	
	for w in endings:
		if word.endswith(w)== True:
			p=word+"es"
	print(p)