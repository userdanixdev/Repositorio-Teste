# Pequeno programa para alugar carros:
# Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias
# que ele foi alugado; Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e o preço por KM 
# rodado é de R$ 0,15.

print('Bem vindo ao aluguel de carros:\n ')
km = float(input('Quantos KM a serem percorridos? '))
dias = int(input('Quantos dias para ser alugado? '))
valor_diaria = 60
km1=0.15
valor_percorrido_total=km*km1
diaria_total=dias*valor_diaria
preco_pagar=diaria_total+valor_percorrido_total
print(f'Preço a pagar proporcional aos dias e a kilometragem será: {preco_pagar:.2f} reais.')



