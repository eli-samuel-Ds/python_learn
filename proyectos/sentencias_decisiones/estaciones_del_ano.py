# Verificar en que estancion del ano esta

print('( EN QUE ESTACION ESTAMOS )')

#Introducion de datos
numero_mes = int(input(' ( Introduzca el numero del mes (1-12): '))

#Procesando datos
if numero_mes == 1 or numero_mes == 2 or numero_mes == 12:
    estacion_ano = 'Invierno'
elif numero_mes == 3 or numero_mes == 4 or numero_mes == 5:
    estacion_ano = 'Primavera'
elif numero_mes == 6 or numero_mes == 7 or numero_mes == 8:
    estacion_ano = 'Verano'
elif numero_mes == 9 or numero_mes == 10 or numero_mes == 11:
    estacion_ano = 'Otono'
else:
    estacion_ano = 'Estacion Desconocida'

#Imprimiendo datos
print(f'  ( La estacion del ano del mes: {numero_mes} es: {estacion_ano}')