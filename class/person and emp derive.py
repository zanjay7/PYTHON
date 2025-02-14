class Person:
    def __init__(self,name,age,gender):
        
        self.name=name
        self.age=age
        self.gender=gender
        
class employe:
    def __init__(self,id,salary):
        self.id=id
        self.salary=salary
        
class Manager(Person,employe):
    def __init__(self, name, age, gender,id,salary,department):
        Person.__init__(self,name, age, gender)
        employe.__init__(self,id,salary)
        self.department=department
    def display(self):
        print(f"name :{self.name}")
        print(self.name,self.age, self.gender,self.id,self.salary,self.department)
        
person1=Manager("Sanjay",12,"male",10,10000,"Electronics")

person1.display()
        
