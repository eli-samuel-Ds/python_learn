# Sitema de calificacion

print('\n---)-> SISTEMA DE CALIFICAION ESTUDIANTIL <-(---\n')

# Introducion de datos
nombre_estudiante = input('Introduzca su nombre: ')
nota_numerica = float(input('Introduzca su nota (0-10): '))
nota_letra_final = None

# Procesando datos
if nota_numerica < 0 or nota_numerica > 10:
    print('---)-> VALOR DE NOTA DESCONOCIDO')
else:
    if 9 <= nota_numerica <= 10:
        nota_letra_final = 'A'
    elif 8 <= nota_numerica < 9:
        nota_letra_final = 'B'
    elif 7 <= nota_numerica < 8:
        nota_letra_final = 'C'
    elif 6 <= nota_numerica < 7:
        nota_letra_final = 'D'
    elif 0 <= nota_numerica < 6:
        nota_letra_final = 'F'

#Inprimiendo datos
    print(f'Estudiante: {nombre_estudiante} su calificaciones: {nota_numerica}, por lo tanto tiene una: {nota_letra_final}')
