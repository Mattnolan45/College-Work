line=raw_input()


while line!= "end":
	i=0
	while i<len(line) and line[i]==" ":
		i+=1
	print line[i:]
    line=raw_input()