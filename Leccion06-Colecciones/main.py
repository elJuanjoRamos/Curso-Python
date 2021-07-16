#LISTAS

nombres: str = ['Juan', 'Karla', 'Ricardo', 'Maria']

print(nombres)

#acceder de forma inversa
print(nombres[-1])
#acceder un rango de valores, sin icluir hasta el indice superior
print(nombres[0:2])
#ir del inicio de la lista al indice sin incluirlo
print(nombres[:3])


#ir desde e indice indicado hasta el final, si se incluye el primer indice
print(nombres[1:])

for i in nombres:
    print(i)
else:
    print('no existen mas nombres en la lista');


print(f'el largo es { len(nombres) }')

##agregar elementos a la lista

nombres.append('Lorena')
print(nombres)

#insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres)
#remover un elemento
nombres.remove('Octavio')
print(nombres)
#remover el ultimo elemento
nombres.pop();
print(nombres)

#eliminar un elemento segun un elemento
del nombres[0] #-- del arreglo[index]
print(nombres)

#limpiar lista
nombres.clear()
print(nombres)
#borrar la lista por completo
#del nombres
#print(nombres)


#////////////////////////////////
#
#////////////////////////////////


