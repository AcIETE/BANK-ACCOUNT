"""
Base BankAccount class that models a simple bank account with attributes for customer name, current
balance, and minimum balance. It includes methods for depositing and withdrawing money.
"""


class BankAccount:
    """Base class for all bank accounts"""
    
    # Class attribute
    bank_title = "Bank of America"
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        """
        Initialize a BankAccount instance.
        
        Args:
            customer_name (str): Name of the customer
            current_balance (float): Current account balance
            minimum_balance (float): Minimum balance required
            account_number (str): Account number (private member)
            routing_number (str): Routing number (private member)
        """
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number  # Private member
        self.__routing_number = routing_number  # Private member
    
    def get_account_number(self):
        """Get the account number."""
        return self.__account_number
    
    def get_routing_number(self):
        """Get the routing number."""
        return self.__routing_number
    
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
        Print customer information including bank title, account and routing numbers.
        """
        print("\n" + "="*60)
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Routing Number: {self.__routing_number}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("="*60 + "\n")
