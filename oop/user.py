class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        return (f'User: {self.name}, Balance {self.balance}')

    def transfer_money(self, self1, amount):
        self.balance -= amount
        self1.balance += amount
        return (f'User: {self.name}, Balance {self.balance}, User: {self1.name}, Balance {self1.balance}')



yumi = User('Yumi', 'yumi@lol.rekt')
yasuo = User('Yasuo', 'fk@lol.rekt')
teemo = User('Teemo', 'sizedoesntmeaneverything@lol.rekt')

# print(yumi.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(275).display_user_balance())

# print(yasuo.make_deposit(2).make_deposit(5).make_withdrawal(10).make_withdrawal(100).display_user_balance())

# print(teemo.make_deposit(1000000000000000).make_withdrawal(5).make_withdrawal(10).make_withdrawal(50).display_user_balance())

# print(yumi.transfer_money(teemo, 50))

print(teemo.make_deposit(100).display_user_balance())