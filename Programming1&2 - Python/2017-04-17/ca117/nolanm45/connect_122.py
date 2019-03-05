import sys
line = []
n = int(sys.argv[1])

def row(line):
   count = 0
   for i in range(len(line)-(n-1)):
      for j in range(len(line[i])):
         k = 0
         while k < n:
            if line[i + k][j] != "x":
               break
            else:
               k += 1
         if k == n:
            count += 1
   return(count)

def column(line):
   count = 0
   for i in range(len(line)):
      for j in range(len(line[i])-(n-1)):
         k = 0
         while k < n:
            if line[i][j + k] != "x":
               break
            else:
               k += 1
         if k == n:
            count += 1
   return(count)

def diagonal(line):
   count = 0
   for i in range(n-1, len(line)):
      for j in range(len(line[i])-(n-1)):
         k = 0
         while k < n:
            if line[i - k][j + k] != "x":
               break
            else:
               k += 1
         if k == n:
            count += 1
   return(count)

def rev_diagonal(line):
   count = 0
   for i in range(n-1, len(line)):
      for j in range(len(line[i])-(n-1)):
         k = 0
         while k < n:
            if line[i - k][j - k] != "x":
               break
            else:
               k += 1
         if k == n:
            count += 1
   return(count)

def main():
   for s in sys.stdin:
      line.append(s.strip())
   total = row(line) + column(line) + diagonal(line) + rev_diagonal(line)
   print(total)

if __name__ == "__main__":
   main()