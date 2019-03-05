import re

def phone(s):
    return re.findall(re.compile(r'\b(?:085|086|087)[-\s]\d{7}\b'))



def main():
    pass



if __name__=="__main__":
	main()