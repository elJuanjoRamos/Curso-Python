from mundo_pc.Computadora import Computadora
from mundo_pc.Monitor import Monitor
from mundo_pc.Orden import Orden
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado

teclado = Teclado('HP', 'USB')
raton = Raton('HP', 'USB')
monitor = Monitor('HP', 15)

computadora = Computadora('HP', monitor, teclado, raton)
computadora2 = Computadora('Dell', monitor, teclado, raton)


computadoras = [computadora, computadora2]

orden = Orden(computadoras)
print(orden)