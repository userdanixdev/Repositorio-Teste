# Valores aleatórios: Versão 02
# Crie uma programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# 1. Mostrar a listagem dos números gerados
# 2. Mostrar o menor e o maior número que estão na tupla

from random import randint   # Método para randomizar números inteiros
numeros= (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)) 
for n in numeros:  # Variável de execucação 'n' irá percorrer os 5 métodos randômicos consecutivos
    print(f'Os números sorteados foram: {n}')
print(f'O maior número foi: {max(numeros)}\ne o menor foi: {min(numeros)}\nAté mais.')    

