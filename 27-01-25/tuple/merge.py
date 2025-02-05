tuple1=("apple","banana","mango","pappaya","cherry")
tuple2=("apple","banana","mango","pappaya","cherry")
# list1=list(tuple1)
# list2=list(tuple2)
# list1.extend(list2)
# tuple3=tuple(list1)

tuple3=(*tuple1,*tuple2)
print(tuple3)