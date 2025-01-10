# Cajero automatico
monto_usuario = 1000.00
bucle_close = False

while not bucle_close:
    print('\n<(==== (CAJERO AUTOMATICO) ====)>')

    # Introduccion de datos
    print('          <==(MENU)==>')
    print('       | 1.CONSULTAR SALDO |'
          '\n       | 2.RETIRAR |'
          '\n       | 3.DEPOSITAR |'
          '\n       | 4.SALIR |')
    opcion_usuario = int(input('<(==== (ELEGI UNA OPCION: '))

    # Procesando datos
    if opcion_usuario == 1:
        print(f'\n<(==== (SALDO ACTUAL:{monto_usuario: .2f}) ====)>')

    elif opcion_usuario == 2:
        print(f'\n<(==== (SALDO ACTUAL:{monto_usuario: .2f}) ====)>')
        saldo_retirar = float(input('\n<(==== (CUANTO DESEAS RETIRAR: '))
        if saldo_retirar > monto_usuario:
            print(f'\n<(==== (EL MONTO A RETIRAR:{saldo_retirar: .2f} ES MAYOR AL SALDO:{monto_usuario: .2f}) ====)>')
        elif saldo_retirar < 0:
            print(f'\n<(==== (EL MONTO A RETIRAR: {saldo_retirar: .2f} ES NEGATIVO:{monto_usuario: .2f}) ====)>')
        else:
            monto_usuario = monto_usuario - saldo_retirar
            print(f'\n<(==== (SALDO ACTUAL:{monto_usuario: .2f}) ====)>')

    elif opcion_usuario == 3:
        print(f'\n<(==== (SALDO ACTUAL:{monto_usuario: .2f}) ====)>')
        monto_depositar = float(input('\n<(==== (CUANTO DESEA DEPOSITAR: '))
        if monto_depositar < 0:
            print(f'\n<(==== (EL MONTO A DEPOSITAR NO PUEDE SER NEGATIVO: {monto_depositar: .2f}) ====)>')
        else:
            monto_usuario = monto_usuario + monto_depositar
            print(f'\n<(==== (SALDO ACTUAL:{monto_usuario: .2f}) ====)>')

    elif opcion_usuario == 4:
        bucle_close = True

    else:
        print('\n<(==== (OPCION DESCONOCIDA) ====)>')

else:
    print('\n<(==== (SALIENDO DEL CAJERO AUTOMATICO) ====)>')
