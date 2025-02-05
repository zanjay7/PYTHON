str=input("Enter the String: ")

# x=str[::-1]

# if str==x:
#     print(f"{str} is Palindrome")
    
# else:print(f"{str}Not palindrome")
s=""
for i in str:
    s=i+s
if s==str:
    print("Is palindrome")
    
else:print("Not palindrome")