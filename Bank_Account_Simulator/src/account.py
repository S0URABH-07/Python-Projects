class Account:
    def __init__(self, account_number, name, pin, balance, history=None):
        # Initializing core bank account details
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = float(balance)
        
        if history == None:
            self.history = [f"Account created with initial balance of ₹{self.balance}"]
        else:
            self.history = history

    def verify_pin(self, entered_pin):
        if self.pin == entered_pin:
            return True
        else:
            print("Access Denied: Invalid PIN!")
            return False

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero!")
            return False
        else:
            self.balance = self.balance + amount
            self.history.append(f"Deposited: +₹{amount}")
            print(f"₹{amount} deposited successfully.")
            return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero!")
            return False
        elif amount > self.balance:
            print(f"Transaction Declined: Insufficient funds! Current Balance: ₹{self.balance}")
            return False
        else:
            self.balance = self.balance - amount
            self.history.append(f"Withdrew: -₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
            return True

    def to_dict(self):
        account_dictionary = {
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "history": self.history
        }
        return account_dictionary