from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_raton = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_raton += 1
        super().__init__(marca, tipo_entrada)
        self._idRaton = Raton.contador_raton

    def __str__(self):
        return f'Id: { self._idRaton}, Marca: { self._marca }, Tipo Entrada: { self._tipo_entrada }'


