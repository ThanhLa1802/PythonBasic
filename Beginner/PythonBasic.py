#object oriented programming
class Car():
    tax = 1
    car_number = 0
    def __init__(self, brand, model, founded_year, price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
        Car.car_number += 1
    
    #regular method
    def GetValue(self):
        return (self.price * self.tax)
    
    @classmethod
    def set_tax(cls):
        cls.tax = 1.5
        
    @classmethod
    def from_string(cls, car_string):
        brand, model, founded_year, price = car_string.split('-')
        founded_year = int(founded_year)
        price = int(price)
        return cls(brand, model, founded_year, price)
    
    @staticmethod
    def check_price(price):
        if price <= 1000:
            return "This car is cheap!"
        else:
            return "This car is expensive!"


car_temp = "Toyota-Camry-1969-1200"
car_1 = Car("Vinfast","LuxA", 2017, 1000)
car_2 = Car("BMW",'i320', 1916, 700)
car_3 = Car.from_string(car_temp)
for  x in range(1,10):
    print(x)