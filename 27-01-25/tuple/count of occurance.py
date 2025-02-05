x=[]
count=0
num=int(input("enetr : "))
for i in range(num):
    li=int(input("Enter the ele: "))
    x.append(li)
spe=int(input("Enter the ele:"))
a=tuple(x)
# for i in range(num):
#     if a[i]==spe:
#         count+=1
# print(count)
x=a.count(spe)
print(x)