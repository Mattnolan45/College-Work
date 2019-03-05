import re

def phone(s):
    t=(re.compile(r'\b(?:085|086|087)[-\s]\d{7}\b'))
    return t.findall(s)



def main():
    pass



if __name__=="__main__":
	main()