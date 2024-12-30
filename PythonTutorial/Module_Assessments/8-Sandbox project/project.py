import os
import random
from datetime import datetime

class BankAccount:
    def __init__(self, name, account_type, balance=0):
        """Initialize the bank account with name, account type, and initial balance."""
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.account_id = random.randint(1000, 9999)  # Randomly generate an account ID
        
        # Create a transaction history file for the user
        self.statement_file = f"{self.name}_{self.account_type}_{self.account_id}_statement.txt"
        
        # Initialize the statement file with the account creation information
        self.create_transaction_history("Account created.")
    
    def create_transaction_history(self, transaction):
        """Logs the transaction to the user's statement file."""
        with open(self.statement_file, "a") as file:
            file.write(f"{datetime.now()} - {transaction}\n")
    
    def deposit(self, amount):
        """Deposits money into the account and records the transaction."""
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            self.create_transaction_history(f"Deposited ${amount}.")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraws money from the account if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.create_transaction_history(f"Withdrew ${amount}.")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Returns the current balance of the account."""
        print(f"Current balance: ${self.balance}")
        return self.balance
    
    def get_account_id(self):
        """Returns the account ID."""
        return self.account_id
    
    def get_username(self):
        """Returns the account holder's username."""
        return self.name
    
    def get_account_type(self):
        """Returns the type of account (e.g., checking or savings)."""
        return self.account_type
    
    def get_transaction_history(self):
        """Displays the transaction history by reading the statement file."""
        if os.path.exists(self.statement_file):
            print(f"\nTransaction History for {self.name} ({self.account_type}):")
            with open(self.statement_file, "r") as file:
                transactions = file.readlines()
                for transaction in transactions:
                    print(transaction.strip())
        else:
            print("No transaction history available.")
    
def main():
    # Create a new bank account for user 'Alice' with a savings account
    alice_account = BankAccount("Alice", "savings")
    
    # Perform various transactions
    alice_account.deposit(500)
    alice_account.withdraw(200)
    alice_account.deposit(150)
    alice_account.withdraw(1000)  # This should fail due to insufficient funds
    
    # Check the balance
    alice_account.get_balance()
    
    # Get account information
    print(f"Account ID: {alice_account.get_account_id()}")
    print(f"Account Holder: {alice_account.get_username()}")
    print(f"Account Type: {alice_account.get_account_type()}")
    
    # View transaction history
    alice_account.get_transaction_history()

    # Create a new bank account for user 'Bob' with a checking account
    bob_account = BankAccount("Bob", "checking")
    
    # Perform some transactions for Bob
    bob_account.deposit(200)
    bob_account.withdraw(50)
    
    # View Bob's transaction history
    bob_account.get_transaction_history()

if __name__ == "__main__":
    main()
