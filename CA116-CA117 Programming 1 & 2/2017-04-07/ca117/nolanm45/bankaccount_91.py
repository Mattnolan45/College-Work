class BankAccount(object):
   next_account_number = 16555232

   def __init__(self, forename = "", surname = "", balance = 0, account_number = None):
      self.forename = forename
      self.surname = surname
      self.balance = balance
      if account_number is None:
         self.account_number = BankAccount.next_account_number
      else:
         self.account_number = account_number 
      BankAccount.next_account_number += 1

   def lodge(self, lodgement):
      self.balance += lodgement
      return(self.balance)

   def __str__(self):
      line1 = "Name: {}".format(self.forename + " " + self.surname)
      line2 = "Account number: {}".format(self.account_number)
      line3 = "Balance: {:.2f}".format(self.balance)
      return("\n".join([line1, line2, line3]))

class CurrentAccount(BankAccount):
   overdraft = 1000
   account_type = "Account type: current"

   def withdraw(self, taken):
      if (self.balance + self.overdraft) - taken < 0:
         print("Insufficient funds available")
      else:
         self.balance -= taken
         return(self.balance)

   def __str__(self):
      part1 = super().__str__()
      part2 = "{}".format(self.account_type)
      return("\n".join([part1, part2]))

class SavingsAccount(BankAccount):
   interest_rate = 0.01
   account_type = "Account type: savings"

   def apply_interest(self):
      self.balance += self.balance * self.interest_rate
      return(self.balance)

   def withdraw(self, taken):
      if self.balance - taken < 0:
         print("Insufficient funds available")
      else:
         self.balance -= taken
         return(self.balance)

   def __str__(self):
      part1 = super().__str__()
      part2 = "{}".format(self.account_type)
      return("\n".join([part1, part2]))