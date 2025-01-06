# Valor Dentro Del Rango

# Datos a confirmar
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# Introduciondo datos
print('[ VALOR DENTRO DEL RANGO ]')
valor_usuario_introduccir = int(input('Introduce un numero: '))

# Procesando Datos
resultado = VALOR_MINIMO <= valor_usuario_introduccir <= VALOR_MAXIMO

#Resultado final
print(f'El valor esta dentro del rango: {resultado}')