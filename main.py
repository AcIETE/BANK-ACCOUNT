"""
Main program to demonstrate Savings and Checking accounts.
This module creates instances of both account types, demonstrates their features,
and illustrates a realistic banking scenario.
"""

from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    """Main function to run the bank account demonstration."""
    
    print("\n" + "="*70)
    print("BANK ACCOUNT MANAGEMENT SYSTEM DEMONSTRATION")
    print("="*70)
    
    # ==================== SAVINGS ACCOUNTS ====================
    print("\n" + "▼"*70)
    print("SAVINGS ACCOUNTS")
    print("▼"*70)
    
    # Savings Account Instance 1: Alice
    print("\n--- Creating Savings Account #1 ---")
    savings1 = SavingsAccount(
        customer_name="Alice Johnson",
        current_balance=5000.00,
        minimum_balance=500.00,
        account_number="SA001234567",
        routing_number="021000021",
        interest_rate=2.5
    )
    savings1.print_customer_information()
    
    print("Deposit $1500:")
    savings1.deposit(1500)
    
    print("\nApplying annual interest:")
    savings1.apply_interest()
    
    print("\nWithdraw $1000:")
    savings1.withdraw(1000)
    
    savings1.print_customer_information()
    
    # Savings Account Instance 2: Bob
    print("\n--- Creating Savings Account #2 ---")
    savings2 = SavingsAccount(
        customer_name="Bob Smith",
        current_balance=10000.00,
        minimum_balance=1000.00,
        account_number="SA009876543",
        routing_number="021000021",
        interest_rate=3.0
    )
    savings2.print_customer_information()
    
    print("Deposit $2000:")
    savings2.deposit(2000)
    
    print("\nUpdating interest rate to 3.5%:")
    savings2.set_interest_rate(3.5)
    
    print("\nApplying annual interest:")
    savings2.apply_interest()
    
    savings2.print_customer_information()
    
    # ==================== CHECKING ACCOUNTS ====================
    print("\n" + "▼"*70)
    print("CHECKING ACCOUNTS")
    print("▼"*70)
    
    # Checking Account Instance 1: Carol
    print("\n--- Creating Checking Account #1 ---")
    checking1 = CheckingAccount(
        customer_name="Carol Davis",
        current_balance=3000.00,
        minimum_balance=200.00,
        account_number="CA112233445",
        routing_number="021000021",
        transfer_limit=5000.00
    )
    checking1.print_customer_information()
    
    # Scenario: User opens a checking account and withdraws money
    print("=== SCENARIO: Carol opens checking account and withdraws $500 ===")
    print("\nWithdraw $500:")
    checking1.withdraw(500)
    
    print("\nTransfer $300 to John Doe:")
    checking1.transfer(300, "John Doe")
    
    print("\nAttempt to transfer $6000 (exceeds transfer limit of $5000):")
    checking1.transfer(6000, "Jane Smith")
    
    print("\nDeposit $1000:")
    checking1.deposit(1000)
    
    checking1.print_customer_information()
    
    # Checking Account Instance 2: David
    print("\n--- Creating Checking Account #2 ---")
    checking2 = CheckingAccount(
        customer_name="David Wilson",
        current_balance=8000.00,
        minimum_balance=500.00,
        account_number="CA998877665",
        routing_number="021000021",
        transfer_limit=2500.00
    )
    checking2.print_customer_information()
    
    print("Withdraw $2000:")
    checking2.withdraw(2000)
    
    print("\nTransfer $1500 to Michael Johnson:")
    checking2.transfer(1500, "Michael Johnson")
    
    print("\nTransfer $1000 to Sarah Brown:")
    checking2.transfer(1000, "Sarah Brown")
    
    print("\nAttempt to transfer $3000 (exceeds transfer limit of $2500):")
    checking2.transfer(3000, "Emma Wilson")
    
    print("\nUpdating transfer limit to $4000:")
    checking2.set_transfer_limit(4000)
    
    print("\nTransfer $3500 to Lisa Anderson:")
    checking2.transfer(3500, "Lisa Anderson")
    
    checking2.print_customer_information()
    
    # ==================== SUMMARY ====================
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print("\n✓ Created 2 Savings Accounts with interest calculation")
    print("✓ Created 2 Checking Accounts with transfer limitations")
    print("✓ Demonstrated deposit, withdrawal, and transfer operations")
    print("✓ Protected and private members (account number, routing number)")
    print("✓ All accounts properly initialized with separate instances")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
