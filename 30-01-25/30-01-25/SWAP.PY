# x={1, 2, 3, 4, 5}
# y={3, 4, 5, 6, 7}
# x=list(x)
# y=list(y)
# x1=x[:]
# y1=y[:]
# x.clear()
# y.clear()
# for i in x1:
#     y.append(i)

# for i in y1:
#     x.append(i)
# x=set(x)
# y=set(y)
# print(x)
# print(y)
# x.update(y)
# y.symmetric_difference_update(x)
# x.symmetric_difference_update(y)
# print(x)
# print(y)

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}


set1, set2 = set2, set1

print("Set 1 after swap:", set1)
print("Set 2 after swap:", set2)



    