import temp1

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        temp = float(input("Enter the temperature in Celsius: "))
        print(f"{temp}°C is {temp1.far(temp):.2f}°F")

    elif choice == "2":
        temp = float(input("Enter the temperature in Fahrenheit: "))
        print(f"{temp}°F is {temp1.cel(temp):.2f}°C")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
