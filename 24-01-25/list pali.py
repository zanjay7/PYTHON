num=int(input("Enter the range:"))
list=[]
for i in range(num):
    li=input("Enter the list: ")
    list.append(li)
print(list)
if list==list[::-1]:
    print("pali")
else:print("not")