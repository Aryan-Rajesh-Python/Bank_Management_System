import hashlib
import json
from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from tkinter.ttk import Treeview

class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Bank System")
        self.master.geometry("800x600")
        self.master.config(bg="#f0f0f0")

        # Initializations
        self.users = {}  # {PIN: {user_data}}
        self.logged_in_user = None
        self.transaction_log = []

        # Create Frames
        self.create_account_frame = Frame(self.master, bg="#f0f0f0")
        self.login_frame = Frame(self.master, bg="#f0f0f0")
        self.user_details_frame = Frame(self.master, bg="#f0f0f0")
        self.account_list_frame = Frame(self.master, bg="#f0f0f0")

        self.create_account_frame.pack(pady=20)
        self.login_frame.pack(pady=20)

        # UI for Create Account Frame
        self.name_label = Label(self.create_account_frame, text="Name:", font=('Arial', 12), bg="#f0f0f0")
        self.name_label.grid(row=0, column=0)
        self.name_entry = Entry(self.create_account_frame, font=('Arial', 12))
        self.name_entry.grid(row=0, column=1)

        self.age_label = Label(self.create_account_frame, text="Age:", font=('Arial', 12), bg="#f0f0f0")
        self.age_label.grid(row=1, column=0)
        self.age_entry = Entry(self.create_account_frame, font=('Arial', 12))
        self.age_entry.grid(row=1, column=1)

        self.salary_label = Label(self.create_account_frame, text="Salary:", font=('Arial', 12), bg="#f0f0f0")
        self.salary_label.grid(row=2, column=0)
        self.salary_entry = Entry(self.create_account_frame, font=('Arial', 12))
        self.salary_entry.grid(row=2, column=1)

        self.account_type_label = Label(self.create_account_frame, text="Account Type:", font=('Arial', 12), bg="#f0f0f0")
        self.account_type_label.grid(row=3, column=0)
        self.account_type = ttk.Combobox(self.create_account_frame, values=["Checking", "Savings"], font=('Arial', 12))
        self.account_type.grid(row=3, column=1)

        self.pin_label = Label(self.create_account_frame, text="PIN:", font=('Arial', 12), bg="#f0f0f0")
        self.pin_label.grid(row=4, column=0)
        self.pin_entry = Entry(self.create_account_frame, show="*", font=('Arial', 12))
        self.pin_entry.grid(row=4, column=1)

        self.create_button = Button(self.create_account_frame, text="Create Account", font=('Arial', 12), command=self.create_account)
        self.create_button.grid(row=5, columnspan=2)

        # Login Frame UI
        self.login_pin_label = Label(self.login_frame, text="Enter PIN:", font=('Arial', 12), bg="#f0f0f0")
        self.login_pin_label.grid(row=0, column=0)
        self.login_pin_entry = Entry(self.login_frame, show="*", font=('Arial', 12))
        self.login_pin_entry.grid(row=0, column=1)

        self.login_button = Button(self.login_frame, text="Login", font=('Arial', 12), command=self.login)
        self.login_button.grid(row=1, columnspan=2)

        # User Details Frame UI
        self.name_label2 = Label(self.user_details_frame, text="Name:", font=('Arial', 12), bg="#f0f0f0")
        self.name_label2.grid(row=0, column=0)
        self.age_label2 = Label(self.user_details_frame, text="Age:", font=('Arial', 12), bg="#f0f0f0")
        self.age_label2.grid(row=1, column=0)
        self.salary_label2 = Label(self.user_details_frame, text="Salary:", font=('Arial', 12), bg="#f0f0f0")
        self.salary_label2.grid(row=2, column=0)
        self.account_type_label2 = Label(self.user_details_frame, text="Account Type:", font=('Arial', 12), bg="#f0f0f0")
        self.account_type_label2.grid(row=3, column=0)
        self.current_balance_label = Label(self.user_details_frame, text="Balance:", font=('Arial', 12), bg="#f0f0f0")
        self.current_balance_label.grid(row=4, column=0)

        self.deposit_button = Button(self.user_details_frame, text="Deposit", font=('Arial', 12), command=self.deposit)
        self.deposit_button.grid(row=5, column=0)

        self.withdraw_button = Button(self.user_details_frame, text="Withdraw", font=('Arial', 12), command=self.withdraw)
        self.withdraw_button.grid(row=5, column=1)

        self.transfer_button = Button(self.user_details_frame, text="Transfer Money", font=('Arial', 12), command=self.transfer_money)
        self.transfer_button.grid(row=6, columnspan=2)

        self.view_transactions_button = Button(self.user_details_frame, text="View Transactions", font=('Arial', 12), command=self.view_transaction_log)
        self.view_transactions_button.grid(row=7, columnspan=2)

        self.logout_button = Button(self.user_details_frame, text="Logout", font=('Arial', 12), command=self.logout)
        self.logout_button.grid(row=8, columnspan=2)

        # Account List Frame UI
        self.account_list_button = Button(self.master, text="View All Accounts", font=('Arial', 12), command=self.show_account_list)
        self.account_list_button.pack(pady=20)

        # Account Holder List UI
        self.account_list = Treeview(self.account_list_frame, columns=("PIN", "Name", "Status"), show="headings", height=10)
        self.account_list.heading("PIN", text="PIN")
        self.account_list.heading("Name", text="Name")
        self.account_list.heading("Status", text="Status")
        self.account_list.pack()

    def create_account(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        salary = self.salary_entry.get()
        pin = self.pin_entry.get()
        account_type = self.account_type.get()

        if name and age and salary and pin and account_type:
            hashed_pin = hashlib.sha256(pin.encode()).hexdigest()
            self.users[hashed_pin] = {
                'name': name,
                'age': age,
                'salary': salary,
                'balance': 0,
                'transaction_log': [],
                'status': 'active',
                'account_type': account_type,
                'interest_rate': 0.03 if account_type == 'Savings' else 0,
                'locked': False  # New field for account lock
            }
            messagebox.showinfo("Success", "Account created successfully!")
            self.clear_create_account_fields()
        else:
            messagebox.showerror("Error", "Please fill all the fields!")

    def clear_create_account_fields(self):
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.pin_entry.delete(0, END)
        self.account_type.set('')

    def login(self):
        pin = self.login_pin_entry.get()
        hashed_pin = hashlib.sha256(pin.encode()).hexdigest()

        if hashed_pin in self.users and not self.users[hashed_pin]['locked']:
            user = self.users[hashed_pin]
            self.logged_in_user = user
            self.transaction_log = user['transaction_log']
            self.show_user_details(user)
        else:
            messagebox.showerror("Error", "Invalid PIN or Account is Locked!")

    def show_user_details(self, user):
        # Hide other frames to show user details frame
        self.create_account_frame.pack_forget()
        self.login_frame.pack_forget()
        self.user_details_frame.pack()

        # Update labels with user details
        self.name_label2.config(text="Name: " + user['name'])
        self.age_label2.config(text="Age: " + str(user['age']))  # Ensure age is treated as an integer
        self.salary_label2.config(text="Salary: " + str(user['salary']))  # Ensure salary is a string/number
        self.account_type_label2.config(text="Account Type: " + user['account_type'])
        self.current_balance_label.config(text="Current Balance: " + str(user['balance']))

        # Apply interest if the account is a savings account
        if user['account_type'] == 'Savings':
            # Check if interest has already been applied (optional)
            # For example, you can use a flag in user data to prevent double application
            if 'interest_applied' not in user or not user['interest_applied']:
                self.apply_interest(user)
                # Mark that interest has been applied
                user['interest_applied'] = True

    def apply_interest(self, user):
        # Check if the account type is Savings
        if user['account_type'] == 'Savings':
            # Example interest rate (3% per deposit cycle)
            interest_rate = 0.03
            # Calculate the interest
            interest = user['balance'] * interest_rate
            # Add the interest to the balance
            user['balance'] += interest
            # Log the interest application in the transaction log
            user['transaction_log'].append(f"Interest applied: {interest:.2f}")
            
            # Show a message confirming interest application
            messagebox.showinfo("Interest Applied", f"Interest of {interest:.2f} has been applied to your account!")
            
            # Update the balance label with the new balance
            self.current_balance_label.config(text="Current Balance: " + str(user['balance']))

    def deposit(self):
        # Ask the user for the deposit amount
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")

        # Check if the amount is valid (greater than 0)
        if amount and amount > 0:
            # Update the balance with the deposit
            self.logged_in_user['balance'] += amount
            # Log the transaction
            self.logged_in_user['transaction_log'].append(f"Deposited {amount}")
            
            # Apply interest if the account type is Savings
            if self.logged_in_user['account_type'] == 'Savings':
                self.apply_interest(self.logged_in_user)
            
            # Update the balance display
            self.current_balance_label.config(text="Current Balance: " + str(self.logged_in_user['balance']))
            
            # Show success message
            messagebox.showinfo("Success", f"Deposited {amount} successfully!")
        else:
            # Handle invalid deposit amount (e.g., negative or zero)
            messagebox.showerror("Error", "Please enter a valid amount to deposit.")

    def withdraw(self):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        if amount and amount > 0:
            if self.logged_in_user['balance'] >= amount:
                self.logged_in_user['balance'] -= amount
                self.logged_in_user['transaction_log'].append(f"Withdrew {amount}")
                self.current_balance_label.config(text="Current Balance: " + str(self.logged_in_user['balance']))  # Update balance label
                messagebox.showinfo("Success", f"Withdrew {amount} successfully!")
            else:
                messagebox.showerror("Error", "Insufficient balance!")

    def transfer_money(self):
        recipient_pin = simpledialog.askstring("Transfer", "Enter recipient's PIN:")
        amount = simpledialog.askfloat("Transfer", "Enter amount to transfer:")

        if recipient_pin and amount and amount > 0:
            recipient_pin_hashed = hashlib.sha256(recipient_pin.encode()).hexdigest()
            if recipient_pin_hashed in self.users:
                recipient = self.users[recipient_pin_hashed]
                if self.logged_in_user['balance'] >= amount:
                    self.logged_in_user['balance'] -= amount
                    recipient['balance'] += amount
                    self.logged_in_user['transaction_log'].append(f"Transferred {amount} to {recipient['name']}")
                    recipient['transaction_log'].append(f"Received {amount} from {self.logged_in_user['name']}")
                    self.current_balance_label.config(text="Current Balance: " + str(self.logged_in_user['balance']))  # Update balance label
                    messagebox.showinfo("Success", f"Transferred {amount} to {recipient['name']} successfully!")
                else:
                    messagebox.showerror("Error", "Insufficient balance!")
            else:
                messagebox.showerror("Error", "Recipient not found!")

    def view_transaction_log(self):
        log = "\n".join(self.logged_in_user['transaction_log'])
        messagebox.showinfo("Transaction Log", log)

    def logout(self):
        self.logged_in_user = None
        self.transaction_log = []
        self.user_details_frame.pack_forget()
        self.create_account_frame.pack(pady=20)
        self.login_frame.pack(pady=20)

    def show_account_list(self):
        self.account_list_frame.pack_forget()  # Hide previous frame
        self.account_list_frame.pack(pady=20)
        self.account_list.delete(*self.account_list.get_children())

        for pin, user in self.users.items():
            self.account_list.insert("", "end", values=(pin[-4:], user["name"], user["status"]))

    def lock_account(self):
        pin = simpledialog.askstring("Lock Account", "Enter the PIN of the account to lock:")
        pin_hashed = hashlib.sha256(pin.encode()).hexdigest()
        if pin_hashed in self.users:
            self.users[pin_hashed]['locked'] = True
            messagebox.showinfo("Account Locked", "Account has been locked successfully.")
        else:
            messagebox.showerror("Error", "Account not found.")

    def unlock_account(self):
        pin = simpledialog.askstring("Unlock Account", "Enter the PIN of the account to unlock:")
        pin_hashed = hashlib.sha256(pin.encode()).hexdigest()
        if pin_hashed in self.users:
            self.users[pin_hashed]['locked'] = False
            messagebox.showinfo("Account Unlocked", "Account has been unlocked successfully.")
        else:
            messagebox.showerror("Error", "Account not found.")

if __name__ == "__main__":
    root = Tk()
    bank_system = BankSystem(root)
    root.mainloop()
