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

      def __add__(self,other):
          z=Weight(self.pounds + other.pounds, self.ounces + other.ounces)
          return Weight.from_ounces(Weight.total_ounces(z))
      
      def __iadd__(self,other):
          z=self+other
          self.pounds,self.ounces= z.pounds,z.ounces
          return self
  
      def __mul__(self,other):
          z=Weight(self.pounds*other,self.ounces*other)
          return Weight.from_ounces(Weight.total_ounces(z))

      def __imul__(self,other):
          z=self*other
          self.pounds,self.ounces=z.pounds,z.ounces
          return self

      def __str__(self):
          return "{} pound(s) and {} ounce(s)".format(self.pounds,self.ounces)

   
