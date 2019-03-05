from stack_92 import Stack
from math import sqrt

def calculator(line):
   
   def plus(a,b):
      return a + b

   def minus(a,b):
      return a - b

   def multiply(a,b):
      return a * b

   def divide(a,b):
      return a / b

   def power(a,b):
      return a ** b

   def negate(a):
      return -a

   bin_ops = {
      "+": plus,
      "-": minus,
      "*": multiply,
      "/": divide,
      "**": power,
   }
   
   un_ops = {
      "n": negate,
      "r": sqrt,
   }

   stack = []

   for ch in line.split(" "):
      try:
         stack.append(float(ch))
      except ValueError:
         if ch in bin_ops and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            stack.append(bin_ops[ch](a,b))
         elif ch in un_ops and len(stack) >= 1:
            a = stack.pop()
            stack.append(un_ops[ch](a))
         else:
            raise IndexError

   if len(stack) == 1:
      return stack[0]
   else:
      raise IndexError