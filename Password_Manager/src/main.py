# src/main.py

import os
from src.vault import PasswordVault

def display_menu():
    print("\n====== SECURE PASSWORD MANAGER ======")
    print("1. Store New Account Credentials")
    print("2. List All Secured Website Indexes")
    print("3. Retrieve Username & Password")
    print("4. Update Existing Account Password")
    print("5. Delete Account Profile From Vault")
    print("6. Secure Vault & Terminate System")
    print("=====================================")

def main():
    data_directory = "data"
    file_path = os.path.join(data_directory, "vault.json")
    
    # Establish the application database folder architecture path
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        
    # Initialize the core Password Vault security data engine
    vault_manager = PasswordVault(file_path)
    
    while True:
        display_menu()
        choice = input("Select a vault operation (1-6): ").strip()
        
        if choice == "1":
            print("\n--- Store New Credentials ---")
            website = input("Enter Website/Service Name (e.g., github.com): ").strip()
            username = input("Enter Account Username/Email: ").strip()
            password = input("Enter Secure Account Password: ").strip()
            
            if not website or not username or not password:
                print("Error: All fields are mandatory to complete configuration stage!")
                continue
                
            vault_manager.add_credential(website, username, password)
            
        elif choice == "2":
            vault_manager.display_all_sites()
            
        elif choice == "3":
            print("\n--- Credential Retrieval Lookups ---")
            website = input("Enter Website Name to query: ").strip()
            record = vault_manager.lookup_site(website)
            
            if record != None:
                print("\n--- Credentials Extracted Successfully ---")
                print(record)
                
        elif choice == "4":
            print("\n--- Update Stored Account Password ---")
            website = input("Enter target Website Name: ").strip()
            record = vault_manager.lookup_site(website)
            
            if record != None:
                new_password = input("Enter New Secure Password: ").strip()
                record.update_password(new_password)
                
        elif choice == "5":
            print("\n--- Purge Account Record From Vault ---")
            website = input("Enter Website Name to delete: ").strip()
            vault_manager.remove_site(website)
            
        elif choice == "6":
            print("\nSynchronizing runtime modifications to file storage...")
            vault_manager.save_vault()
            print("Vault file system locked successfully. Connection terminated!")
            break
            
        else:
            print("Invalid security prompt! Please input a valid menu value from 1 to 6.")

if __name__ == "__main__":
    main()