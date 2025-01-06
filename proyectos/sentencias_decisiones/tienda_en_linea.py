# Tienda en linea
# Dependiendo de las condiciones se
# realiza un descuento, tambien si es miembro

print(':=------ SISTEMA DE TIENDA EN LINEA ------=:\n')

# Introducion de datos
nombre_usuario = input(': Introduzca el nombre: ')
es_miembro = input('=: Es miembro de la tienda (SI o NO): ')
monto_usuario = float(input('-=: Introduzca el monto a pagar: '))
print('\n:=----------------------------------------=:\n')

# Procesando datos
es_miembro = es_miembro.lower().strip().replace(' ', '')

if monto_usuario >= 1000 and es_miembro == 'si':
    print(f': FACTURA DEL CLIENTE: {nombre_usuario}')
    print('=: Se le aplicara un descuento del 10%, en la compra.')
    print(f'-=: Monto de la compra: {monto_usuario: .2f}')
    descuento_10 = monto_usuario * (10 / 100)
    print(f'--=: Monto del descuento: {descuento_10: .2f}')
    monto_final_pagar = monto_usuario - descuento_10
    print(f'---=: Monto final con descuento: {monto_final_pagar: .2f}')

elif es_miembro == 'si':
    print(f': FACTURA DEL CLIENTE: {nombre_usuario}')
    print('=:  Se le aplicara un descuento del 5%, en la compra.')
    print(f'-=: Monto de la compra: {monto_usuario: .2f}')
    descuento_5 = monto_usuario * (5 / 100)
    print(f'--=: Monto del descuento: {descuento_5: .2f}')
    monto_final_pagar = monto_usuario - descuento_5
    print(f'---=: Monto final con descuento: {monto_final_pagar: .2f}')

else:
    print(f': FACTURA DEL CLIENTE: {nombre_usuario}')
    print('=: No se aplicara ningun descuento.')
    print('-=: Pero puedes hacerte miembro para recibir beneficios')
    print(f'--=: Monto final: {monto_usuario: .2f}')

print('\n:=----------------------------------------=:')