class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate * 0.01 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            
        else:
            self.balance -= amount
        
        return self
        
    def display_account_info(self):
        print("Balance:", "$", self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# alpha = BankAccount( 1, 0)
# beta = BankAccount( 1, 0)

# alpha.deposit(500).deposit(1000).deposit(1500).yield_interest().display_account_info()

# beta.deposit(1000).deposit(5000).withdraw(500).withdraw(100).withdraw(600).withdraw(300).yield_interest().display_account_info()