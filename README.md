# Bank Account Management System

A Python-based bank account management system that demonstrates object-oriented programming principles through inheritance and polymorphism. This project provides a comprehensive framework for managing different types of bank accounts with specialized features.

## Overview

This project implements a bank account system with a base `BankAccount` class and two specialized account types: `SavingsAccount` and `CheckingAccount`. Each account type has unique features tailored to its purpose.

## Features

### Base Account Features
- Deposit and withdrawal operations
- Minimum balance enforcement
- Account holder information management
- Balance tracking and display

### Savings Account
- Annual interest rate calculation and application
- Interest earned tracking
- Ideal for long-term savings

### Checking Account
- Per-transaction transfer limit enforcement
- Transfer operations to other accounts
- Transfer history tracking
- Designed for frequent transactions

## Project Structure

```
BANK-ACCOUNT/
├── account.py              # Base BankAccount class
├── bank_account.py         # Original bank account implementation
├── savings_account.py      # SavingsAccount class (extends BankAccount)
├── checking_account.py     # CheckingAccount class (extends BankAccount)
├── main.py                 # Main demonstration program
└── README.md               # This file
```

## Classes

### BankAccount
The base class for all account types, providing core banking functionality.

**Attributes:**
- `customer_name`: Name of the account holder
- `current_balance`: Current account balance
- `minimum_balance`: Minimum required balance

**Methods:**
- `deposit(amount)`: Add funds to the account
- `withdraw(amount)`: Remove funds from the account (with balance validation)
- `print_customer_information()`: Display account details

### SavingsAccount
Extends `BankAccount` with interest earning capabilities.

**Additional Attributes:**
- `account_number`: Unique account identifier
- `routing_number`: Bank routing number
- `interest_rate`: Annual interest rate (as percentage)

**Additional Methods:**
- `apply_interest()`: Calculate and apply annual interest to the balance

### CheckingAccount
Extends `BankAccount` with transfer capabilities and limits.

**Additional Attributes:**
- `account_number`: Unique account identifier
- `routing_number`: Bank routing number
- `transfer_limit`: Maximum transfer amount per transaction

**Additional Methods:**
- `transfer(amount, recipient_name)`: Transfer funds to another account (subject to limit)

## Usage

Run the main demonstration program:

```bash
python main.py
```

This will demonstrate:
- Creating and managing savings accounts
- Applying interest calculations
- Creating and managing checking accounts
- Performing deposits and withdrawals
- Executing account transfers

## Contributors

- Bindu Harini Gunturi
- Gavin Binkley
- Achal Ananthabotla
- Smriti Bhemireddy
- Kaleiah McPherson

## Date

Last Updated: 05-28-2026
