class Employee:

    def __init__(self, name, sueldo):
        self.name = name
        self.sueldo = sueldo

    def __str__(self):
        return f'Employee: [ Name: {self.name}, Sueldo: { self.sueldo } ]'

