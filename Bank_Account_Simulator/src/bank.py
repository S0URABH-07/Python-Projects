import json
import os
from src.account import Account

class BankSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        # Key: Account Number, Value: Account Object.
        self.accounts = {}
        
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                raw_data = json.load(file)

                for acc_num, info in raw_data.items():
                    saved_account = Account(
                        account_number=acc_num,
                        name=info["name"],
                        pin=info["pin"],
                        balance=info["balance"],
                        history=info["history"]
                    )
                    # Put it into our active dictionary ledger
                    self.accounts[acc_num] = saved_account
        else:
            self.accounts = {}

    def save_accounts(self):
        output_dictionary = {}
        
        # Convert our objects back to dictionaries for saving
        for acc_num, acc_object in self.accounts.items():
            output_dictionary[acc_num] = acc_object.to_dict()
            
        with open(self.file_path, "w") as file:
            json.dump(output_dictionary, file, indent=4)
        print("Bank vault records backed up safely!")

    def open_account(self, account_number, name, pin, initial_deposit):
        if account_number in self.accounts:
            print("Error: An account with this number already exists!")
            return False
            
        if initial_deposit < 0:
            print("Error: Initial deposit cannot be negative!")
            return False
            
        # Create the new account object
        new_account = Account(account_number, name, pin, initial_deposit)
        self.accounts[account_number] = new_account
        print(f"Account for {name} opened successfully with Number: {account_number}")
        return True

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Error: Account number not found!")
            return None