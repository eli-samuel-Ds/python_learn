# JUEGO DE ADIVINANZAS
from random import randint
numero_secreto = randint(1,50)
numero_intentos = 10

print('JUEGO DE ADIVINAZAS DE NUMERO')
print('EL NUMERO ESTA ENTRE 1 Y 50, TIENES 10 INTENTOS')

#Introducciendo datos
while not numero_intentos <= 0:
    numero_secreto_usuario = int(input('CUAL NUMERO CREES QUE SEA: '))
    if 0 < numero_secreto_usuario < 51:
        # Procesando datos
        if numero_secreto == numero_secreto_usuario:
            print(f'\nHAS GANADO CON ({numero_intentos} : INTENTOS)')
            numero_intentos = 0
        elif numero_secreto_usuario < numero_secreto:
            print(f'\n{numero_secreto_usuario} ES MENOR QUE EL NUMERO SECRETO: {numero_secreto - numero_secreto_usuario}')
            print(f'NUMERO DE INTENTOS {numero_intentos} / 10')
        else:
            print(f'\n{numero_secreto_usuario} ES MAYOR QUE EL NUMERO SECRETO: {numero_secreto - numero_secreto_usuario}')
            print(f'NUMERO DE INTENTOS {numero_intentos} / 10')

        numero_intentos -= 1
else:
    print(f'\nEL NUMERO SECRETO ERA: {numero_secreto}')
    print('TERMINO EL JUEGO')