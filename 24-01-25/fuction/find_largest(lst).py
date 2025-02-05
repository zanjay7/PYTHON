def find_largest(lst):
    temp=0
    for i in lst:
        if i>=temp:
            temp=i
        
    print(temp)
lst=[]
n=int(input("Enter the range of the list:"))
for i in range(n):
    li=int(input("Enter the list:"))
    lst.append(li)
find_largest(lst)
    