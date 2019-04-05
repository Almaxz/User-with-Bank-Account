from Bank_Account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        self.saving = BankAccount(int_rate = 0.05, balance = 0)

    def make_deposit(self, amount, account_name):
        if account_name == "Checking":
            self.account.deposit(amount)

        elif account_name == "Saving":
            self.saving.deposit(amount)
            
        return self

    def make_withdrawal(self, amount, account_name):
        if account_name == "Checking":
            self.account.withdraw(amount)

        elif account_name == "Saving":
            self.saving.withdraw(amount)
            
        return self

    def display_useraccount(self, account_name):
        if account_name == "Checking":
            print(self.name, ":", "Checking =", self.account.balance)

        elif account_name == "Saving":
            print(self.name, ":", "Saving =", self.saving.balance)

        else:
            print(self.name, ":", "Checking =",self.account.balance, "Saving =", self.saving.balance)
            
        return self

    def transfer_money(self, other_user, amount, account_name):
        self.other_user = other_user
        if account_name == "Checking":
            if self.account.balance < amount:
                self.account.withdraw(amount)

            else:
                self.account.withdraw(amount)
                other_user.account.deposit(amount)

            print(self.name, ":", "Checking =", self.account.balance)
            print(other_user.name, ":", "Checking =", other_user.account.balance)

        elif account_name == "Saving":
            self.saving.withdraw(amount)
            other_user.saving.deposit(amount)
            print(self.name, ":", "Saving =", self.account.balance)
            print(other_user.name, ":", "Saving =", other_user.account.balance)

        else:
            if self.account.balance < amount:
                self.account.withdraw(amount)

            else:
                self.account.withdraw(amount)
                other_user.account.deposit(amount)

            print(self.name, ":", "Checking =",self.account.balance, "Saving =", self.saving.balance)
            print(other_user.name, ":", "Checking =",other_user.account.balance, "Saving =", other_user.saving.balance)
        
        return self

alpha = User("Alpha", "alpha@gmail.com")
beta = User("Beta", "beta@gmail.com")
charlie = User("Charlie", "charlie@gmail.com")

alpha.make_deposit(5000, "Saving").make_deposit(1500, "Checking").make_deposit(3300, "Checking").make_withdrawal(2500, "Checking").display_useraccount("")

beta.make_deposit(9200, "Saving").make_deposit(1200, "Checking").make_withdrawal(3000, "Saving").make_withdrawal(500, "Checking").display_useraccount("")

charlie.make_deposit(50000, "Saving").make_withdrawal(2500, "Saving").make_withdrawal(1000, "Saving").make_withdrawal(1000, "Saving").display_useraccount("")

alpha.transfer_money(charlie, 2000, "")
