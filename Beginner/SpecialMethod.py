#object oriented programming
class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay
    def __repr__(self) :
        return f"Employee ({self.first}, {self.last}, {self.pay})"
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    def __add__(self, other):
        return self.pay + other.pay
    def __len__ (self):
        return len(self.fullname())
emp1 = Employee("Thanh", "La", 1000)
emp2 = Employee("Thanh", "Dep Trai", 500)


   