from fundamentals.oop.bankaccount import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest=5,balance=4000)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)

    def display_user_balance(self):
        print(self.account.display_account_info())


