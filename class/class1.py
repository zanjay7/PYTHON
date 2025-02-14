# class emplo:
    
#     name="sanjay"
#     id=10
    
#     def display(self):
#         print(self.name,self.id)
        
# p1=emplo()
# p1.display()

class emplo:
    def __init__(self,name,id,age):
        
        self.name=name
        self.id=id
        self.age=age
    
    def display(self):
        print(self.name,self.id,self.age)
        
p1=emplo("Sanjay",10,20)
p2=emplo("SANJAY",11,23)
# p1.display()
# p2.display()

print(getattr(p1,"name"))

setattr(p1,"id",30000)
print(getattr(p1,"id"))

print(hasattr(p2,"id"))
