def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    print(f"{fac}")
    
n=int(input("Enter the range: "))

factorial(n)    