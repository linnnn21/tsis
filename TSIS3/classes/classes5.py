class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.balance:.2f}")
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance:.2f}"

# Testing the Account class
account = Account("Alina", 100.0)
print(account)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)  # Should be denied
account.withdraw(-10)  # Invalid amount test
print(account)
