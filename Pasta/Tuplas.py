# Variável Composta: Trabalhando com Tuplas
# Para declarar uma tupla : ()
# Para declarar uma lista : []
# Para declarar um dicionário : {}

from time import sleep
lanche=()  # Tupla vazia

# Função para garantir que a entrada seja somente número inteiro:
def input_inteiro(mensagem):
    while True:
        try:
            valor= int(input(mensagem))
            return valor
        except ValueError:
            print('Valor inválido.Somente números inteiros.')

# Obter o número de valores a serem inseridos: Coleta de dados
num_valores=input_inteiro('Quantos valores deseja inserir na tupla? ')

#Loop para coletar os valores na tupla:
for i in range(num_valores):
    valor=input(f'Digite o tipo de lanche {i+1}: ')
    # Adicionar o valor a tupla:
    lanche += (valor,)
    sleep(1)
#Exibir a tupla resultante:
print('Tupla resultante: ',lanche)

# Percorrer a tupla: Uso de laço for
for comida in lanche:   # Comida é uma variável de execução que irá percorrer a tupla 'lanche'
    print(f'Eu vou comer {comida}')
    sleep(0.7)
print(f'Comi muito, foram {len(lanche)} tipos de lanches','\n')    

# Segunda forma de percorrer a lista de tupla:
sleep(1)
print('Segunda forma de percorrer a tupla: Por comprimento da tupla')
for cont in range(0,len(lanche)):
    sleep(0.7)
    print(f'Vou comer {lanche[cont]} na posição {cont+1}','\n')

print('Terceira forma de percorrer a tupla: Uso da função Enumerate')
# Terceira forma de percorrer a lista de tupla:
for posicao,comida in enumerate(lanche):
    sleep(0.7)
    print(f'Eu vou comer {comida} na posição {posicao+1}')
print(f'Comi muito, foram {len(lanche)} tipos de lanches','\nAté mais!') 







