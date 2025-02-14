class Person:
    name="Sanjay"
    id=12
    # def display(self):
    #     print(self.name,self.id)
class student(Person):
    grade="A+"
    def display(self):
        print(self.name,self.id,self.grade)
            
Student=student()
Student.display()
