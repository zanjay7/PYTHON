library = {}

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search for a Book")
    print("4. Remove a Book")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN number: ")
        if isbn in library:
            print("A book with this ISBN already exists!")
        else:
            library[isbn] = {'title': title, 'author': author}
            print("Book added successfully!")
    
    elif choice == "2":
        if not library:
            print("No books available in the library.")
        else:
            print("\nLibrary Books:")
            for isbn, book in library.items():
                print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}")
    
    elif choice == "3":
        search_title = input("Enter book title to search: ")
        found = False
        for isbn, book in library.items():
            if book['title'].lower() == search_title.lower():
                print(f"Found Book - ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}")
                found = True
                break
        if not found:
            print("Book not found!")
    
    elif choice == "4":
        isbn = input("Enter ISBN number to remove: ")
        if isbn in library:
            del library[isbn]
            print("Book removed successfully!")
        else:
            print("Book not found!")
    
    elif choice == "5":
        print("Exiting the program!")
        break

