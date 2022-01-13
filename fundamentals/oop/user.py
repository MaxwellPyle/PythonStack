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

max.make_deposit(100)
max.make_deposit(200)
max.make_deposit(400)
print(max.account_balance)

paisley.make_deposit(200)
paisley.make_deposit(400)
paisley.make_withdrawal(100)
paisley.make_withdrawal(200)
print(paisley.account_balance)

zed.make_deposit(200)
zed.make_withdrawal(40)
zed.make_withdrawal(30)
zed.make_withdrawal(10)
print(zed.account_balance)

paisley.display_user_balance()