# Valores aleatórios: Versão 04
# Crie uma programa que vai gerar 5 números aleatórios e colocar em uma tupla.
# 1. Mostrar a listagem dos números gerados
# 2. Mostrar o menor e o maior número que estão na tupla

from random import sample  # importar da biblioteca random o método sample

valores=(sample(range(10),5)) # Variável randômica
valores_ordem = sorted(valores) 
print(f'Os valores sorteados: {valores}\nO maior valor é: {valores_ordem[-1]}\nO menor valor é: {valores_ordem[0]}')
# Obs: A variável 'valores_ordem' põe a variável randômica 'valores' em ordem crescente , assim podemos extrair
# O maior valor [-1] e o menor valor: [0]
