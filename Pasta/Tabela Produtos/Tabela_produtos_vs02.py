# Tabela produtos: Versão 02

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print(f'{'+'*45}\n{"Listagem de preços":^42}\n{'+'*45}')
quantidade=int(input('Quantos produtos você quer listar? '))
produtos=()
for c in range(0,quantidade):
    nome=input('Nome do produto: '), float(input('Preço do produto: '))
    produtos = produtos + (nome[0],nome[1])
print()    
for p in range(0,len(produtos),2):
    nome = produtos[p]
    preco = produtos[p+1]
    pontos = '.'*(25-len(produtos[p]))
    print(f'{nome.capitalize()}{pontos}R${preco:.2f}')
