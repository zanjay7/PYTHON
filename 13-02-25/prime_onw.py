import prime

while True:
    print("\n1.Check Weather a no is prime")
    print("2.Print Prime nos upto the given no")
    
    choice=input("Enter the choice: ")
    
    if choice == "1":
        
        x=int(input("Enter the Number:"))

        print(prime.prime_no(x))
        
    if choice == "2":
        
        x=int(input("Enter the Number:"))

        print(prime.prime_series(x))