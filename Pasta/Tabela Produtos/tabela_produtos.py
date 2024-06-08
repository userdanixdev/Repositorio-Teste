# Tabela produtos: Versão 01

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabela=('Lápis',1.75,'Borracha',2,'Carderno',15.9,'Estojo',25,'Transferidor',4.2,
        'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

print(f'{'+'*45}\n{"Listagem de preços":^42}\n{'+'*45}')

for c in range(0,len(tabela),2):
    print(f'{tabela[c]:.<30} R$ {tabela[c+1]:>10.2f}')
print('+'*45)    

