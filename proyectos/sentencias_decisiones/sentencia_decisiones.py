# Sentencia Decisiones
# Estos son condicionales que devuelven
# (True o False) dependiendo de lo que se le pida

# Ejemplo con (if) funciona si es True
edad = 19
if edad >= 18:
    print('Eres mayor de edad')

# Ejemplo con (else) funciona si es False
edad = 1
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

# Ejemplo con (elif) funciona para colocar otra condicion adicional
edad = 17
if edad >= 18:
    print('Eres mayor de edad')
elif 10 <= edad < 18:
    print('Eres un adolecente')
else:
    print('Eres menor de edad')