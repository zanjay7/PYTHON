num=int(input("Enter the range:"))
list=[]
n=5
repl=3
for i in range(num):
    li=int(input("Enter the ele:"))
    list.append(li)
for i in range(len(list)):
    if list[i]==3:
        list[i]=5
print(list)
