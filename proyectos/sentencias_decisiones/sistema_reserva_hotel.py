# SISTEMA DE RESERVA DE HOTEL
print('========-\\\\ SITEMA DE RESERVAS DE HOTEL //-========')

# Introducion de datos
nombre_cliente = input('\n/ Nombre del Cliente: ')
dias_estadia_hotel = (int(input('-/ Dias de estadia del hotel: ')))
tiene_vista_mar = input('=-/ Quieres tener vista al mar (SI O NO): ')

# Procesando informacion
tiene_vista_mar = tiene_vista_mar.strip().replace(' ', '').lower() == 'si'

if not tiene_vista_mar:
    monto_final_pagar = dias_estadia_hotel * 150.50
else:
    monto_final_pagar = dias_estadia_hotel * 190.50

# Imprimiendo datos
print('\n========-\\\\ DETALLES DE LA RESERVACION //-=========\n')
print(f'/ CLIENTE: {nombre_cliente.upper()}')
print(f'-/ DIAS DE ESTADIA: {dias_estadia_hotel}')
print(f'=-/ COSTO TOTAL A PAGAR: {monto_final_pagar: .2f}')
tiene_vista_mar = 'SI' if tiene_vista_mar else 'NO'
print(f'==-/ ELIGIO UNA HABITACION CON VISTA AL MAR: {tiene_vista_mar}')