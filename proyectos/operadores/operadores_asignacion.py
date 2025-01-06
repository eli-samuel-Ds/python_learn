# Operadores de asignacion
# Son lo que anaden valor a una variable

# Ejemplo
numero = 12  # Se le asigna el 12 a la variable

# Asignacion multiple
# Asigna multiples valores a multiples variables

# Ejemplo
cadena, numero_int, numero_float = 'Juana', 12, 12.22
print(f'Cadena: {cadena}, Numero entero: {numero_int}, Numero Flotante: {numero_float}')

# Asignacion encadena
# Asignar un mismo valor a varias variables
num_uno = num_dos = 10
print(f'Se declaran con el mismo valor: {num_uno}, {num_dos}')

# Intercambiar valores de dos variables
x, y = 10, 5
print(f'Valores iniciales: x:{x}, y:{y}')
x, y = y, x
print(f'Valores intercambiados: x:{x}, y:{y}')

# Hacer que el usuario introduzca mas de un valor
nombre, apellido = input('Introduce tu nombre y apellido (Separados por (,)): ').replace(' ', '').split(',')
print(f'Hola {nombre} me gusta tu apellido ({apellido})')
