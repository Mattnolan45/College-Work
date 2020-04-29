import sys

def build_dictionary(filename):
    with open(filename,"r") as f:
    	return({k:v for line in f for k,v in [line.split()] })


def main():
	d=build_dictionary(sys.argv[1])
	s=""
	best=0
	for word in sys.stdin:
		total=0
		t=sys.argv[2]
		for w in word:
			if w in t:   
				total+=int(d[w])
				t=t.replace(w,"",1)
				if total>best:
					s=word 
					best=total
	print("{}: {}".format(s.strip(),best))  
         
 
if __name__=="__main__":
	main()    	