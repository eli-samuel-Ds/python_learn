# Operador Tenario
# Esta tecnica se utiliza para
# compactar las condiciones si son de una linea

# Ejemplo
edad = int(input('Cual es tu edad: '))

# Procesando
es_mayor = f'Si eres mayor: {edad}' if edad >= 18 else f'No eres mayor de edad: {edad}'
print(es_mayor)
