import os
files = os.listdir(".")         
c="#!/usr/bin/env python"

i = 0
while i < len(files):
  with open(files[i],"r") as f:
     b=f.readline().strip()
     if len(b) > 0:
        if (files[i][-3:] == ".py" or b==c):      
           print files[i]
  i = i + 1
