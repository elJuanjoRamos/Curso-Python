class Orden:
    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self._idOrden = Orden.contador_orden
        self._computadoras = computadoras

    def add_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadora_Str = ''

        for comp in self._computadoras:
            computadora_Str += comp.__str__()


        return f"""
        Orden: { self._idOrden} 
        Computadoras: [
            { computadora_Str }
        ]
        """

