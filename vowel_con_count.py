str=input("Enter the strg: ")
count=0
temp=0
len=len(str)
for i in str:
    if i in 'aeiouAEIOU':
        count +=1   
    else: 
        temp +=1
print(temp)
print(count)