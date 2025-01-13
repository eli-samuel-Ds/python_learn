# Calculadora
bucle_close = False
while not bucle_close:
    print('\n)-----(CALCULADORA)-----(\n')

    # Menu
    print('   )-----(MENU)-----(')
    print(')--(1. SUMA'
          '\n)--(2. RESTA'
          '\n)--(3. MULTI'
          '\n)--(4. DIVI'
          '\n)--(5. SALIR')
    opcion_usuario = input(')---(ELIGE UNA OPCION)-(')

    # Procesando datos
    if opcion_usuario == '1':
        print('\n)-----(SUMA)-----(')
        num_uno = float(input(')--(INTRODUCE EL PRIMER VALOR: '))
        num_dos = float(input(')--(INTRODUCE EL SEGUNDO VALOR: '))
        print(f')---(EL RESULTADO ES: {num_uno + num_dos:.2f}')

    elif opcion_usuario == '2':
        print('\n)-----(RESTA)-----(')
        num_uno = float(input(')--(INTRODUCE EL PRIMER VALOR: '))
        num_dos = float(input(')--(INTRODUCE EL SEGUNDO VALOR: '))
        print(f')---(EL RESULTADO ES: {num_uno - num_dos:.2f}')

    elif opcion_usuario == '3':
        print('\n)-----(MULTI)-----(')
        num_uno = float(input(')--(INTRODUCE EL PRIMER VALOR: '))
        num_dos = float(input(')--(INTRODUCE EL SEGUNDO VALOR: '))
        print(f')---(EL RESULTADO ES: {num_uno * num_dos:.2f}')

    elif opcion_usuario == '4':
        print('\n)-----(DIVI)-----(')
        num_uno = float(input(')--(INTRODUCE EL PRIMER VALOR: '))
        num_dos = float(input(')--(INTRODUCE EL SEGUNDO VALOR: '))
        print(f')---(EL RESULTADO ES: {num_uno / num_dos:.2f}')

    elif opcion_usuario == '5':
        bucle_close = True

    else:
        print('\n)---(OPCION INVALIDA')
else:
    print('\n)---(SALIENDO DE LA CALCULADORA')