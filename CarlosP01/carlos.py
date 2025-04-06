
# this is my first class called Employees.
class Employee:
    num_employee = 0
    annual_rate = 0.05

#intances.

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@carlos.com'

        Employee.num_employee += 1

#first functions to add Full Name.

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

#Function to add annual raise pay.

    def pay_rate(self):
        return Employee.annual_rate * self.pay

#This is a ClassMethod to handle the rate for the raise's annual pay

    @classmethod
    def rate_new_pay(cls, amount):
        cls.annual_rate = amount

#This is a ClassMethod to split user with dashes input.

    @classmethod
    def from_name(cls, emp_new):
        first, last, pay = emp_new.split('-')
        return cls(first, last, pay)

#This is to confer if the day is a week day.

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#this is a second Class associated with the main Class, to add a new type of employees.

class Developers(Employee):

    def __init__(self,first, last, pay, lenguage):
        super().__init__(first, last, pay)
        self.lenguage = lenguage

#this is a third Class associated with the main Class, to add a new type of employees.
#here we created functions to add, remove and print from this Class.

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())


emp4 = Developers('carlos', 'javier', 25000, 'python')
emp5 = Developers('Enna', 'Castillo', 28000, 'java')


emp1 = Manager('carlos', 'javier', 25000, [emp4])
emp2 = Manager('Enna', 'Castillo', 28000, [emp5])

#End...