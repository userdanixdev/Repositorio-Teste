# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o seu time:

# Refatoração para funções da versão 03:

from time import sleep
clubes = (
    'Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Fluminense',
    'Atlético-PR', 'São Paulo', 'Fortaleza', 'Cruzeiro', 'Bragantino', 'Santos',
    'Internacional', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco',
    'Coritiba'
)

def exibir_titulo():
    '''Função para exibir o título do programa'''
    print(f'{'+'*50}\n{"Tabela do Brasileirão - 2023 ":^48}\n{'+'*50}')
    sleep(1)

def exibir_tabela_completa(clubes):
    '''Função para exibir a tabela completa'''
    for t in range(len(clubes)):
        print(f'{t+1}º{clubes[t]}')
        sleep(0.3)
    print(' '*20)        

def exibir_top_5(clubes):
    '''Função para exibir os 5 primeiros colocados'''
    print('Os 5 primeiros colocados do Brasileirão são:\n')
    for t in range(5):
        print(f'{t+1}º{clubes[t]}')
        sleep(0.3)
    print(' '*20)

def exibir_4_ultimos(clubes):
    '''Função para exibir os 4 ultimos colocados'''
    print('Os 4 últimos colocados são: \n')
    sleep(0.4)
    for posicao,time in enumerate(clubes[16:],17):
        print(f'{posicao}°{time}')
        sleep(0.3)

def exibir_times_ordenados(clubes):
    '''Função para exibir os times em ordem alfabética'''
    print('\nOs times em ordem alfabética: \n')
    sleep(1)
    clubes_ordenados = sorted(clubes)
    for ordem,time in enumerate(clubes_ordenados,1):
        print(f'{ordem}°{time}')
        sleep(0.3)
    print('\nFIM')

def main():
    sleep(1)
    exibir_titulo()
    exibir_tabela_completa(clubes)
    exibir_top_5(clubes)
    exibir_4_ultimos(clubes)
    exibir_times_ordenados(clubes)

main()

