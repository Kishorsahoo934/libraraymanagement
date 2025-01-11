import json

class Book:
    def __init__(self, title, author, status=True):
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        # """Convert Book object to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "status": self.status
        }

    #@staticmethod
    def from_dict(data):
        # """Convert dictionary to Book object."""
        return Book(data["title"], data["author"], data["status"])


class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = []  
        self.load_data()

    def load_data(self):
        # """Load library data from a file."""
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
                print("Library data loaded successfully.")
        except FileNotFoundError:
            print("No existing library data found. Starting fresh.")
        except json.JSONDecodeError:
            print("Error reading library data. Starting fresh.")

    def save_data(self):
        """Save library data to a file."""
        with open(self.filename, "w") as file:
            data = [book.to_dict() for book in self.books]
            json.dump(data, file, indent=4)
            print("Library data saved successfully.")

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.status:
                book.status = False
                print(f"You have borrowed '{title}'.")
                return
        print(f"'{title}' is not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.status:
                book.status = True
                print(f"Book '{title}' has been returned.")
                return
        print(f"'{title}' was not borrowed from this library.")

    def display_books(self):
        print("\nBooks in the Library:")
        for book in self.books:
            status = "Available" if book.status else "Borrowed"
            print(f"'{book.title}' by {book.author} - {status}")


# Main Program
library = Library()

while True:
    print("\n--------------------------- Library Management System ---------------------------")
    print("1. Add Book to the Library")
    print("2. Borrow Book from the Library")
    print("3. Return Book to the Library")
    print("4. Display All Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            new_book = Book(title, author)
            library.add_book(new_book)
        case 2:
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        case 3:
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        case 4:
            library.display_books()
        case 5:
            library.save_data()
            print("Exiting the system. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
