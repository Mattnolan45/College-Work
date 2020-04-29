class Score(object):
    
      def __init__(self,goals=0,points=0):
          self.goals=goals
          self.points=points
    

      def __str__(self):
          return "{} goal(s) and {} point(s)".format(self.goals, self.points)         

      def __eq__(self,other):
          return self.g_to_p() == other.g_to_p()
     
      def __gt__(self,other):
          return self.g_to_p() > other.g_to_p()

      def __ge__(self,other):
          return self.g_to_p() >= other.g_to_p()
      
      def __add__(self,other):
          return Score(self.goals+other.goals, self.points+other.points)
   
      def __sub__(self,other):
          return Score(self.goals-other.goals, self.points-other.points)

      def __iadd__(self,other):
          z=self+other
          self.goals,self.points = z.goals,z.points
          return self
 
    
      def __isub__(self,other):
          z=self-other
          self.goals,self.points = z.goals,z.points
          return self	
          
 
      def g_to_p(self):
          return self.goals*3+self.points

      def __mul__(self,other):
          return Score(self.goals*other, self.points*other)

      def __rmul__(self,other):
          return Score(other*self.goals, other*self.points)

      def __imul__(self,other):
          z=self*other
          self.goals,self.points = z.goals,z.points
          return self
                    
