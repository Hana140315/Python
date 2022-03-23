
class BankAccount:
    def __init__(self, int_rate, ini_balance, account_no):
        self.balance=ini_balance
        self.int_rate= int_rate
        self.account= account_no
     
     # Business processes deposit
    def deposit(self, amount):
        self.account.balance +=amount
        return self
     # Business processes with drawal 
    def withdrawal(self,amount):
        if amount>self.balance:
            return False
        self.account.balance -= amount
        return self
    def display_account_info(self):
        print("Account Balance: ",self.account.balance, "Intrest rate: ",self.int_rate)
        return self
    def yield_interest(self):
        self.account.balance +=self.account.balance*self.int_rate
        return self

class User:
    def __init__(self, name, email, ini_balance, int_rate, account_no):
        self.name=name
        self.email=email
        self.account=BankAccount(ini_balance,int_rate, account_no)

 #   def deposit(self,amount):
  #      self.account.deposit (amount)
 #   def withdrawal(self, amount):
  #      self.account.withdrawal (amount)
   # def display_user_balance(self):
    #    print(self.account.display_account_info())

Hana= BankAccount(0.01, 1500,220178)
Mody=BankAccount(0.014, 500, 130812)
Ameer=BankAccount(0.016, 500, 140315)
Hana=User("Hana", "Hanaalbidaq@hotmail.com", 0.01, 1500, 220178)
Mody=User("Mody", "Mody@hotmail.com", 0.014, 500, 130812)
Ameer=User("Ameer", "ameer@hotmail.com", 0.016, 500, 140315)
Hana.account.deposit(4500).withdrawal(1850).display_account_info()