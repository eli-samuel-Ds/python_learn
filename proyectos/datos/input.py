# Manejo de Entrada de Datos
# Es la forma de interactuar con el usuario

# Input sin conversion
nombre_usuario = input('Introduzca su nombre: ')
print(f'Como estas {nombre_usuario} ?')

# Input con int
edad_usuario = int(input('Introduzca su edad: '))
print(f'{nombre_usuario} tu edad es la siguiente: {edad_usuario}')
print(f'{nombre_usuario} en un ano vas a tener: {edad_usuario + 1}')

# Cosita pa que sepas
# 1
# Si usas el operador (==)
# puede hacer como si estuvieras manejando un boolean

# Ejemplo
es_jefe = input('Eres jefe (SI o NO): ')
print(f'Es jefe: ({es_jefe.lower() == 'si'})')  # Es como un condicional automatica

# 2
# Tambien puedes elegir cuantos decimales mostrar

# Ejemplo
float_larog = 102.2
print(f'Muestra solo un decimal: {float_larog}')
print(f'Aqui muestra mas decimales: {float_larog: .2f}')
