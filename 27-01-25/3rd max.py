n = int(input("Enter the length of the list: "))
lst = []
temp = []
for i in range(n):
    li = int(input("Enter the elements in the list: "))
    lst.append(li)

for i in lst:
    if i not in temp: 
        temp.append(i)

if len(temp) >= 3:
    temp.sort(reverse=True)
    print(temp[2])
else:
    print(temp[1])

print( temp)
