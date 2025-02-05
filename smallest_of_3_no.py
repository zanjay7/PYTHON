num1=float(input("Enter the first number: "))
num2=float(input("Enter the Second number: "))
num3=float(input("Enter the Third number: "))

if num1<=num2 and num1<=num3:
    smallest_num=num1

elif num2<=num1 and num2<=num3:
    smallest_num=num2
else:
    smallest_num=num3
    
print("smallest number is: ",smallest_num)    


