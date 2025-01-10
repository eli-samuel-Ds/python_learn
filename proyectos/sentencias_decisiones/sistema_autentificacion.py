# Sistema de autentificacion

print('=-+( SISTEMA DE AUTENTIFICACION )+-=')
USUARIO_VALIDO = 'admin'
CONTRASENA_VALIDA = '123'

# Introduccion de datos
nombre_usuario = input('Introduce tu nombre: ')
contrasena_usuario = input('Introduce tu contrasena: ')

# Procesando datos
if USUARIO_VALIDO == nombre_usuario and CONTRASENA_VALIDA == contrasena_usuario:
    print('BIENVENIDO AL SISTEMA')

elif USUARIO_VALIDO != nombre_usuario and CONTRASENA_VALIDA == contrasena_usuario:
    print('Su nombre no es el correcto')
    nombre_usuario = input('Introduce tu nombre: ')
    if USUARIO_VALIDO == nombre_usuario:
        print('BIENVENIDO AL SISTEMA')

elif USUARIO_VALIDO == nombre_usuario and CONTRASENA_VALIDA != contrasena_usuario:
    print('Su contrasena no es la correcto')
    contrasena_usuario = input('Introduce tu contrasena: ')
    if CONTRASENA_VALIDA == contrasena_usuario:
        print('BIENVENIDO AL SISTEMA')

else:
    print('Su nombre y contrasena son incorrectas')
    nombre_usuario = input('Introduce tu nombre: ')
    contrasena_usuario = input('Introduce tu contrasena: ')
    if USUARIO_VALIDO == nombre_usuario and CONTRASENA_VALIDA == contrasena_usuario:
        print('BIENVENIDO AL SISTEMA')