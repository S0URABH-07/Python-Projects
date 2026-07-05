import os
from src.bank import BankSystem

def display_menu():
    print("\n====== DIGITAL ATM SIMULATOR ======")
    print("1. Open New Bank Account")
    print("2. Check Account Balance")
    print("3. Deposit Funds")
    print("4. Withdraw Funds")
    print("5. Print Bank Statement Ledger")
    print("6. Exit & Save Records")
    print("===================================")

def main():
    data_directory = "data"
    file_path = os.path.join(data_directory, "bank_data.json")
    
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        
    atm_vault = BankSystem(file_path)
    
    while True:
        display_menu()
        choice = input("Please select a transaction (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Open New Account ---")
            acc_num = input("Create Unique Account Number: ").strip()
            name = input("Enter Account Holder Name: ").strip()
            pin = input("Set Secure 4-Digit PIN: ").strip()
            
            try:
                initial_deposit = float(input("Enter Initial Deposit Amount: ₹"))
            except ValueError:
                print("Error: Initial deposit must be a valid number!")
                continue
                
            atm_vault.open_account(acc_num, name, pin, initial_deposit)
            
        elif choice == "2":
            print("\n--- Check Balance ---")
            acc_num = input("Enter Account Number: ").strip()
            account = atm_vault.get_account(acc_num)
            
            if account != None:
                entered_pin = input("Enter Your PIN: ").strip()
                if account.verify_pin(entered_pin) == True:
                    print(f"Account Holder: {account.name}")
                    print(f"Current Available Balance: ₹{account.balance}")
                    
        elif choice == "3":
            print("\n--- Deposit Funds ---")
            acc_num = input("Enter Account Number: ").strip()
            account = atm_vault.get_account(acc_num)
            
            if account != None:
                try:
                    amount = float(input("Enter Deposit Amount: ₹"))
                except ValueError:
                    print("Error: Amount must be a valid number!")
                    continue
                account.deposit(amount)
                
        elif choice == "4":
            print("\n--- Withdraw Funds ---")
            acc_num = input("Enter Account Number: ").strip()
            account = atm_vault.get_account(acc_num)
            
            if account != None:
                entered_pin = input("Enter Your PIN: ").strip()
                if account.verify_pin(entered_pin) == True:
                    try:
                        amount = float(input("Enter Withdrawal Amount: ₹"))
                    except ValueError:
                        print("Error: Amount must be a valid number!")
                        continue
                    account.withdraw(amount)
                    
        elif choice == "5":
            print("\n--- Print Bank Statement Log ---")
            acc_num = input("Enter Account Number: ").strip()
            account = atm_vault.get_account(acc_num)
            
            if account != None:
                entered_pin = input("Enter Your PIN: ").strip()
                if account.verify_pin(entered_pin) == True:
                    print(f"\n--- Statement Ledger for Account: {acc_num} ---")
                    for log in account.history:
                        print(log)
                    print("------------------------------------------")
                    
        elif choice == "6":
            print("\nUpdating security ledger file logs...")
            atm_vault.save_accounts()
            print("ATM Connection closed safely. Thank you!")
            break
            
        else:
            print("Invalid selection! Please enter a valid number between 1 and 6.")

if __name__ == "__main__":
    main()