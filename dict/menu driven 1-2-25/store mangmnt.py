inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Remove Product")
    print("4. View All Products")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        if product_name in inventory:
            print("Product already exists! Use update option to modify quantity.")
        else:
            inventory[product_name] = {'quantity': quantity, 'price': price}
            print("Product added successfully!")
    
    elif choice == "2":
        product_name = input("Enter product name to update quantity: ")
        if product_name in inventory:
            new_quantity = int(input("Enter new quantity: "))
            inventory[product_name]['quantity'] = new_quantity
            print("Product quantity updated successfully!")
        else:
            print("Product not found!")
    
    elif choice == "3":
        product_name = input("Enter product name to remove: ")
        if product_name in inventory:
            del inventory[product_name]
            print("Product removed successfully!")
        else:
            print("Product not found!")
    
    elif choice == "4":
        if not inventory:
            print("No products available in the inventory.")
        else:
            print("\nInventory:")
            for product_name, details in inventory.items():
                print(f"Product: {product_name}, Quantity: {details['quantity']}, Price: {details['price']}")
    
    elif choice == "5":
        print("Exiting the program!")
        break

