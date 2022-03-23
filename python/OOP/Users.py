class User:		# define the user variables
    def __init__(self, name, email, account_no, int_balance):
        self.name = name
        self.email = email
        self.account_no = account_no
        self.balance=int_balance

    def make_deposit(self, amount):
        self.balance +=amount

    # Business processes with drawal 
    def make_withdrawal(self, amount):	# takes take from the amount
        if amount>self.balance:
            return False
        self.balance -= amount
   
    # Business processes print the balance
    def display_user_balance(self):
        print("Name: ",self.name, "Balance: ",self.balance)
    
    def transfer_balance(self, other_user, amount):
        self.balance-=amount
        other_user.balance +=amount

    
        
ameer = User("Ameer", "Ameer14@gmail.com", 140315, 175860)
Mody = User("Mody", "mody12@gmail.com", 130812, 97820)
ameer.make_withdrawal(400)
ameer.make_withdrawal(2000)
ameer.make_deposit(5500)
ameer.transfer_balance(Mody, 6000)
ameer.display_user_balance()
Mody.display_user_balance()
# print(ameer.make_withdrawal)
# print(ameer.display_user_balance)