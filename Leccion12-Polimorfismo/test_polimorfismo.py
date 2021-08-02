from Employee import Employee
from Manager import  Manager

def print_detail(obj):
    print(obj)
    print(type(obj))


employee = Employee('Pepe', 5000)
print_detail(employee)

manager = Manager('Karla', 5000, 'Sistemas')
print_detail(manager)

