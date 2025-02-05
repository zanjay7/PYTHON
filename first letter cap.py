str=input("Enter the string:")
str1=str.split(" ")
temp=""
for i in range(len(str1)):
    a=str1[i]
    b=a[0].upper() +a[1:]
    temp+=b+" "
    
print(temp)
    
    
    
        
        