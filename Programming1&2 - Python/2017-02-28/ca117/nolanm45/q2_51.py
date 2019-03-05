import sys

def main():
	for word in sys.stdin:
		word=word.strip()
		s=""
		for w in word.lower().strip() :
			if w in set("evil"):
				s+=w
		if s=="evil":
			print(word)

if __name__=="__main__":
	main()