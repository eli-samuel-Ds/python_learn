# Manejo de conversion
# Cambiar el tipo de dato a otro

print(f'Conversiones normales\n')

# De String a Int
dato_1 = '19'
numero_convertido = int(dato_1)
print(f'Se convirtio el numero {dato_1} de {type(dato_1)} a {type(numero_convertido)}')

# De String a Float
dato_1 = '19.00'
numero_convertido = float(dato_1)
print(f'Se convirtio el numero {dato_1} de {type(dato_1)} a {type(numero_convertido)}')

# De Int a Cadena String
dato_1 = 19
numero_convertido = str(dato_1)
print(f'Se convirtio el numero {dato_1} de {type(dato_1)} a {type(numero_convertido)}')

print(f'\nLa conversion a boolean es diferente a las demas\n')

#Convertir Boolean
''''
False: Si el valor es 0 o None
True: Si es distinto de 0, o si la variable tiene un valor
'''

#Salidas False
dato_1 = 0
numero_convertido = bool(dato_1)
print(f'El valor convertido: ({dato_1}) a boolean es: {numero_convertido}')

dato_1 = None
numero_convertido = bool(dato_1)
print(f'El valor convertido: ({dato_1}) a boolean es: {numero_convertido}')

#Salidas True
dato_1 = 1
numero_convertido = bool(dato_1)
print(f'El valor convertido: ({dato_1}) a boolean es: {numero_convertido}')

dato_1 = 'Juana'
numero_convertido = bool(dato_1)
print(f'El valor convertido: ({dato_1}) a boolean es: {numero_convertido}')