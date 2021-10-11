#object oriented programming
class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay
class Developer(Employee):
    co_salary = 1.02
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang
    
class Manager(Employee):
    co_salary = 1.5
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employess = []
        else:
            self.employess = employees
    def add_employee(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)
    def remove_employee(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)
    def print_emp(self):
        for emp in self.employess:
            print('-->', emp.fullname())
class Secretary(Employee):
    co_salary = 1.05
    def __init__(self, first, last, pay, job):
        super().__init__(first, last, pay)
        self.job = job

dev1 = Developer("Thanh", "La", 400, "Python")
dev2 = Developer("Thanh", "Deptrai", 500, "C++")
sec1 = Secretary('Ngoc', 'Trinh', 600, 'Eat with manager')
man1 = Manager('Trump', 'Donal', 1000,[dev1, dev2])
man1.remove_employee(dev1)
man1.add_employee(sec1)
man1.print_emp()