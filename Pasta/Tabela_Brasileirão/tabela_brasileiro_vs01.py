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

print(times)  # Com a função imprime toda a tupla.
print('='*40)

# O slicing [0:5] irá retornar uma sub-tupla contendo os elementos do índice 0 a 4 (os 5 primeiros)
print(f'Os 5 primeiros times do Brasileirão 2023: {times[0:5]}')
print('='*40)

# O slicing [-4:] irá retornar uma sub-tupla contendo os últimos 4 elementos.
print(f'Os 4 últmos times do Brasileirão 2023: {times[-4:]}')
print('='*40)

# A função sorted() irá ordenar a tupla 'times' 
print(f'Os times em ordem alfabética: {sorted(times)}')
print('+'*40)

# Seu time está em que posição:
while True:
    clube=input('Digite o nome do seu time: ').capitalize()
    if clube in times:
        print(f'O {clube} esta na posição {times.index(clube)+1}°')
        break
    else:
        print('O seu time não está na lista.')

        
      

