
#IF

edad = int(input('Proporciona tu edad: ' ))
mensaje: str = 'Etapa de vida no reconocida'

if 0 <= edad < 10:
    mensaje = 'La infancia es increible...'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'


print(f'Tu edad es { edad }, ', mensaje )



