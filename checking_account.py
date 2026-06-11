"""
CheckingAccount class that extends BankAccount with transfer limitation.
"""

from account import BankAccount


class CheckingAccount(BankAccount):
    """Checking Account with transfer limitation"""
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        """
        Initialize a CheckingAccount instance.
        
        Args:
            customer_name (str): Name of the customer
            current_balance (float): Current account balance
            minimum_balance (float): Minimum balance required
            account_number (str): Account number (private)
            routing_number (str): Routing number (private)
            transfer_limit (float): Maximum amount that can be transferred per transaction
        """
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self._transfer_limit = transfer_limit  # Protected member
        self._transfers_made = 0  # Protected member to track transfers
    
    def transfer(self, amount, recipient_name):
        """
        Transfer money to another account.
        
        Args:
            amount (float): Amount to transfer
            recipient_name (str): Name of the recipient
        """
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self._transfer_limit:
            print(f"Cannot transfer ${amount:.2f}. Transfer limit is ${self._transfer_limit:.2f}")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Cannot transfer ${amount:.2f}. Remaining balance would be less than minimum balance of ${self.minimum_balance:.2f}")
        else:
            self.current_balance -= amount
            self._transfers_made += 1
            print(f"${amount:.2f} transferred to {recipient_name} successfully.")
            print(f"New balance: ${self.current_balance:.2f}")
    
    def get_transfer_limit(self):
        """Get the transfer limit."""
        return self._transfer_limit
    
    def set_transfer_limit(self, new_limit):
        """Set a new transfer limit."""
        self._transfer_limit = new_limit
        print(f"Transfer limit updated to ${self._transfer_limit:.2f}")
    
    def get_transfers_made(self):
        """Get the number of transfers made."""
        return self._transfers_made
    
    def print_customer_information(self):
        """
        Print customer information including transfer limit.
        """
        super().print_customer_information()
        print(f"Account Type: Checking Account")
        print(f"Transfer Limit: ${self._transfer_limit:.2f}")
        print(f"Transfers Made: {self._transfers_made}\n")
