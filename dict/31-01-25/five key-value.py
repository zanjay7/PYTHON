n=int(input("Enter the range of key values:"))
x={}
for i in range(n):
    key=input("Enter the Key: ")
    value=input("Enter the values: ")
    x[key]=value
y=x.keys()
print(y)
print(x)