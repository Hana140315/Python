class User:		# define the user variables
    def __init__(self, name, email, account_no, int_balance):
        self.name = name
        self.email = email
        self.account_no = account_no
        self.balance=int_balance

    def make_deposit(self, amount):
        self.balance +=amount
        return self

    # Business processes with drawal 
    def make_withdrawal(self, amount):	# takes take from the amount
        if amount>self.balance:
            return False
        self.balance -= amount
        return self
   
    # Business processes print the balance
    def display_user_balance(self):
        print("Name: ",self.name, "Balance: ",self.balance)
        return self
    
    def transfer_balance(self, other_user, amount):
        self.balance-=amount
        other_user.balance +=amount
        return self
ameer = User("Ameer", "Ameer14@gmail.com", 140315, 8500)
Mody = User("Mody", "mody12@gmail.com", 130812, 0)
rahaf= User("Rahaf","rahaf",1130,0)
ameer.make_deposit(4800).make_withdrawal(400).make_withdrawal(780).transfer_balance(Mody, 6000).display_user_balance()
Mody.display_user_balance()
rahaf.display_user_balance()
# print(ameer.make_withdrawal)
# print(ameer.display_user_balance)