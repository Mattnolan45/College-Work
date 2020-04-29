import sys

with open(sys.argv[1],"r") as f:
     lines=f.readlines()
try:
   name=" "
   highest=0
   for line in lines:
       line=line.strip().split()
       if int(line[0])>int(highest):
          highest=line[0]
          name=" ".join(line[1:])  
   print("Best student: {}".format(name))
   print("Best mark: {}".format(highest))

except ValueError:
    print("The file {} could not be opened.".format(sys.argv[1]))

