# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Posição do seu time

# Refatorado por funções:

times = ('Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Fluminense',
         'Atlético-PR', 'São Paulo', 'Fortaleza', 'Cruzeiro', 'Bragantino', 'Santos',
         'Internacional', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco',
         'Coritiba')

def exibir_tabela():
    print(f'{'+'*40}\n{"Tabela do Brasileiro 2023":^38}\n{'+'*40}\n')

def exibir_todos_times():
    print(f'\nA tabela completa do Brasileiro:\n{times}\n{'='*40}\n')

def exibir_cinco_primeiros():
    print(f'Os 5 primeiros times do Brasileiro 2023: \n{times[0:5]}\n{'='*40}\n')

def exibir_quatro_ultimos():
    print(f'Os 4 últmos times do brasileiro 2023:\n{times[-4:]}\n{'='*40}\n')
def times_ordem_alfabética():
    print(f'Os times na ordem alfabética são:\n{sorted(times)}\n{'='*40}\n')
def exibir_posicao_time():
    while True:
        clube = input('Digite o nome do seu time: ').capitalize()
        if clube not in times:
            print('Seu time não está na lista') 
        elif clube in times:
            print(f'O {clube} está na posição {times.index(clube)+1}º')                               
            break
        else:
            print('O seu time não está na lista')
def main():
    exibir_tabela()
    exibir_todos_times()
    exibir_cinco_primeiros()
    exibir_quatro_ultimos()
    exibir_posicao_time()

main()                        