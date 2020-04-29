import sys
from math import sqrt


def quadratic_formula(a,b,c):
	try:
		r1=(-b+sqrt((b**2)-(4*a*c)))/(2*a)
		r2=(-b-sqrt((b**2)-(4*a*c)))/(2*a)
		return("r1 = {}, r2 ={}".format(r1,r2))
	except:
		return("None")

	


def main():	
    #print(quadratic_formula([int(a),int(b),int(c) for line in sys.stdin for a,b,c in [line.split()]]))
    print([a,b,c for line in sys.stdin for a,b,c in [line.strip().split()]])	
     	

if __name__=="__main__":
	main()