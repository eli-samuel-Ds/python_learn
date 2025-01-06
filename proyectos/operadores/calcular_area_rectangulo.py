# Calcular El Area De Un Rectangulo

# Introducciendo datos
print('{- CALCULO DEL AREA DEL RECTANGULO -}')
dato_usuario_base = int(input('\n-[ Introduce la base: '))
dato_usuario_altura = int(input('-[ Introduce la altura: '))

# Formulas a tratar
area_final = dato_usuario_base * dato_usuario_altura
perimetro_final = 2 * (dato_usuario_base + dato_usuario_altura)

# Formato final
print(f'\n--[ El AREA: {area_final} y PERIMETRO: {perimetro_final} del RECTANGULO')
