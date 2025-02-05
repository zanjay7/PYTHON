def reverse_string(s):
    temp=""
    for i in s:
        temp=i+temp
    print(temp)
    
s=input("Enter the string to be reversed:")

reverse_string(s)

