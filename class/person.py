class Person:
    def __init__(self,name,age,gender):
        
        self.name=name
        self.age=age
        self.gender=gender
    def display_details(self):
        print(self.name,self.gender,self.age)
        
person1=Person("SANJAY",23,"male")

person2=Person("SANJAY",26,"male")

person1.display_details()
person2.display_details()
        
    