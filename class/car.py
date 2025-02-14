class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def info(self):
        print(self.brand,self.model,self.year)
        
car1=car("Ford","Mustang GT",1947)
car2=car("Ford","Shelby",1969)
car3=car("Ford","Mustang",1945)

car1.info()
car2.info()
car3.info()
        