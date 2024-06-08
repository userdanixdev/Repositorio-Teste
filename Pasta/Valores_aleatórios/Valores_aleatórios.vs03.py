# Valores aleatórios: Versão 03
# Crie uma programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# 1. Mostrar a listagem dos números gerados
# 2. Mostrar o menor e o maior número que estão na tupla

from random import sample  # Importar da biblioteca random o método sample

a=tuple(sample(range(10),5)) # Declarar uma variável com tipo tupla e adicionar o método sample (5) com range (10)
print(f'{a},\nO maior valor desse random {max(a)}\ne o menor {min(a)}')
