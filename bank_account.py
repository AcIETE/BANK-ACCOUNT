"""This module defines a BankAccount class that models a simple bank account with attributes for customer name, current
balance, and minimum balance. It includes methods for depositing and withdrawing money, as well as printing customer information.
@author: Bindu Harini Gunturi
@date: 05-28-2026
@author: Gavin Binkley
@author: Achal Ananthabotla
@author: Smriti Bhemireddy
@author: Kaleiah McPherson
"""




class BankAccount:
    # Class attribute
    bank_title = "Bank of America"
    
    def __init__(self, customer_name, current_balance, minimum_balance):
        """
        Initialize a BankAccount instance.
        
        Args:
            customer_name (str): Name of the customer
            current_balance (float): Current account balance
            minimum_balance (float): Minimum balance required
        """
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
        """
        if amount > 0:
            self.current_balance += amount
            print(f"${amount:.2f} deposited successfully.")
            print(f"New balance: ${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Validates that remaining balance will not be less than minimum balance.
        
        Args:
            amount (float): Amount to withdraw
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ${amount:.2f}. Remaining balance would be less than minimum balance of ${self.minimum_balance:.2f}")
        else:
            self.current_balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            print(f"New balance: ${self.current_balance:.2f}")
    
    def print_customer_information(self):
        """
        Print customer information including bank title.
        """
        print("\n" + "="*50)
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("="*50 + "\n")


# Create at least two different instances to make sure it works

# Instance 1: Alice's account
account1 = BankAccount("Bindu Harini", 5000.00, 500.00)
print("Account 1 Created:")
account1.print_customer_information()

# Test deposit
print("Deposit $1000:")
account1.deposit(1000)

# Test valid withdrawal
print("\nWithdraw $2000:")
account1.withdraw(2000)

# Test invalid withdrawal (would go below minimum)
print("\nAttempt to withdraw $3500:")
account1.withdraw(3500)

account1.print_customer_information()

# Instance 2: Bob's account
account2 = BankAccount("Gavin Smith", 2000.00, 300.00)
print("Account 2 Created:")
account2.print_customer_information()

# Test deposit
print("Deposit $500:")
account2.deposit(500)

# Test valid withdrawal
print("\nWithdraw $1500:")
account2.withdraw(1500)
print("\nWithdraw -$100:")
account2.withdraw(-100)  # Invalid withdrawal amount

# Test invalid withdrawal (would go below minimum)
print("\nAttempt to withdraw $1000:")
account2.withdraw(1000)

account2.print_customer_information()
