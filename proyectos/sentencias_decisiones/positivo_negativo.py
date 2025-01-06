# Un numero que introduzca el
# usuario es positivo o negativo

# Entrada de Datos
print(':- NUMERO POSITIVO O NEGATIVO -:')
numero_usuario = int(input('Introduce un numero: '))

# Procesando datos
if numero_usuario > 0:
    print(f'El numero es positivo: {numero_usuario}')
elif numero_usuario < 0:
    print(f'El numero es negativo: {numero_usuario}')
else:
    print(f'El numero es cero: {numero_usuario}')
