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
flag=0
for i in x2:
    for j in y2:
        if i==j:
            flag=1
if flag!=0:
    print("its join")
else:print("its dis join")

                
    