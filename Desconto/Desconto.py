# Faça um algoritmo que leia o preço de um produto e mostre o desconto:

preco_produto=float(input('Qual é o preço do produto? '))
desconto = preco_produto * 0.05
print(f'O preço do produto com desconto de 5% é: {preco_produto-desconto}.')
print(f'Foi descontado {desconto} reais do valor do {preco_produto}')