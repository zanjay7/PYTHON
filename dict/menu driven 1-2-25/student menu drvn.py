students = {}

while True:
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Search Student")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        if roll_number in students:
            print("Student with this roll number already exists!")
        else:
            students[roll_number] = {'name': name, 'marks': marks}
            print("Student added successfully!")
    
    elif choice == "2":
        roll_number = input("Enter roll number to update marks: ")
        if roll_number in students:
            new_marks = float(input("Enter new marks: "))
            students[roll_number]['marks'] = new_marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")
    
    elif choice == "3":
        roll_number = input("Enter roll number to delete: ")
        if roll_number in students:
            del students[roll_number]
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    
    elif choice == "4":
        if not students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for roll_number, student in students.items():
                print(f"Roll Number: {roll_number}, Name: {student['name']}, Marks: {student['marks']}")
    
    elif choice == "5":
        roll_number = input("Enter roll number to search: ")
        if roll_number in students:
            student = students[roll_number]
            print(f"Found Student - Roll Number: {roll_number}, Name: {student['name']}, Marks: {student['marks']}")
        else:
            print("Student not found!")
    
    elif choice == "6":
        print("Exiting the program")
        break
