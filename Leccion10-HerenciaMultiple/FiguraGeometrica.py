class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, a):
        self._alto = a
    @ancho.setter
    def ancho(self, a):
        self._ancho = a


    def __str__(self):
        return f'Ancho: {self._ancho}, Alto: {self._ancho}'
