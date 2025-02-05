list=["sanjay","sreethul",1,2,3]
n=int(input("Enter the range:"))
for i in range(n):
    x=input("Enter the elements")
    
    # list.append(x)
    list[1]=2
    list.extend("sanjay")
    list.pop(2)
    # list.clear()
    # del list

print(list)