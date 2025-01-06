# Subcadenas Manejo-----------------------------------------
# Las subcadenas son partes de la cadena original,
# es como buscar una parte

texto_utilizar = 'Juana De La Mar'

# Obtener la subcadena
subcadena = texto_utilizar[0:5]
print(f'La busqueda es: {subcadena}')

# Busqueda de Subcadenas-----------------------------------------
# Esto regresa el indice que estamos buscando, devuelve el primero
busqueda_subcadena = texto_utilizar.find('De')
print(f'El indice de busqueda es: {busqueda_subcadena}')

# Esto pasa si no lo encuentra
busqueda_subcadena = texto_utilizar.find('Del')
print(f'El indice de busqueda es: {busqueda_subcadena}')  # Ensena un (-1)

# Remplazar subcadenas-----------------------------------------
remplazar_subcadena = texto_utilizar.replace('Juana', 'Lucas')
print(f'El se remplazo: ({texto_utilizar}), por: ({remplazar_subcadena})')

# Separa Subcadenas-----------------------------------------
# Separa todo lo que se le especifique en el metodo (split)
# y lo convierte en una lista
texto_utilizar = 'Juana De La Mar, Esta En La Mar'

separar_cadenas = texto_utilizar.split(',')  # A que se le indica como separar
print(separar_cadenas)
separar_cadenas = texto_utilizar.split(' ')
print(f'{separar_cadenas}, esta lista tiene un tamano de: {len(separar_cadenas)}')
