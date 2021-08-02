class Monitor:
    contador_monitor = 0;

    def __init__(self, marca, size):
        Monitor.contador_monitor += 1
        self._idMonitor = Monitor.contador_monitor
        self._marca = marca
        self._size = size

    def __str__(self):
        return f'Id: { self._idMonitor}, Marca: { self._marca }, Size: { self._size }'

