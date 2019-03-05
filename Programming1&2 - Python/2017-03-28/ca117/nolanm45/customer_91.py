class Customer(object):
    
      def __init__(self,name,balance,addr_1,addr_2,addr_3):
          self.name=name
          self.addr_1=addr_1
          self.addr_2=addr_2
          self.addr_3=addr_3
          self.balance=float(balance)
    
      def owes(self):
          return self.balance - (self.balance*self.discount)
    
      def __str__(self):
          return "{}\n{}\n{}\n{}\nBalance: {:.2f}\nDiscount: {:.0f}%\nAmount due: {:.2f}".format(self.name,self.addr_1,self.addr_2,self.addr_3,self.balance,self.discount*100,self.owes()) 
          
      discount=float(0)
 


class ValuedCustomer(Customer):
      
      discount=float(0.1)
 
 
