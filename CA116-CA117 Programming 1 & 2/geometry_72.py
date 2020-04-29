class Point(object):

      def __init__(self,x=0,y=0):
          self.x=x
          self.y=y

      def reflect(self):
          self.x=self.x*-1
          self.y=self.y*-1
          
      def distance(self,other):
          return(((other.x-self.x)**2+(other.y-self.y)**2)**0.5)
    
      def __str__(self):
          return "({:.1f}, {:.1f})".format(self.x,self.y)

class Segment(object):
      
      def __init__(self,p1=0,p2=0):
          self.p1=p1
          self.p2=p2

      def midpoint(self,other):
          return "({:.1f}, {:.1f})".format((self.p1+other.p1)/2,(self.p2 +other.p2)/2)
       
      def length(self):
          return(((other.p1-self.p1)**2+(other.p2-self.p2)**2)**0.5)

class Circle(object):
    
      def __init__(self,r,centre):
          self.r=r
          centre=r

      def overlap(self,other):
          return (self.x-other.x)**2+(self.y-other.y)**2<(self.r+other.r)**2

            
                 
           
