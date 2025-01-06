# Concatenacion de cadena
cadena1 = 'Juana'
cadena2 = 'De'
cadena3 = 'Arco'

# Nombre unido con el (+)
nombre_completo_concatenado = cadena1 + ' ' + cadena2 + ' ' + cadena3
print(nombre_completo_concatenado)

# Nombre unido con el (.join)
nombre_completo_concatenado = ''.join([cadena1,' ', cadena2, ' ', cadena3])
print(nombre_completo_concatenado)
