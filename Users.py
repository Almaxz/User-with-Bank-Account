class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, ":", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        self.other_user = other_user
        other_user.account_balance += amount
        print(self.name, ":", self.account_balance)
        print(other_user.name, ":", other_user.account_balance)
        return self


alpha = User("Alpha", "alpha@gmail.com")
beta = User("Beta", "beta@gmail.com")
charlie = User("Charlie", "charlie@gmail.com")

alpha.make_deposit(5000).make_deposit(1500).make_deposit(3300).make_withdrawal(2500).display_user_balance()

beta.make_deposit(9200).make_deposit(1200).make_withdrawal(3000).make_withdrawal(500).display_user_balance()

charlie.make_deposit(50000).make_withdrawal(2500).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()

alpha.transfer_money(charlie, 2500)
