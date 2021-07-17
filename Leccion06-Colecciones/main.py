# LISTAS

nombres: str = ['Juan', 'Karla', 'Ricardo', 'Maria']

print(nombres)

# acceder de forma inversa
print(nombres[-1])
# acceder un rango de valores, sin icluir hasta el indice superior
print(nombres[0:2])
# ir del inicio de la lista al indice sin incluirlo
print(nombres[:3])

# ir desde e indice indicado hasta el final, si se incluye el primer indice
print(nombres[1:])

for i in nombres:
    print(i)
else:
    print('no existen mas nombres en la lista');

print(f'el largo es {len(nombres)}')

##agregar elementos a la lista

nombres.append('Lorena')
print(nombres)

# insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)
# remover un elemento
nombres.remove('Octavio')
print(nombres)
# remover el ultimo elemento
nombres.pop();
print(nombres)

# eliminar un elemento segun un elemento
del nombres[0]  # -- del arreglo[index]
print(nombres)

# limpiar lista
nombres.clear()
print(nombres)
# borrar la lista por completo
# del nombres
# print(nombres)


# ////////////////////////////////
#           TUPLES
# ////////////////////////////////
print('inicia tuplas')

# definir una tupla
frutas = ('Naranja', 'Manzana', 'Platano')

print(len(frutas))
print(frutas[0])

#recorrer
for i in frutas:
    print(i, end=' ')

# convertir tupla a lista
frutasLista = list(frutas)
frutasLista.insert(1, 'Pera')
frutas = tuple(frutasLista)
print(frutas)




tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
else:
    print('Ya no hay numeros')
print(lista)


# ////////////////////////////////
#           SET
# no tiene indices ni orden, no soporta elementos duplicados
# ////////////////////////////////
print('inicia set')

planetas = { 'Marte', 'Tierra', 'Venus', 'Jupiter' }

print(planetas)

#largo
print(len(planetas))
# revisar si elemento esta presente
print('Marte' in planetas)
# agregar mas elementos
planetas.add('Mercurio')
print(planetas)
# eliminar elementos
planetas.remove('Tierra')
print(planetas)

planetas.discard('Jupiter')
print(planetas)

# limpiar por completo
planetas.clear()
print(planetas)
# eliminar por completo
#del planetas
#print(planetas)


# ////////////////////////////////
#           Diccionarios
# esta compuesto por dos elementos, (key, value)
# ////////////////////////////////

print('empieza dicionario')

diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBSM': 'Database Management System'
}

variable: int = 0

print(diccionario)

#largo
print(len(diccionario))
#acceder a los elementos
print(diccionario['IDE'])
#otra forma de acceder
print(diccionario.get('IDE'))

#RECCORRER ELEMENTOS DEL DICCIONARIO
for key, value in diccionario.items():
    print(key, value)

#Unicamente recuperar las llaves
for key in diccionario.keys():
    print(key)

# Unicamente recuperar los valores
for value in diccionario.values():
    print(value)

# agregar un elemento

diccionario['PK'] = 'Primary Key'
print(diccionario)
# remover un elemento
diccionario.pop('IDE')
print(diccionario)
# LIMPIAR
diccionario.clear()
print(diccionario)




