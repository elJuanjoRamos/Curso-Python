
#IF

edad = int(input('Proporciona tu edad: ' ))
mensaje: str = 'Etapa de vida no reconocida'

if 0 <= edad < 10:
    mensaje = 'La infancia es increible...'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'


print(f'Tu edad es { edad }, ', mensaje)




calificacion = int(input('Proporciona un valor entre 0 y 10: ' ))
letra: str = None

if 9<= calificacion < 10 :
    letra = 'A'
elif 8<= calificacion < 9 :
    letra = 'B'
elif 7 <= calificacion < 8 :
    letra = 'C'
elif 6<= calificacion < 7 :
    letra = 'D'
elif 0<= calificacion < 6 :
    letra = 'F'
else:
    letra = 'Desconocida'

print(f'Tu calificacion fue de { calificacion }, tiene una letra { letra } ')

