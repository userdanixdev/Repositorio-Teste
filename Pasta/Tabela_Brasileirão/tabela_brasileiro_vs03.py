# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o seu time:

clubes=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

# O módulo 'sleep' do módulo 'time' usa-se para pausar a execução do programa por determinado tempo
from time import sleep
sleep(1)  # Pausa por 1 segundo

# Centralizar o título:
print(f'{'+'*50}\n{"Tabela do Brasileirão 2023":^48}\n{'+'*50}')
sleep(1)

# Crie um loop 'for' para a variável de execução iterar sobre cada elemente da tupla clubes e com a função
# print mostrar o valor de cada elemento. Com um laço a iteração irá sair formatada, uma embaixo da outra.
for t in range(0,20):  # Sabemos que são 20 clubes, por isso um range de 0 a 20
    print(f'{t+1}°{clubes[t]}')  
    sleep(0.3)
print(f'{' '*20}\nOs 5 primeiros colocados do Brasileirão 2023: \n')
for t in range(0,len(clubes)-15): # -15 fica somente os 5 primeiros colocados
    sleep(0.3)
    print(f'{t+1}°{clubes[t]}')
print(' '*20,'\nOs 4 últimos colocados são: \n')
sleep(1)  
# A função enumerate irá percorrer tanto o índice e o valor dos 4 últimos elementos:
for posicao,time in enumerate(clubes[16:],17): # Contagem a partir do 16
    sleep(0.3)
    print(f'{posicao}º{time}')
print(f'{' '*15}\nTimes em ordem alfabética ordenada por posição: \n')
sleep(1)
for ordem in range(0,len(clubes)):
    print(f'{ordem+1}°{sorted(clubes)[ordem]}')
    sleep(0.3)
print('\nFIM')        






