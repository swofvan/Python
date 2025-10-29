# You are helping a bank manage different types of bank accounts.
# Your task is to create a simple Python program that does the following steps in order:

# Create a base class called Account with an account holder's name (string) and 
# balance (number, like 1000.0). Use a single underscore to keep the name and balance protected.

# Create a class called SavingsAccount that inherits from Account and has a method
# calculate_interest that returns the interest as balance * 0.05 (5% interest).

# Create a class called CurrentAccount that inherits from Account
# and has a method calculate_interest that returns the interest as balance * 0.02 (2% interest).

# Add a special method to the Account class so that using the + operator on two accounts adds their balances together.

# In the main part of the program:
# Create a SavingsAccount object for "Ravi" with a balance of 10000.
# Create a CurrentAccount object for "Anjali" with a balance of 15000.
# Show the name, balance, and interest for each account object.
# Show the total balance by adding the two account objects using the + operator.
# Make the output clear, showing each account’s name, balance, interest, and the total balance.

class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance

    
class SavingsAccount(Account):
    def _init_(self, _name, _balance):
         super()._init_(_name, _balance)

    def calculate_interest(self):
         interest = self._balance * 0.05
         return interest

class CurrentAccount(Account):
    def _init_(self, _name, _balance):
         super()._init_(_name, _balance)

    def calculate_interest(self):
         interest = self._balance * 0.02
         return interest
    

client_1 = SavingsAccount("Ravi", 10000)
client_2 = SavingsAccount("Anjali", 15000)

print(f"Name: {client_1._name}\nBalance: {client_1._balance}\nInterest: {client_1.calculate_interest()}")
print(f"\nName: {client_2._name}\nBalance: {client_2._balance}\nInterest: {client_2.calculate_interest()}")

total_balance = client_1 + client_2
print(f"\nTotal Balance: {total_balance}")