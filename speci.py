x = [1, 10, 3, 4, 5, 6, 7, 8, 10, 10]
y = int(input("Enter the element to search: "))
flag = 0

for i in x:
    if y==i:
        flag+=1

if flag!=0:
    print(flag)
else:
    print("no")
    
