class Point(object):
   def __init__(self, x, y):     
      self.x = x     
      self.y = y  
   def distance(self, other):       
      return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5 

class Shape(object):    
   def __init__(self, points):      
      self.points = points

   def sides(self):     
      a = []      
      i = 1       
      while i < len(self.points):         
         a.append(self.points[i].distance(self.points[i - 1]))          
         i += 1 
      a.append(self.points[0].distance(self.points[-1]))       
      return a 

   def perimeter(self):       
      return sum(self.sides()) 

class Triangle(Shape):
   def area(self):      
      sides = self.sides()       
      n = (sum(sides)) / 2       
      return (n * (n - sides[0]) * (n - sides[1]) * (n - sides[2])) ** 0.5 
                  
class Square(Shape):    
   def area(self):      
      sides = self.sides()       
      return(sides[0] * sides[1])