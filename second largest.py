n=int(input("Enter the lenght of the list:"))
list=[]
# temp=[]
for i in range(n):
    li=input("ENter the elements in the list:")
    list.append(li)
list.sort()
print(list[-2])

# for i in range(len(list)):
#     for j in range(i,(len(list))):
#         if list[i]>list[j]:
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
# print(list[-2])
