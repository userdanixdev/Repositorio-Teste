# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Posição do seu time

times=('Botafogo','Palmeiras','Atlético-MG','Grêmio','Flamengo','Fluminense',
       'Atlético-PR','São Paulo','Fortaleza','Cruzeiro','Bragantino','Santos',
       'Internacional','Cuibá','Bahia','Corinthians','Goiás','América-MG','Vasco',
       'Coritiba')

print(f'{"Tabela do Brasileiro-2023"}\n{times}\n{'+'*40}\nOs 5 primeiros times: {times[0:5]}\n{'+'*40}\nOs 4 últimos times: {times[-4:]}\n')
print(f'{'='*40}\nOs times em ordem alfabética: {sorted(times)}\n{'='*40}')
while (clube := input('Digite o nome do seu time: ').capitalize()) not in times:
    print('O seu time não está na lista')
print(f'O {clube} está na posição {times.index(clube)+1}°\n{'+'*40}')    
