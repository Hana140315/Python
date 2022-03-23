
class BankAccount:
    def __init__(self, int_rate, ini_balance, account_no):
        self.balance=ini_balance
        self.int_rate= int_rate
        self.account= account_no
     
     # Business processes deposit
    def deposit(self, amount):
        self.balance +=amount
        return self
     # Business processes with drawal 
    def withdrawal(self,amount):
        if amount>self.balance:
            return False
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Account Balance: ",self.balance, "Intrest rate: ",self.int_rate)
        return self
    def yield_interest(self):
        self.balance +=self.balance*self.int_rate
        return self

Hana= BankAccount(0.01, 1500,220178)
Mody=BankAccount(0.014, 500, 130812)
Ameer=BankAccount(0.016, 500, 140315)
Ameer.deposit(4800).withdrawal(400).withdrawal(780).yield_interest().display_account_info()