# Generar numeros aleatorios

# Importar funciones
import random
from random import randint

# Generando valores
numero_generado = random.randint(1,10) # Si usamos solo (import random)
print(f'Generando numeros del 1 al 10: {numero_generado}')
print(f'Generando numeros como un dado del 1 al 6: {randint(1,6)}')