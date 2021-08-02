from Employee import Employee


class Manager(Employee):

    def __init__(self, name, sueldo, depto):
        super().__init__(name, sueldo)
        self.depto = depto


    def __str__(self):
        return f'Gerente[ Depto: { self.depto } ] { super().__str__()}'



