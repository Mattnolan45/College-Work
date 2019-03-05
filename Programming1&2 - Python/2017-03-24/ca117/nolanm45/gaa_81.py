class Score(object):
    
      def __init__(self,goals=0,points=0):
          self.goals=goals
          self.points=points
          self.score= 3*goals + points

      def __str__(self):
          return "{} goal(s) and {} point(s)".format(self.goals, self.points)         

      def __eq__(self,other):
          return (self.score) == (other.score)
     
      def __gt__(self,other):
          return (self.score) > (other.score)

      def __ge__(self,other):
          return (self.score) >= (other.score)
      
      def __add__(self,other):
          return (self.goals+other.goals, self.points+other.points).__str__()
   
      def __sub__(self,other):
          return self.score-other.score

      def __iadd__(self,other):
          z=self.score +other.score 
          return self
 
    
      def __isub__(self,other):
          z=self.score - other.score
          return self	
      
