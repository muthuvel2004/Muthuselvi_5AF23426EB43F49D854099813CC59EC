class BankAccount:
  def initial(self,account_number,account_holder_name,initial_balance):
   self.__account_number=account_number
   self.__account_holder_name= account_holder_name
   self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance += amount
      print("Deposited Rs.{}\nnow balance: rs.{}".format(amount,self.__account_balance))
      print("\n")
    else:
      print("invalid deposit")
      print("\n")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance -= amount
      print("withdraw rs .{}\nnow balance: rs.{}".format(amount,self.__account_balance))
      print("\n")
    else:
      print("invalid withdraw or amount insufficient")
      print("\n")
  def display(self):
    print("account holder:{}\naccount number:{}\naccount balance:{}.".format(self.__account_holder_name,self.__account_number,self.__account_balance))
    print("\n")
account = BankAccount()
account.initial(account_number="2005" ,account_holder_name="joysha",initial_balance=9000.0)
account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()