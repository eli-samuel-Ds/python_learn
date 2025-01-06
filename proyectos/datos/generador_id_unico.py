# Generador de ID Unico
print(')--------=(-> Generador De ID Unico <-)=--------(\n')
nombre_usuario = input('Introduzca su nombre: ')
apellido_usuario = input('Introduzca su apellido: ')
fecha_ano_nacimiento = int(input('Introduzca su ano de nacimiento: '))

# Procesando datos-----------------------------------------
primeros_caracteres_nombre = nombre_usuario[0:2].upper()
primeros_caracteres_apellido = apellido_usuario[0:2].upper()
ultimos_digitos_nacimiento_ano = str(fecha_ano_nacimiento)[2:]

# Generando numero----------------------------------------
from random import randint
generando_4_numero = randint(1000, 9000)

# Imprimiendo datos--------------------------------------
print(f'\nHola {nombre_usuario},')
print('     Tu numero de identificacion (ID) generado por el sistema es:')
print(
    f'     {primeros_caracteres_nombre}{primeros_caracteres_apellido}{ultimos_digitos_nacimiento_ano}{generando_4_numero}')
print('     Felicidades!')

print('\n-------------------------------------------------')