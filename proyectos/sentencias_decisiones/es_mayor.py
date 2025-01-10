# Sistema de verficacion mayor o menor

print('-=- CUAL ES MAYO DE LOS DOS -=-')

# Introducir datos
num_uno = int(input('- Introduce el primero numero: '))
num_dos = int(input('-= Introduce el segundo numero: '))

# Procesando numeros
es_mayor = f'\n-=- El primer numero es mayor: {num_uno}, el segundo es menor: {num_dos}' if num_uno > num_dos else f'\n-=- El segundo numero es mayor: {num_dos}, el primer numero es menor: {num_uno}'
print(es_mayor)