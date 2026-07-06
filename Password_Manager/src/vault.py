import json
import os
from src.credential import Credential

class PasswordVault:
    def __init__(self, file_path):
        self.file_path = file_path
        # The central dictionary structure holding all account allocations
        # Key: Website Name String, Value: Credential Object Instance
        self.credentials = {}
        
        self.load_vault()

    def load_vault(self):
        """Reads stored account credentials from the private JSON vault file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                raw_data = json.load(file)
                
                # Loop through the raw dictionary to rebuild real Credential objects
                for website, info in raw_data.items():
                    saved_credential = Credential(
                        website=website,
                        username=info["username"],
                        password=info["password"]
                    )
                    # Bind the object back under its master website key split
                    self.credentials[website] = saved_credential
        else:
            self.credentials = {}

    def save_vault(self):
        output_dictionary = {}
        
        # Re-compile our operational class objects back into standard nested dictionaries
        for website, cred_object in self.credentials.items():
            output_dictionary[website] = cred_object.to_dict()
            
        with open(self.file_path, "w") as file:
            json.dump(output_dictionary, file, indent=4)
        print("Vault file system synchronized and written securely.")

    def add_credential(self, website, username, password):
        """Registers a completely new account credential entry to the vault."""
        # Normalize the website input immediately for duplicate checking
        clean_site = website.strip().lower()
        
        if clean_site in self.credentials:
            print(f"Error: A login profile for '{clean_site}' already exists in this vault!")
            return False
            
        # Create and cache the fresh credential object asset
        new_cred = Credential(clean_site, username, password)
        self.credentials[clean_site] = new_cred
        print(f"Credentials for '{clean_site}' successfully staged to vault.")
        return True

    def display_all_sites(self):
        """Lists out all website names currently secured inside the storage manager."""
        if len(self.credentials) == 0:
            print("The password vault is currently completely empty.")
            return
            
        print("\n--- Secured Website Indexes ---")
        for index, website in enumerate(self.credentials.keys(), 1):
            print(f"{index}. {website}")
        print("--------------------------------\n")

    def lookup_site(self, website):
        """Fetches and reveals the account record for a specific requested service."""
        clean_site = website.strip().lower()
        
        if clean_site in self.credentials:
            return self.credentials[clean_site]
        else:
            print(f"Error: No credentials found for website '{clean_site}'.")
            return None

    def remove_site(self, website):
        """Deletes an account credential structure completely from your dictionary ledger."""
        clean_site = website.strip().lower()
        
        if clean_site in self.credentials:
            self.credentials.pop(clean_site)
            print(f"Success: Account profile for '{clean_site}' has been wiped from local cache.")
            return True
        else:
            print(f"Error: Target site '{clean_site}' not found inside vault registry.")
            return False