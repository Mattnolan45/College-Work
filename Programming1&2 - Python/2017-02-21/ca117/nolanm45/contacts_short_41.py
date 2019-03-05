import sys
p={}



with open("contacts_short.txt","r") as contacts:
    for line in contacts:
        line=line.strip().split()
        p[line[0]]=line[1]
     


names=sys.stdin.readlines()
for name in names:
    name=name.strip() 
    print("Name: {}".format(name))
    try:
          
          
          print("Phone: {}".format(p[name]))
    except:
       
          print("No such contact")
