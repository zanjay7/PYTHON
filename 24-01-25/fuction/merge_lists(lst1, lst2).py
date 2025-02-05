def merge_lists(lst1, lst2):
    lst3=[]
    for i in lst1:
        for j in lst2:
            lst3=lst1+lst2
            
    print(lst3)
        
lst1=[]
n1=int(input("Enter the range of the list:"))
for i in range(n1):
    li1=int(input("Enter the list:"))
    lst1.append(li1)


lst2=[]
n2=int(input("Enter the range of the list:"))
for i in range(n2):
    li2=int(input("Enter the list:"))
    lst2.append(li2)
merge_lists(lst1, lst2)