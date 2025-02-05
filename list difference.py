x=[1,2,3,4,5,6,7,8]
y=[2,4,5,6,7]
copyy=x[:]
for i in copyy:
    for j in y:
        if i==j:
            x.remove(i)
print(x)
