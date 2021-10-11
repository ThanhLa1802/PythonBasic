#object oriented programming
class Car:  
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @property
    def fullname(self):
        return f'{self.brand} {self.model}'
    
    @fullname.setter
    def fullname(self, full_name):
        brand, model = full_name.split(" ")
        self.brand = brand
        self.model = model

    @fullname.deleter
    def fullname(self):
        self.brand = None
        self.model = None
        print("Deleted fullname!")

car = Car("Vinfast", "Lux A 2.0")
print(car.fullname)
car.fullname = "BMW i320"
print(car.brand)
print(car.model)
del car.fullname
print(car.brand, car.model)

   