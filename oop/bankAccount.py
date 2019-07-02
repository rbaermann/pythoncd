class BankAccount:
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


# ryan = BankAccount('Ryan')
# ryan1 = BankAccount('Ryan1')

# print(ryan.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(150).display_account_info())

# print(ryan1.make_deposit(100).make_deposit(500).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).make_withdrawal(100).yield_interest().display_account_info())

# print(ryan.make_deposit(10).make_withdrawal(20).display_account_info())

