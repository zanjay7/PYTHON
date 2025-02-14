book={}
while True:
    print("\nLibrary management system ")
    print("1. Add books")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Exit")
    choice = input("enter the choice : ")
    if choice=="1":
        isbn=input("enter the isbn number : ")
        if isbn in book:
            print("!! This book already exists !!")
        else:
            title = input ("Enter the name of book : ")
            author = input("Enter the Author name : ")
            book[isbn]={"title":title, "author":author, "isbn":isbn}
            print("!! Book added successfully !!")
    elif choice=="2":
        print("List of all books")
        print(book)
    elif choice=="3":
        isbn=input("enter the isbn number : ")
        if isbn in book:
            print("\nBook name : ",title)
            print("Author name : ",author)
            print("isbn number : ",isbn)
        else:
            print("!! The book not exists !!")
    elif choice == "4":
        isbn = input("Enter the ISBN number: ")
        if isbn in book:
            del book[isbn]
            print("!! The book is removed !!")
        else:
            print("!! The book does not exist !!")

    elif choice=="5":
        print("!! Exiting the program !!")
        break
    else:
        print("invalid choice")