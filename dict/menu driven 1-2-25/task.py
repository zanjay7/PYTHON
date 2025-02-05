task = {}

while True:
    print("\nInventory Management System")
    print("1. Add Task")
    print("2. Remove task ")
    print("3. View All TAsk")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        t_name = input("Enter Task name: ")
        Priority = input("Enter the Priority of task as 1-5 rating: ")
        Due = input("Enter Due Date as DD.MM.YYYY: ")
        if t_name in task:
            print("Task Already Exists!")
        else:
            task[t_name] = {'name': t_name, 'due': Due, 'priority':Priority}
            print("Task added successfully!")
    elif choice=="2":
        t_name = input("Enter Task name: ")
        if t_name in task:
            del task[t_name]
            print("Task Removed Succesfully!")
        else: print("Task Not Found!")
        
    elif choice == "3":
        if not task:
            print("No Task records available.")
        else:
            print("\nTask Records:")
            for t_name, task in task.items():
                print(f"Task Name: {t_name}, Name: {task['name']}, Due Date: {task['due']},Priority: {task['priority']}")
                
    elif choice=="4":
        break
    