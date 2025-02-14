class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed the book '{self.name}'")
        else:
            print(f"Sorry, the book '{self.name}' is already borrowed.")

    def returnit(self):
        if not self.available:
            self.available = True
            print(f"You have returned the book '{self.name}'")
        else:
            print(f"The book '{self.name}' was not borrowed.")
            
def display(library):
    if not library:
        print("No books available in the library.")
    else:
        print("\nLibrary Books:")
        for book in library.values():
            status = "Available" if book.available else "Borrowed"
            print(f"Title: {book.name}, Author: {book.author}, Status: {status}")


library = {}

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Borrow")
    print("4. Return")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        
        if title in library:
            print("Book already exists in the library!")
        else:
            library[title] = Book(title, author)
            print(f"Book '{title}' added successfully!")

    elif choice == "2":
        display()
        
        
    
    elif choice == "3":
        search_title = input("Enter book title to borrow: ")
        if search_title in library:
            library[search_title].borrow()
        else:
            print("Book not found!")

    elif choice == "4":
        search_title = input("Enter book title to return: ")
        if search_title in library:
            library[search_title].returnit()
        else:
            print("Book not found!")

    elif choice == "5":
        print("Exiting the program!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
