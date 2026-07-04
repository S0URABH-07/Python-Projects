import json
import os
from src.book import Book

class Library:
    def __init__(self, file_path):
        self.file_path = file_path
        self.books = {}
        
        # Load your inventory file instantly when the library starts
        self.load_inventory()

    def load_inventory(self):
        """Reads stored book configurations from the JSON database."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                raw_data = json.load(file)
                
                # Loop through the raw storage to build real Book objects
                for book_id, info in raw_data.items():
                    saved_book = Book(
                        book_id=book_id,
                        title=info["title"],
                        author=info["author"],
                        is_borrowed=info["is_borrowed"]
                    )
                    # Store the reconstructed object back into our operational ledger
                    self.books[book_id] = saved_book
        else:
            self.books = {}

    def save_inventory(self):
        """Saves current runtime library objects back to the storage disk."""
        output_dictionary = {}
        
        # Convert our objects back to flat standard dictionaries for JSON storage
        for book_id, book_object in self.books.items():
            output_dictionary[book_id] = book_object.to_dict()
            
        with open(self.file_path, "w") as file:
            json.dump(output_dictionary, file, indent=4)
        print("Library database backup successful!")

    def add_book(self, book_id, title, author):
        """Adds a completely new book entry to the library collection."""
        if book_id in self.books:
            print("Error: A book entry with this ID asset code already exists!")
            return False
            
        # Instantiate a new book object. By default, it will be marked as available (False)
        new_book = Book(book_id, title, author)
        self.books[book_id] = new_book
        print(f"Book '{title}' successfully registered to inventory.")
        return True

    def display_all_books(self):
        """Prints out the complete status logs of all library assets."""
        if len(self.books) == 0:
            print("The library catalog is currently empty.")
            return
            
        print("\n--- Current Library Inventory Catalog ---")
        for book_id, book_object in self.books.items():
            print(book_object)
        print("------------------------------------------\n")

    def issue_book(self, book_id):
        """Processes a checkout request, moving status to borrowed."""
        if book_id in self.books:
            book_object = self.books[book_id]
            # Call the inner function we wrote in Phase 2
            if book_object.borrow_book():
                print(f"Success: '{book_object.title}' has been checked out.")
                return True
        else:
            print("Error: Book asset ID not found in catalog logs.")
            return False

    def receive_return(self, book_id):
        """Processes a check-in request, returning book status to shelf."""
        if book_id in self.books:
            book_object = self.books[book_id]
            # Call the return function we wrote in Phase 2
            if book_object.return_book():
                print(f"Success: '{book_object.title}' returned safely to the shelf.")
                return True
        else:
            print("Error: Book asset ID not found in catalog logs.")
            return False