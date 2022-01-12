class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

max = User("Maxwell Pyle", "maximumlax@gmail.com")
paisley = User("Paisley Pyle","paisleypyle@gmail.com")
zed = User("Zed Pyle","zedp@gmail.com")

max.make_deposit(100).make_deposit(200).make_deposit(400).display_user_balance()

paisley.make_deposit(200).make_deposit(400).make_withdrawal(100).make_withdrawal(200).display_user_balance()

zed.make_deposit(200).make_withdrawal(40).make_withdrawal(30).make_withdrawal(10).display_user_balance()