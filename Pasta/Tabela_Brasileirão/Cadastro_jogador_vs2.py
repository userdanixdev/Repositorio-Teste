# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Posição do seu time

# Versão 02:
# Criar um dicionário jogador com as chaves: 'Nome','Partidas','Gols' e os valores serão inseridos pelo usuário:
jogador=dict()  # Declarar a variável como dicionário
jogador['Nome']=input('Nome do jogador: ').capitalize()  # Chave declarada e o valor a ser inserido
jogador['Partidas']=int(input('Quantas partidas jogadas? '))
jogador['Gols']=list()  # Dicionário jogador, sua chave 'gols' recebe uma lista

for i in range(0,jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Quantos gols na {i+1}º partida? ')))   # Adiciona os gols para o dicionário chave gols
# Dicionário Partidas recebe a soma de Gols:
jogador['Total']=sum(jogador['Gols'])
print(f'{'='*70}\n{jogador}\n{'='*70}')
# Usaremos o 'items' para percorrer o dicionário:
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print()
print(f'O jogador {jogador["Nome"]} fez {jogador["Partidas"]} partidas.\n')    
#print()
# Mostrar o total de partidas e total de gols:
for c in range (0,jogador['Partidas']):
    print(f'=> Na partida {c+1} fez {jogador["Gols"][c]}.')
print(f' Um total de {jogador["Total"]} gols')    

