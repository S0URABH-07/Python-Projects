import os
from src.library import Library

def display_menu():
    """Prints out the interactive options layout for the library terminal."""
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add New Book Asset")
    print("2. Display Inventory Catalog")
    print("3. Issue Book (Checkout)")
    print("4. Return Book (Check-in)")
    print("5. Save Progress & Exit")
    print("=======================================")

def main():
    # Setup data directory configuration paths
    data_directory = "data"
    file_path = os.path.join(data_directory, "library.json")
    
    # Verify the local storage architecture path exists
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        
    # Boot up the Library control system engine
    library_system = Library(file_path)
    
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Register New Book Asset ---")
            book_id = input("Enter Book Unique ID/ISBN: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            
            # Send input directly to the engine
            library_system.add_book(book_id, title, author)
            
        elif choice == "2":
            library_system.display_all_books()
            
        elif choice == "3":
            print("\n--- Process Book Checkout ---")
            book_id = input("Enter Book ID to issue: ").strip()
            library_system.issue_book(book_id)
            
        elif choice == "4":
            print("\n--- Process Book Return ---")
            book_id = input("Enter Book ID to return: ").strip()
            library_system.receive_return(book_id)
            
        elif choice == "5":
            library_system.save_inventory()
            print("System shutdown complete. Goodbye!")
            break  # Shuts down the infinite system loop
            
        else:
            print("Invalid system command selection! Please input a value from 1 to 5.")

if __name__ == "__main__":
    main()