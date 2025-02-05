str=input("Enter the String of digits: ")
count=0
temp=0
for i in str:
    if i in '1234567890':
        count+=1
    else:
        temp+=1
print(count)
print(temp)
        