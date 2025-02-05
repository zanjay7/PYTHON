str1=input("Enter the string1: ")

count=0

for i in str1:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        count+=1
print(count)
