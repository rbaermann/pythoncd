from bankAccount import BankAccount
from user import BasicUser
from usersWithBankAccounts import User

if __name__ == "__main__":
    #this code will only execute when this file is run
    bob = User('bob ross', 'bob@gmail.com')
    print('hi')
bob.make_deposit(100)