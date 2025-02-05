def sum_of_list(lst):
    sum=0
    for i in lst:
        sum=sum+i
        
    print(sum)
lst=[]
n=int(input("Enter the range of the list;"))
for i in range(n):
    li=int(input("Enter the list:"))
    lst.append(li)
sum_of_list(lst)
    