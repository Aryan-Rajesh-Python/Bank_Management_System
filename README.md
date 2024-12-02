# Advanced Bank System

This is a simple bank system built using Python and Tkinter. It allows users to create accounts, log in securely using a PIN, perform transactions such as deposit, withdrawal, and transfer money, and view their account details and transaction logs. The system also applies interest to savings accounts automatically.

## Features

- **Create Account**: Allows users to create an account by entering their name, age, salary, account type, and a PIN for security.
- **User Login**: Users can log in to their account using their PIN. Account status must be active, and the PIN is stored in a hashed format for security.
- **Deposit**: Users can deposit money into their account, and interest is applied if the account is of type "Savings."
- **Withdraw**: Users can withdraw money from their account, as long as the balance is sufficient.
- **Transfer Money**: Allows users to transfer money to another user within the system.
- **Transaction Log**: Users can view all their past transactions, including deposits, withdrawals, and interest applications.
- **Interest Application**: Automatically applies interest to savings accounts at a rate of 3% per cycle.

## Requirements

- Python 3.x
- Tkinter (for the GUI)
- hashlib (for PIN hashing)
- json (for storing user data)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Advanced-Bank-System.git
   cd Advanced-Bank-System
   python bank_system.py
