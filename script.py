class Employee:
    num_employee = 0
    annual_rate = 0.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@carlos.com'

        Employee.num_employee += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def pay_rate(self):
        return Employee.annual_rate * self.pay


    @classmethod
    def rate_new_pay(cls, amount):
        cls.annual_rate = amount


    @classmethod
    def from_name(cls, emp_new):
        first, last, pay = emp_new.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developers(Employee):

    def __init__(self,first, last, pay, lenguage):
        super().__init__(first, last, pay)
        self.lenguage = lenguage


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






