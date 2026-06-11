"""
SavingsAccount class that extends BankAccount with interest calculation.
"""

from account import BankAccount


class SavingsAccount(BankAccount):
    """Savings Account with interest calculation"""
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        """
        Initialize a SavingsAccount instance.
        
        Args:
            customer_name (str): Name of the customer
            current_balance (float): Current account balance
            minimum_balance (float): Minimum balance required
            account_number (str): Account number (private)
            routing_number (str): Routing number (private)
            interest_rate (float): Annual interest rate (as percentage, e.g., 2.5 for 2.5%)
        """
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self._interest_rate = interest_rate  # Protected member
    
    def apply_interest(self):
        """
        Apply annual interest to the account balance.
        """
        interest_earned = self.current_balance * (self._interest_rate / 100)
        self.current_balance += interest_earned
        print(f"Interest applied: ${interest_earned:.2f}")
        print(f"New balance after interest: ${self.current_balance:.2f}")
    
    def get_interest_rate(self):
        """Get the interest rate."""
        return self._interest_rate
    
    def set_interest_rate(self, new_rate):
        """Set a new interest rate."""
        self._interest_rate = new_rate
        print(f"Interest rate updated to {self._interest_rate}%")
    
    def print_customer_information(self):
        """
        Print customer information including interest rate.
        """
        super().print_customer_information()
        print(f"Account Type: Savings Account")
        print(f"Interest Rate: {self._interest_rate}%\n")
