class Person:
    # similar a un constructor
    def __init__(self, n, a, e):
        self.nombre: str = n
        self.apellido: str = a
        self.edad: int = e

    def describe(self):
        return {
            'Nombre' : self.nombre,
            'Apellido': self.apellido,
            'Edad': self.edad
        }

person1 = Person('Juan', 'Ramos', 22)

print(person1.describe())