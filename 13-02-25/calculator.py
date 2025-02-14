while True:
    print("\n1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    
    choice=input("\nEnter your Operation:")
    
    if choice == "1":
        import cal
        a=int(input("\nEnter the First Number:"))
        b=int(input("\nEnter the second Number:"))
        print(f"\nThe Sum of {a}+{b}:",cal.add(a,b))
        
    elif choice == "2":
        import cal
        a=int(input("\nEnter the First Number:"))
        b=int(input("\nEnter the second Number:"))
        print(f"\nThe Diff of {a}-{b}:",cal.sub(a,b))
        
    elif choice == "3":
        import cal
        a=int(input("\nEnter the First Number:"))
        b=int(input("\nEnter the second Number:"))
        print(f"\nThe Product of {a}*{b}:",cal.multi(a,b))
        
    elif choice == "4":
        import cal
        a=int(input("\nEnter the First Number:"))
        b=int(input("\nEnter the second Number:"))
        print(f"\nThe  of {a}/{b}:",cal.div(a,b))
    
    
    else:
        print("Enter a valid Choice!")    
    