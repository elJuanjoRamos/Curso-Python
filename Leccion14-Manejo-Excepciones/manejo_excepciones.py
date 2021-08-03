resultado = None
a = 10
b = 0

try:
    resultado = a/b
except Exception as e:
    print(f'Ocurrio un error: ', e)
except TypeError as e:
    print(f'Ocurrio un error: ', e)
except Exception as e:
    print(f'Ocurrio un error: ', e)

print(f'Resultado { resultado }')
print('Continuamos...')