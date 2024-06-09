# Cadastro Jogador de futebol : Versão 01

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
#Versão 04:

from time import sleep
print(f'{'='*30}\n{"Rendimento do jogador":^30}\n{'='*30}\n{'Insira os dados abaixo:'}')
sleep(0.7)
jogador={}  # Variável 'jogador' recebe dicionário
jogador['Nome']=input('Nome: ').capitalize()   #Dic 'jogador' recebe chave para receber valor do usuário
sleep(0.5)
jogador['Partidas']=int(input('Quantidade de partidas: ')) # Dic/chave/valor para o usuário inserir
gols=list()
for i in range(jogador['Partidas']):
    sleep(0.3)
    n_gols=int(input(f'Quantos gols na {i+1}º partida? '))
    sleep(0.5)
    gols.append(n_gols)  #Lista 'gols' recebe o número de gols de 'n_gols'
    jogador['Gols']=gols # Chave gols recebe lista de gols
    jogador['Total']=sum(gols)
# Inserir média de gols:
media_gols = jogador['Total']/jogador['Partidas'] # Calculo para média de gols por partida
jogador['Média']=media_gols # Dicionário 'jogador' recebe chave 'média' com valor 'media_gols'
# Dados gerais do dicionário:
sleep(2)
print(f'{'+'*30}\n{"Dados do dicionário jogador":^30}\n{'+'*30}\n{jogador}')
sleep(2)
print(f'{'+'*30}\n{"Varredura do dicionário jogador":^30}\n{'+'*30}')
sleep(2)
for k,v in jogador.items():
    sleep(0.7)
    print(f'O campo {k} tem o valor {v}.')
    sleep(0.7)
print(f'{'+'*30}\n{"Quantas partidas":^30}\n{"QTD GOLS":^30}\n{'+'*30}')
sleep(2)    
for k,v in enumerate(gols):
    sleep(0.7)
    print('Na partida {k+1}, fez {v} gols.')
sleep(0.5)
print(f'Total de {jogador["Total"]} gols.')    
print(f'Média de gols por partida: {media_gols:.2f}.')

                         


