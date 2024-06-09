# Cadastro Jogador de futebol : Versão 01

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

# Versão 03:

from time import sleep
# Declarações das variáveis:
jogador=dict()  # Variável 'jogador' recebe um dicionário
gol=[] # Variável gol recebe lista
partidas=0 # Contagem de partidas
total_gols = 0  # Contagem de gols

# Inserindo dados pelo usuário:
print(f'{'+'*50}\n{'Rendimento do jogador':^48}\n{'+'*50}\nInsira os dados abaixo...')
sleep(0.5)
jogador['Nome']=input('Nome do jogador: ').capitalize()
sleep(0.3)
partidas=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
# Inserir um laço para cada partida:
for p in range(partidas):
    gol.append(int(input(f'Quantos gols da {p+1}º partida? '))) # Para cada partida,a lista 'gol' recebe os dados
    total_gols += gol[p] # Variável contagem 'total_gols' recebe os gols
# Fora do laço, cria-se uma chave 'Gols' de jogador para receber uma cópia da lista 'gol'
jogador['Gols']=gol.copy()
jogador['Total']=total_gols # Dicionário jogador com chave 'total' recebe contagem de gols  'total_gols'

# Mostrar valores na tela:
sleep(0.8)
print(f'{'+'*50}\n{"Percorrendo o dicionário JOGADOR":^48}\n{'+'*50}')
sleep(1)
print(jogador)
sleep(1)
print()
for k,v in jogador.items():
    sleep(1)
    print(f'O campo {k} tem o valor {v}.')
print()    
# Mostrar o total de partidas e o total de gols:
print(f'O jogador {jogador["Nome"]} tem {partidas} partidas.')
for c in range(0,partidas):
    print(f'Na partida {c+1} fez {jogador["Gols"][c]}')
print(f'Fez um total fez {jogador["Total"]} gols.')    