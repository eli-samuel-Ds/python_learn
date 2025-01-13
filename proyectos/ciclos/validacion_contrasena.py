# VALIDACION DE CONTRASENA
bucle_close = False
while not bucle_close:
    print('\n-= CREAR Y VALIDAR LA CONTRASENA =-')

    # Introducciendo datos
    contra_usuario = input('- INTRODUCE NUEVA CONTRASENA SOLO (6 CARACTERES): ')
    if len(contra_usuario) == 6:
        # Procesando
        contra_usuario_valida = input('-= VUELVA A ESCRIBIRLA: ')
        bucle_close = True if contra_usuario == contra_usuario_valida else False
else:
    print('-= CONTRASENA VALIDA =-')