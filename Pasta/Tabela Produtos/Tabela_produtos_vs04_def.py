# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
# Versão 04:
# Essa versão o programa irá perguntar quantos e quais produtos entrar na lista.(tupla)

# Modelagem de funções:
def obter_quantidade_produtos():
    """
    Solicita ao usuário a quantidade de produtos a serem listados.
    
    :return: int, quantidade de produtos
    """
    while True:
        try:
            quantidade = int(input('Quantos produtos você quer listar? '))
            if quantidade < 0:
                print("Por favor, insira um número inteiro positivo.")
            else:
                return quantidade
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def listar_produtos(*,quantidade):
    """
    Coleta os nomes e preços dos produtos.
    
    :param quantidade: int, quantidade de produtos a serem listados
    :return: tuple, contendo os produtos e seus preços
    """
    produtos = ()
    for _ in range(quantidade):
        nome = input('Nome do produto: ')
        while True:
            try:
                preco = float(input('Preço do produto: '))
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido para o preço.")
        produtos += (nome, preco)
    return produtos

def formatar_listagem(produtos):
    '''Formata a listagem de produtos com seus preçoc'''        
    listagem_formatada=[] # Lista vazia
    for c in range(0,len(produtos),2):
        nome = produtos[c]
        preco = produtos[c+1]
        pontos = '.'*(25-len(nome))
        listagem_formatada.append(f'`{nome.capitalize()}{pontos}R${preco:.2f}')
    return listagem_formatada

def exibir_listagem(listagem):
    '''Exibe a listagem formatada'''        
    print(f'{"+" * 45}\n{"Listagem de preços":^42}\n{"+" * 45}')
    for item in listagem:
        print(item)
    print()        

def main():
    quantidade: int(input('Quantos produtos você quer listar? '))
    produtos = listar_produtos(quantidade)
    listagem_formatada= formatar_listagem(produtos)
    exibir_listagem(listagem_formatada)

main()