class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


employee_1 = Employee('David', 'olatoye', 500000)
employee_2 = Employee('Isreal', 'Fasina', 500000)
employee_3 = Employee('Precious', 'Lois', 800000)
employee_4 = Employee('Kimberly', 'Mojoyinola', 800000)

print(employee_1.email)
print(employee_2.email)
print(employee_3.email)
print(employee_4.email)
print(employee_1.fullname())
print(Employee.fullname(employee_4))

