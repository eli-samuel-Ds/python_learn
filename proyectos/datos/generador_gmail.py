# Generador De Gmail

# Introduciendo de datos ----------------------------------
print('==============-> Generador De Gmail <-===============\n')

nombre_usuario = input('Introduce tu nombre: ')
apellido_usuario = input('Introduce tu apellido: ')
nombre_empresa = input('Introduce el nombre de la empresa: ')
extension_dominio = input('Introduce tu dominio de empresa: ')

# Manejo de datos -----------------------------------------
print('\n-----------------------------------------------------\n')

formateando_nombre_usuario = nombre_usuario.lower().replace(' ', '.')
formateando_apellido_usuario = apellido_usuario.lower().replace(' ', '.')
formateando_nombre_empresa = nombre_empresa.lower().replace(' ', '')
formateando_extension_dominio = extension_dominio.lower().replace(' ', '')

gmail_final = f'{formateando_nombre_usuario}.{formateando_apellido_usuario}@{formateando_nombre_empresa}{formateando_extension_dominio}'

# Imprimiendo gmail generado
print(f'El gmail generado es: {gmail_final}')

print('\n=====================================================')