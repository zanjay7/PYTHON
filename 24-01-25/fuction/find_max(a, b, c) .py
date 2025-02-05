def find_max(a, b, c):
    if a>b and a>c:
        print(f"a= {a} is the largest")
    elif b>a and b>c:
        print(f"b= {b} is the largest")
    else:
        print(f"c= {c} is the largest")
        
a=int(input("Enter the First number:"))
b=int(input("Enter the Second number:"))
c=int(input("Enter the Third number:"))

find_max(a, b, c)
