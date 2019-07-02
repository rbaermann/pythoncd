class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        return (f'User: {self.name}, Balance {self.account.balance}')

    def transfer_money(self, self1, amount):
        self.account.balance -= amount
        self1.account.balance += amount
        return (f'User: {self.name}, Balance {self.account.balance}, User: {self1.name}, Balance {self1.account.balance}')


class BankAccount(User):
    def __init__(self, int_rate='', balance=''):
        self.int_rate = .001
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return (f'Balance: ${self.balance}')

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(self.balance)
            return self

    def transfer_money(self, self1, amount):
        self.balance -= amount
        self1.balance += amount
        return (f'User: {self.name}, Balance {self.balance}, User: {self1.name}, Balance {self1.balance}')
        

ryan = User('Ryan', 'ryansucks@123.com')
print(ryan.account.make_deposit(100).yield_interest().display_account_info())