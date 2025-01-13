# Palabra BREAK
# Esta rompe completamente
# todo cuando se ejecuta, lo termina

# Ejemplo
print('PALABRA (BREAK):')
for i in range(1, 10):
    if i % 2 == 0:
        print(f'ESTE ES UN NUMERO PAR: {i}')
        break  # Cuando encuentra un numero par temina

print('\nPALABRA (CONTINUE):')
# Palabra CONTINUE
# Esta permite que continue el programa
for i in range(1, 10):
    if i % 2 == 1:
        continue  # Este hace que continue y busque los pares
    print(f'ESTO ES UN NUMERO PAR: {i}')
