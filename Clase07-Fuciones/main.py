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


# argumentos variables, cuando no se sabe la cantidad de parametros que tiene una funcion
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Pedro', 'Karina', 'Marcos', 'Martha', 'Erick', 'El Brayan', 'La Kimberly')


def sumar_numeros(*args):
    resul: int = 0
    for i in args:
        resul += i
    return resul

resultado = sumar_numeros(10,20,30,40,50)
print(f'El resultado es: { resultado }')



def multiplicar_numeros(*args):
    resul: int = 1
    for i in args:
        resul *= i
    return resul

print(f'El resultado es: { multiplicar_numeros(10,10,10) }')

# ARGUMENTOS VARIABLES LLAVE-VALOR
# **nombre -> diccionario
def listar_terminos(**terminos):
    for key, value in terminos.items():
        print(f'Llave: { key }, Valor: { value }')


listar_terminos(IDE='Integrated Delevopment Enviroment', PK='Primary Key', DBSM='Database Management System')

#Distintos tipos de datos como argumentos
def desplegar_nombres(nombres):
    for i in nombres:
        print(i)


desplegar_nombres(['Juan', 'Pedro', 'Martha', 'Luisa'])

#Funciones Recursivas

def factorial(numero:int):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)


print(f'El factorial es { factorial(9) }')


def print_numeros(numero:int):
    if numero > 1:
        print(numero)
        print_numeros(numero-1)


print_numeros(5)