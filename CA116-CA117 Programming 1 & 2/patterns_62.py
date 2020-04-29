import re
import sys


def main():
	s=sys.stdin.read()
	print(re.findall(s,r"\d{1,2}[/]\d{1,2}/\d{2}"))
	print(re.findall(s,r"\d{1,2}-\d{1,2}-\d{2}"))
	print(re.findall(s,r"\d{1,2}[/-]\d{1,2}[/-]\d{2}"))
	print(re.findall(s,r"01[\s-]\d{7}"))
    print(re.findall(s,r"\w{1,}@\w{1,}"))


if __name__=="__main__":
	main()