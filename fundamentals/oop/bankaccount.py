class BankAccount:
    def __init__(self,interest,balance = 0):
        self.interest = interest/100
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdrawal(self,amount):
        if (self.balance > amount):
            self.balance -= amount
            return self
        else:
            print("insufficient funds: Charging 5$ fee")

    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest: {self.interest}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance*self.interest
        return self

max = BankAccount(3,5000)
max.deposit(400).deposit(5000).deposit(4000).withdrawal(3000).yield_interest().display_account_info()

paisley = BankAccount(5,6000)
paisley.deposit(500).deposit(5000).withdrawal(40).withdrawal(300).withdrawal(400).withdrawal(9).yield_interest().display_account_info()