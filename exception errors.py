x= int(input("Enter the number:"))
y=int(input("Enter the number:"))

try:
    result=x/y
    print(result)
    
except ZeroDivisionError:
    
    print("Zero")
    
