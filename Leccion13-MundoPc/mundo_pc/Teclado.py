from mundo_pc.DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        super().__init__(marca, tipo_entrada)
        self._idTeclado = Teclado.contador_teclado

    def __str__(self):
        return f'Id: { self._idTeclado}, Marca: { self._marca }, Tipo Entrada: { self._tipo_entrada }'

