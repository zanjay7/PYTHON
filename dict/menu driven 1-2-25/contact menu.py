contact={}

while True:
    print("\1.Add a contact")
    print("2.Search a Contact by the name")
    print("3.Display all contact")
    print("4.Delete a contact by name")
    print("5.Exit the program")
    
    choice=input("Enter the choice:")
    
    if choice == "1":
        name=input("Enter the name of the contact:")
        number=input("Enter the mob.number:")
         