# Generador de gmail
nombre_usuario = '  SrElisamuel'
nombre_empresa = '  gmail'
extension_dominio = '.com'

print('-----------------+ Generador de Gmail +-----------------')

# Normalizacion de nombre de usuario
print(f'1 --- Nombre Usuario: {nombre_usuario}')
normalizando_nombre_usuario = nombre_usuario.strip().replace(' ', '.').lower()
print(f'-- Nombre Usuario Normalizado: {normalizando_nombre_usuario} -+')

# Normalizando nombre de empresa y dominio
print(f'\n2 --- Nombre Empresa: {nombre_empresa}')
print(f'3 --- Extension del Dominio: {extension_dominio}')
normalizando_nombre_empresa = nombre_empresa.strip().lower().replace(' ', '')
gmail_final = f'@{normalizando_nombre_empresa}{extension_dominio.strip()}'
print(f'-- Dominio de gmail normalizado: {gmail_final} -+')

# Creacion del Gmail
gmail_final = f'{normalizando_nombre_usuario}{gmail_final}'
print(f'\n4 --- Gmail Final: {gmail_final} -+')

print('--------------------------------------------------------')
