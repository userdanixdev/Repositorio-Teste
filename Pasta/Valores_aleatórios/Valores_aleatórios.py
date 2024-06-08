# Valores aleatórios:
# Crie uma programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# 1. Mostrar a listagem dos números gerados
# 2. Mostrar o menor e o maior número que estão na tupla

from random import randint   # Método para randomizar números inteiros
numeros= (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram: {numeros}',end='','\n')
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'\nO menor valor sorteado foi: {min(numeros)}')


