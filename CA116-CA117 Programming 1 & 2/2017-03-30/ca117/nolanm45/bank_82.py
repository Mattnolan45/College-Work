class BankAccount(object):
    
      next_account_number=16555232
      total_lodgements=0
      interest_rate=0.043

      def __init__(self,forname,surname,balance=0,account_number=0):
          self.forname=forname
          self.surname=surname
          self.balance=balance
          self.account_number=BankAccount.next_account_number
          BankAccount.next_account_number+=1
         
      
      def lodge(self,amount):
           self.balance+=amount
           BankAccount.total_lodgements+=1 
           
 
      def apply_interest(self):
          self.balance=self.balance*(1+BankAccount.interest_rate)
          BankAccount.total_lodgements+=1 
      
      def __iadd__(self,other):
          z=self.balance+other
          self.balance=z
          return self

      def __str__(self):
          return "Name: {}\nAccount number: {}\nBalance: {:.2f}".format(" ".join([self.forname,self.surname]),self.account_number,self.balance)

