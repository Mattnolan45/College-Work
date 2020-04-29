import sys
import string

code = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def main():
   words = ""
   for w in sys.stdin:
      for l in w:
         words += l

   letters = ""
   for l in words:
      l = l.strip()
      l = l.strip(string.punctuation)
      letters += l

   dic = {}
   dic2 = {}
   for i in letters:
      dic[i] = letters.count(i)
   for (k,v) in dic.items():
      dic2[v] = k
   freq = dic2[max(dic2)]

   key = code.index(freq) - code.index("E")

   cipher = ""
   for c in words:
      for s in c:
         if s in code:
            cipher += code[(code.index(s) - key)]
         else:
            cipher += s

   sys.stdout.write(cipher)

if __name__ == "__main__":
   main()