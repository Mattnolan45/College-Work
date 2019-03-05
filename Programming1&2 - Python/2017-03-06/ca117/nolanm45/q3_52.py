import sys

def build_dictionary(filename):
    d={}
    with open(filename,"r") as f:
          for line in f:
                 line=line.split()
                 d[line[0]]=line[1]
    return(d) 


def extract_range(d,low,high):
     c={}
     for (key,item) in d.items():
          if int(item)>=low and int(item)<=high:
                c[key]=item
     
     return(c)
