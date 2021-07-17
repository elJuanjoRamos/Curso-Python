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
    def set_nombre(self, n):
        self.nombre = n
    def set_edad(self, e):
        self.edad = e
    def set_apellido(self, a):
        self.apellido = a

    def get_nombre(self):
        return self.nombre



