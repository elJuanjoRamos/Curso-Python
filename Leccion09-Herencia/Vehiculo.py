class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return f'Vehiculo[Color: { self.color }, Ruedas { self.ruedas }]'


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return f'{ super.__str__()}  Coche[ Velocidad { self.velocidad }]'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f'{ super.__str__()}  Bicicleta[ Tipo { self.tipo }]'
