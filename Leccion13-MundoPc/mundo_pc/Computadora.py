from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:

    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self._idComputadora = Computadora.contador_computadora
        self._nombre = nombre
        self._monitor = monitor
        self._telado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        {self._nombre} : {self._idComputadora}
        Monitor: { self._monitor }
        Teclado: { self._telado }
        Raton: { self._raton }
        """


