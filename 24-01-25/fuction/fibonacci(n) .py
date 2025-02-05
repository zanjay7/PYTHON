def fibonacci(n):
    a=0
    b=1
    for i in range(n+1):
        print(a)
        a,b=b,a+b
        


n=int(input("Enter the no: "))

fibonacci(n)