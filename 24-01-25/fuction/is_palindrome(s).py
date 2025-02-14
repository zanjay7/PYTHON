def is_palindrome(s):
    str=""
    for i in s:
        str=i+str
    if s==str:
        print("Is palindrome")
        
    else:print("Not palindrome")
    
# s=input("Enter the string: ")

# is_palindrome(s)