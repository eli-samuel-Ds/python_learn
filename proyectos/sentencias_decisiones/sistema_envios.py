#Sistema de envios

print('\n======-> SISTEMA DE ENVIOS ======->\n')

#Variables globales
PESO_NACIONAL = 10
PESO_INTERNACIONAL = 20

#Introduccion de datos
nombre_cliente = input('Nombre cLiente: ')
print('\n====-> MENU DE TIPOS DE ENVIO ===->')
print('=-> 1(Nacional) - 2(Internaci.) =->')
tipo_envio = int(input('Elija un tipo de envio: '))
print('=================================->\n')
peso_envio = float(input('Peso en (Kilogramos): '))

#Procesando datos
if tipo_envio == 1:
    tipo_envio = 'NACIONAL'
    monto_pagar = PESO_NACIONAL * peso_envio
else:
    monto_pagar = PESO_INTERNACIONAL * peso_envio
    tipo_envio = 'INTERNACIONAL'

#Imprimiendo
print('\n=================================->')
print('=====-> FACTURA DE ENVIO')
print(f'> NOMBRE CLIENTE: {nombre_cliente.upper()}')
print(f'-> TIPO DE ENVIO: {tipo_envio}')

if tipo_envio == 'NACIONAL':
    tipo_envio = PESO_NACIONAL
else:
    tipo_envio = PESO_INTERNACIONAL

print(f'=-> TARIFA DE PESO DE ENVIO: {tipo_envio}')
print(f'==-> PESO DEL PAQUETE: {peso_envio: .2f} (KG)')
print(f'===-> MONTO FINAL A PAGAR: {monto_pagar: .2f}')

print('=================================->')