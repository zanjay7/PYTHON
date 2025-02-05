str=input("Enter the string:")
numeric=""

for i in str:
    if i in '1234567890':
        numeric+=i
print(numeric)
print(str)
        