accounts={}
while True:
    print("\nBank Account Management Menu:")
    print("1. Create Account")
    print("2. Display Account Details")
    print("3. Deposit Money")
    print("4. withdraw Money")
    print("5. Delete Account")
    print("6. Exit")
    choice=int(input("Enter your Choice between 1-6:"))
    
    if choice == 1:
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            print("\n Account already exists!")
            
        else:
            name = input("Enter account holder's name: ")
            balance = int(input("Enter initial balance: "))
            accounts[acc_number] = {"name": name, "balance": balance}
            print("Account created successfully!")
            
            
    elif choice == 2: 
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            print("\nAccount Details:")
            print("Account Number:", acc_number)
            print("Account Holder:", accounts[acc_number]["name"])
            print("Balance:", accounts[acc_number]["balance"])
        else:
            print("Account not found!")
    elif choice==3:
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            amount=int(input("Enter the Amount to Deposit:"))
            if amount>0:
                accounts[acc_number]['balance']+=amount
                print("Amount Deposited Successfully!")
                print("New Account Balance:",accounts[acc_number]["balance"])
            elif amount<=0:
                print("\nEnter A Valid amount!")
        else:
            print("\nEnter A Valid Account no!")       
            
    elif choice==4:
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            with_amount=int(input("Enter the Amount to Withdraw:"))
            if with_amount>0:
                accounts[acc_number]['balance']-=with_amount
                print("Amount Withdrawed Successfully!")
                print("New Account Balance:",accounts[acc_number]['balance'])
            elif with_amount<=0:
                print("\nEnter A Valid amount!")
        else:
            print("\nEnter A Valid Account no!")       

    elif choice==5:
        acc_number = input("Enter account number: ")
        if acc_number in accounts:
            del accounts[acc_number]
            print("Deleted Your Account Successfully!")
        else:
            print("Enter A Valid Account No!")
    
    elif choice==6:
        break