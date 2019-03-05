class Weight(object):
      
      OUNCES_PER_POUND=16

      def __init__(self,pounds=0,ounces=0):
          self.pounds=pounds
          self.ounces=ounces
      
      @classmethod
      def from_ounces(cls,s):
          pounds,ounces=divmod(s,cls.OUNCES_PER_POUND)
          return cls(pounds,ounces)

      def total_ounces(self):
          return self.pounds*16+self.ounces

      def __eq__(self,other):
          return self.total_ounces() == other.total_ounces()

      def __gt__(self,other):
          return self.total_ounces() > other.total_ounces()
      
      def __ge__(self,other):
          return self.total_ounces() >= other.total_ounces()

      def __lt__(self,other):
          return self.total_ounces() < other.total_ounces()
      
      def __le__(self,other):
          return self.total_ounces() <= other.total_ounces()

      def __str__(self):
          return "{} pound(s) and {} ounce(s)".format(self.pounds,self.ounces)

   
