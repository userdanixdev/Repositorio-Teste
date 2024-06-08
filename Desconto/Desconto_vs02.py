# Desconto Versão 02:
# Faça um algoritmo que leia o preço de um produto e mostre o desconto:

preco_produto=float(input('Qual é o preço do produto? '))
desconto = preco_produto * 0.05 
print(f''' O preço com desconto do produto {preco_produto-desconto} reais
      Foi descontado {desconto} reais do valor de {preco_produto} do produto.''')

