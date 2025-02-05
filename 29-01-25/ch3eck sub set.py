x=set()
y=set()
n1=int(input("Enter the first range of x:"))
for i in range(n1):
    x1=input("Enter the elements: ")
    x.update(x1)
n2=int(input("Enter the second range of y:"))
for i in range(n2):
    y1=input("Enter the elements: ")
    y.update(y1)
x2=list(x)
y2=list(y)
l1=len(x2)
l2=len(y2)
set1=[]
if l1>=l2:
    for i in x2:
        for j in y2:
            if j==i:
                set1.append(j)
    if set1==y2:
        print("It is a sub set")
    else:print("not a sub set")
else:print("Enter it correctly")
                
    