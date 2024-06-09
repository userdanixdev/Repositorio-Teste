# Cadastro Jogador de futebol : Versão 01

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

#Versão 04: Refatoração modelada para função:

from time import sleep

def cabecalho():
    '''Função que exibe o cabeçalho'''
    print(f'{"="*30}\n{"Rendimento do jogador":^30}\n{"="*30}\n{"Insira os dados abaixo:"}')
    sleep(0.7)

def obter_dados_jogador():
    '''Função que obtem dados do jogador como nome
            e número de partidas'''
    jogador={}   # Variável 'jogador' recebe tipo dicionário
    jogador['Nome']=input('Insira o nome do jogador: ').capitalize()
    sleep(0.5)
    jogador['Partidas']=int(input('Quantidade de partidas: '))
    return jogador

def obter_gols(partidas):
    '''Função para obter o número de gols por partida'''
    gols = []  # Variável que recebe tipo lista
    for i in range(partidas):
        sleep(2)
        n_gols = int(input(f'Quantos gols na {i+1}º partida? '))
        sleep(2)
        gols.append(n_gols)
    return gols

def calcular_media(total_gols,partidas):
    '''Calcula a média de gols por partida'''
    return total_gols/partidas
def exibir_dados_jogador(jogador):
    '''Função que exibe os dados gerais do dicionário jogador'''
    sleep(2)
    print(f'{"+"*30}\n{"Dados do dicionário jogador":^30}\n{"+"*30}\n{jogador}')
    sleep(2)
    print(f'{"+"*30}\n{"Varredura do dicionário jogador":^30}\n{"+"*30}')
    sleep(2)
    for k,v in jogador.items():
        sleep(0.7)
        print(f'O campo {k} tem o valor {v}.')
        sleep(0.7)

def exibir_partidas_gols(gols):
    '''Função que exibe o número de gols por partida'''
    print(f'{"+"*30}\n{"Quantas partidas":^30}\n{"QTD GOLS":^30}\n{"+"*30}')
    sleep(2)
    for k,v in enumerate(gols):
        sleep(0.7)
        print(f'Na partida {k+1} fez {v} gols. ')
    sleep(0.7)        

def main():
    cabecalho()
    jogador=obter_dados_jogador()
    gols=obter_gols(jogador['Partidas'])

    jogador['Gols']=gols
    jogador["Total"]=sum(gols)
    jogador['Média']=calcular_media(jogador["Total"],jogador["Partidas"])

    exibir_dados_jogador(jogador)
    exibir_partidas_gols(gols)

    print(f'Total de {jogador["Total"]} gols. ')
    print(f'Média de gols por partida: {jogador["Média"]:.2f}.')

main()    
    



