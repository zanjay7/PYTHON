car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car)
x=car.values()
y=car.keys()
print(x,y)
car["brand"]="Toyota"
print(car)
car["Color"]="Black"
print(car)
z=car.items()
car.update({"year":2000})
print(car)
n=int(input("Enter the range: "))
x={}
for i in range(n):
    key=input("Enter the Key: ")
    value=input("Enter the values: ")
    x[key]=value
print(x)