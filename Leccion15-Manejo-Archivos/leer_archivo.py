try:
    archivo = open('prueba.txt', 'r', encoding='utf8')
    # leer caracteres
    #print(archivo.read(2))
    #print(archivo.read(5))
    # leer lineas completas

    archivo = open('prueba.txt', 'a', encoding='utf8')

except Exception as e:
    print(e)
