'''
El formateo de cadena es como la union de
diferentes datos, no solo string.
'''

# Formato de cadenas
nombre_completo = 'Julia Marisol'
edad = 30
dirrecion = 'La Duarte'

# F-String
print(f'Hola {nombre_completo}, tienes {edad} anos de edad, y vives en {dirrecion}')

# Format
print('Hola {}, tienes {} anos de edad, y vives en {}'.format(nombre_completo, edad, dirrecion))

