try:

    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('hola mundo ')
    archivo.write('desde Python')
except Exception as e:
    print(e)
finally:
    archivo.close()