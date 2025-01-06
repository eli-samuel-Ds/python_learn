# Sistema de Autentificacion

# Base de datos
# -Usuario
USUARIO_VALIDO = 'admin'
# -Contrasena
CONTRASENA_VALIDA = 123

print('-=- SISTEMA DE AUTENTIFICACION -=-')

usuario_ingresar = input('Intruzca su nombre: ')
contrasena_ingresar = int(input('Intruzca su contrasena: '))

print(f'Los Datos son correctos: {(USUARIO_VALIDO == usuario_ingresar) and (CONTRASENA_VALIDA == contrasena_ingresar)}')

print('------======------======------====')
