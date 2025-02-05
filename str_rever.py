x=input("Enter:")
y=input("enter2: ")

flag=1

if len(x)==len(y):
    for i in x:
        if x.count(i)!=y.count(i):
            flag=0
            break
else:
    flag=0
    
if flag==1:
    print("Ana")
    
else: print("not ana")
        