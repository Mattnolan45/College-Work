class BankAccount(object):
    
      next_account_number=16555232
      total_lodgements=0
      interest_rate=float(0.043)

      def __init__(self,forname,surname,balance=0,account_number=0):
          self.forname=forname
          self.surname=surname
          self.balance=balance
          self.account_number=BankAccount.next_account_number
          BankAccount.next_account_number+=1
          self.total_lodgements+=1
      
      def lodge(self,amount):
           self.balance+=amount
             
      def apply_interest(self):
          self.balance=self.balance*(1+BankAccont.interest_rate)
 
      def __iadd__(self,other):
          return self.lodge(other)
          

      def __str__(self):
          return "Name: {}\nAccount number: {}\nBalance: {:.2f}".format(" ".join([self.forname,self.surname]),self.account_number,self.balance)

