class Person:
    # similar a un constructor
    def __init__(self, n, a, e):
        self._nombre: str = n
        self._apellido: str = a
        self._edad: int = e

    def describe(self):
        return {

            'Nombre' : self._nombre,
            'Apellido': self._apellido,
            'Edad': self._edad

        }

    # gets
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return  self._apellido

    @property
    def edad(self):
        return self._edad
    # sets
    @nombre.setter
    def nombre(self, n):
        self._nombre = n

    @apellido.setter
    def apellido(self, a):
        self._apellido = a

    @edad.setter
    def edad(self, e):
        self._edad = e

    def __del__(self):
        print('Objeto eliminado', self.describe())

# atributos encapsulados: llevan gion bajo _propiedad
"""
    DECORADORES
        modifican el comportamiento de los metodos
"""

