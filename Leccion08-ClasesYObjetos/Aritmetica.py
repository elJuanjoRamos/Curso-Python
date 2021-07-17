class Aritmetica:
    """
    CLASE ARITMETICA para realizar las operaciones de suma, resta, multiplicaion, divicion
    """
    def __init__(self, op1: int, op2: int):
        self.operando1 = op1
        self.operando2 = op2
    def suma(self):
        return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2
    def multi(self):
        return self.operando1 * self.operando2
    def divi(self):
        return self.operando1 / self.operando2




aritmetica1 = Aritmetica(5,3)
print(aritmetica1.suma())

class Rectangle:

    def __init__(self, base, alt):
        self.base = base
        self.alt = alt

    def calculate_area(self):
        return self.base * self.alt
    def calculate_perimeter(self):
        return  2*self.base + 2*self.alt




base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

rectangle = Rectangle(base, altura)

print("El Area es: ", rectangle.calculate_area())
print("El Perimetro es: ", rectangle.calculate_perimeter())
