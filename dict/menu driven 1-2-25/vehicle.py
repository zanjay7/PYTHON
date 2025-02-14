def add_vehicle(vehicle):
    name = input("Enter Vehicle name: ")
    tyre = input("Enter Number Of tyres: ")
    price = int(input("Enter the Price of Vehicle: "))
    vehicle[name] = {"No.Of Tyers": tyre, "price": price}
    print(f"Vehicle '{name}' added to the Garage.")

def display_vehicles(vehicle):
    if not vehicle:
        print("No vehicles in the garage.")
    else:
        for name, details  in vehicle.items():
            print(f"{name}\n No.of Tyres:{details["No.Of Tyers"]}\n Price:{details["price"]}INR")

def display_by_tyres(vehicle):
    tyres = input("Enter the number of tyres to filter: ")
    
    if details in vehicle:
        tyres==tyres
        for name, details in vehicle.items():
            print(f"{name}\n No.of Tyres:{details["No.Of Tyers"]}\n Price:{details["price"]}INR")
    else:
        print("\nNo vehicles found with that number of tyres.")


vehicle={}

while True:
    print("\nVehicle Management System")
    print("1. Add Vehicle")
    print("2. Display all Vechicles")
    print("3. Display by Number of Tyres")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_vehicle(vehicle)
    
    elif choice == "2":
        display_vehicles(vehicle)
        
    elif choice == "3":
        display_by_tyres(vehicle)
        
    elif choice == "4":
        break
    else:
        print("Invalid Choice!")
    