class Distance(object):

      YARDS_PER_MILE=1760
      
      def __init__(self,miles=0,yards=0):
          self.miles=miles
          self.yards=yards
    
      def total_yards(self):
          return self.miles*1760+self.yards
    
      @classmethod
      def from_yards(cls,s):
          miles,yards=divmod(s,1760)
          return cls(miles,yards)
 
      def __str__(self):
        return "{} mile(s) and {} yard(s)".format(self.miles,self.yards)

      def __eq__(self,other):
          return self.total_yards() == other.total_yards()
    
      def __gt__(self,other):
          return self.total_yards() > other.total_yards()

      def __ge__(self,other):
          return self.total_yards() >= other.total_yards()

      def __lt__(self,other):
          return self.total_yards() < other.total_yards()
 
      def __le__(self,other):
          return self.total_yards() <= other.total_yards()

