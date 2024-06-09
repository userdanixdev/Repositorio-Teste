# Cadastro Jogador de futebol : Versão 03

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

#Versão 03: Refatoração modelada para funções:

from time import sleep

def obter_dados_jogador():
    jogador=dict()
    gol=[]
    total_gols=0

    print(f'{'+'*50}\n{"Rendimento do jogador":^48}\n{'+'*50}\nInsira os dados abaixo...')
    sleep(0.5)
    jogador['Nome']= input('Nome do jogador: ').capitalize()
    sleep(0.3)
    partidas=int(input(f'Quantas partidas {jogador['Nome']} jogou? '))

    for p in range(partidas): # Percorrer os números de partidas computadas pelo usuário:
        gols_da_partida=int(input(f'Quantos gols na {p+1}º partida?  '))
        gol.append(gols_da_partida)
        total_gols += gols_da_partida

    jogador['Gols']=gol
    jogador['Total']=total_gols
    jogador['Partidas']=partidas

    return jogador

def exibir_dados_jogador(jogador):
    sleep(0.8)
    print(f'{'+'*50}\n{"Percorrendo o dicionário Jogador":^48}\n{'+'*50}\n{jogador}\n')
    sleep(1)
    for k,v in jogador.items():
        sleep(1)
        print(f'O campo {k} tem o valor {v}')
    print()

def exibir_desempenho(jogador):
    partidas=jogador['Partidas']
    print(f'O jogador {jogador['Nome']} tem {partidas} partidas. ')            
    for c in range(partidas):
        print(f'Na partida {c+1} fez {jogador['Gols'][c]} gols.' )
    print(f'Fez um total de {jogador['Total']} gols.')        

def main():
    jogador=obter_dados_jogador()
    exibir_dados_jogador(jogador)
    exibir_desempenho(jogador)

main()    


