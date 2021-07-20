class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'Person[ Name: {self._name}, Age: {self._age}]'


    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, n):
        self._name = n
    @age.setter
    def age(self, a):
        self._age = a


class Employee(Person):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo