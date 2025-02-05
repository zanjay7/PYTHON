rooms = {}

while True:
    print("\nRoom Booking System")
    print("1. Book Room")
    print("2. Cancel Booking")
    print("3. View All Rooms")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
       
        room_no = input("Enter the Room no: ")
        
        if room_no in rooms:
            print("Room Already occupied!")
        else:
            name = input("Enter name: ")
            date = input("Enter Due Date as DD.MM.YYYY: ")
            rooms[room_no] = {'name': name, 'date': date}
            print("Room Assigned successfully!")
    elif choice == "2":
        room_no = input("Enter the Room no: ")
        if room_no in rooms:
            del rooms[room_no]
            print("Room cancelled successfully!")
        else:
            print("Room Not Found!")
        
    elif choice == "3":
        if not rooms:
            print("No Rooms available.")
        else:
            print("\nRoom Records:")
            for room_no, details in rooms.items():
                print(f"Name: {details['name']}, Room No: {room_no}, Date: {details['date']}")
                
    elif choice == "4":
        break
