class Book:
    def __init__(self, title, author):
        """Initialize the book with title, author, and availability status (True for available)."""
        self.title = title
        self.author = author
        self.availability = True  # Book is available by default

    def check_out(self):
        """Marks the book as checked out (not available)."""
        if self.availability:
            self.availability = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        """Marks the book as returned and available."""
        if not self.availability:
            self.availability = True
            print(f"'{self.title}' has been returned and is now available.")
        else:
            print(f"'{self.title}' is already available.")

    def display_info(self):
        """Displays the book's title, author, and availability."""
        availability_status = "Available" if self.availability else "Checked out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {availability_status}")


class Library:
    def __init__(self):
        """Initialize an empty list to store books."""
        self.books = []

    def add_book(self, title, author):
        """Adds a new book to the library."""
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"'{title}' by {author} has been added to the catalogue.")

    def view_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("No books available in the catalogue.")
        else:
            print("\nLibrary Catalogue:")
            for book in self.books:
                book.display_info()

    def search_book(self, title):
        """Searches for a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book with title '{title}' not found.")
        return None


def main():
    # Create a new Library instance
    library = Library()

    # Add books to the library
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # View all books in the library
    library.view_books()

    # Check out a book
    book_to_check_out = library.search_book("1984")
    if book_to_check_out:
        book_to_check_out.check_out()

    # Try to check out the same book again
    if book_to_check_out:
        book_to_check_out.check_out()

    # Return the book
    if book_to_check_out:
        book_to_check_out.return_book()

    # View books again after return
    library.view_books()

    # Search for a book that doesn't exist
    library.search_book("The Catcher in the Rye")

    # Add a new book and view the catalogue
    library.add_book("The Catcher in the Rye", "J.D. Salinger")
    library.view_books()


# Run the program
if __name__ == "__main__":
    main()
