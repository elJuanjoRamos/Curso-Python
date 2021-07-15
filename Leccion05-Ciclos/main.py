# condicion = True
#
# #el while puede tener un else
#
# while condicion :
#     print('Ejecutando ciclo while')
# else:
#     print('fin del cliclo while')

contador: int = 5

while contador >= 1:
    print(contador)
    contador -= 1
else:
    print('Fin ciclo while')


#CICLO FOR
print('Inicia FOR')
cadena:str = 'cansonante'

for letra in cadena:

    if letra == 'o':
        print(f'Letra encontrada { letra }')
        break
    if letra == 'a':
        print(f'Letra encontrada { letra }')
        continue
    print(letra)
else:
    print('Fin ciclo for')



for i in range(10):
    if i % 2 != 0:
        continue
    print(f'Valor: { i }')