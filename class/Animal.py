class Animal:
    def info(self):
        print("All animals can speak!")
        
class Dog(Animal):
    def info(self):
        print("Dog Always Bark!")
        
class Cat(Animal):
    def info(self):
        print("Cat Always Meows!")
        
cat=Cat()
dog=Dog()




cat.info()
dog.info()