# para definir funciones

def mi_funcion(nombre:str, edad: int, direccion: str):
    print(f'Hola {nombre}, con edad { edad } y direccion { direccion }, te saludo desde mi funcion')


mi_funcion('Karina', 15, '19 Av Zona 15')


def sumar(operando1:int,operando2:int):
    return operando1 + operando2

print('El resultado es ', sumar(5,5))


# valores por default a los parametros de funcion

def dividir(a=1, b=1) -> int:
    return a / b


print('El resultado de dividir es ', dividir(5,5))
print('El resultado de dividir es ', dividir())


