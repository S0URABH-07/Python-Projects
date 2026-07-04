class Book:
    def __init__(self, book_id, title, author, is_borrowed=False):
        # Setting up the core variables for an individual book
        self.book_id = book_id
        self.title = title
        self.author = author
        
        # Simple boolean state: True means borrowed, False means available on the shelf
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        """Changes the book state to borrowed if it is available."""
        if self.is_borrowed == True:
            print("Sorry, this book is already borrowed by someone else!")
            return False
        else:
            self.is_borrowed = True
            return True

    def return_book(self):
        """Changes the book state back to available."""
        if self.is_borrowed == False:
            print("This book is already sitting safely on the shelf!")
            return False
        else:
            self.is_borrowed = False
            return True

    def to_dict(self):
        """Converts the book object data into a simple dictionary for JSON saving."""
        book_dictionary = {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }
        return book_dictionary

    def __str__(self):
        """Prints a clean status line for the user to see in the terminal."""
        if self.is_borrowed == True:
            status = "Borrowed"
        else:
            status = "Available"
            
        return f"ID: {self.book_id} | Title: '{self.title}' | Author: {self.author} | Status: [{status}]"