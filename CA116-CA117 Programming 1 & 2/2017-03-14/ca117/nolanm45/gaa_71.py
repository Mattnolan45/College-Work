class Score(object):

      def __init__(self,goals=0,points=0):
            self.goals=goals
            self.points=points
            self.total=self.goals*3+self.points 
                    

      def greater_than(self,other):
          return(self.total > other.total)
  
      def less_than(self,other):
          return(self.total < other.total)

            
      def equal_to(self,other):
          return(self.total == other.total)
