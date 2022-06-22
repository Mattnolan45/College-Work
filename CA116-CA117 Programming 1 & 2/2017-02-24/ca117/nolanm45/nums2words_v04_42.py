import sys

d={
   "0":"zero",
   "1":"one",
   "2":"two",
   "3":"three",
   "4":"four",
   "5":"five",
   "6":"six",
   "7":"seven",
   "8":"eight",
   "9":"nine",
   "10":"ten",
   "11":"eleven",
   "12":"twelve",
   "13":"thirteen",
   "14":"fourteen",
   "15":"fifteen",
   "16":"sixteen",
   "17":"seventeen",
   "18":"eighteen",
   "19":"nineteen",  
  }

d2={
	"2":"twenty",
	"3":"thirthy",
	"4":"forty",
	"5":"fifty",
	"6":"sixty",
	"7":"seventy",
	"8":"eighty",
	"9":"ninty",
	"100":"one hundred",
}


a=[]
for n in sys.stdin.readlines():
	if n in d:
		a.append(d[n])
	else:
		a.append(d2[n[1]]+"-"+d[n[2]])

print(" ".join(a))