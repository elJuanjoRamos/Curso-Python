from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto


    def __str__(self):
        return f'Rectangulo[ {FiguraGeometrica.__str__(self)} , { Color.__str__(self)} ]'