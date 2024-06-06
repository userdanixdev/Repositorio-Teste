## Realizando testes com Python:
# Calculadora:

from time import sleep

print(f'{"+"*50}\n{"Calculadora em Python":^49}\n{"+"*50}')
sleep(1)

def adicao(x,y):
    return x+y
def subtracao(x,y):
    return x-y
def multiplicacao(x,y):
    return x*y
def divisao(x,y):
    return x/y
while True:
    print(f'\n{'Selecione o número da operação desejada':^49}\n')
    print('''
                    1- Soma 
                    2 - Subtração
                    3. Multiplicação
                    4. Divisão '''
                )
    sleep(1)     
    escolha=input('Digite sua opção (1/2/3/4):')           
    sleep(0.5)
    numero_1 = int(input('Digite o primeiro número: '))
    sleep(0.3)
    numero_2 = int(input('Digite o segundo número: '))
    sleep(1)
    print('Aguarde instantes ...')
    sleep(1.5)
    if escolha == '1':
        print(numero_1, '+',numero_2,'=',adicao(numero_1,numero_2))
    elif escolha == '2':
        print(numero_1, '-',numero_2,'=',subtracao(numero_1,numero_2))
    elif escolha == '3':
        print(numero_1,'X',numero_2,'=', multiplicacao(numero_1,numero_2))        
    elif escolha == '4':
        print(numero_1, '/',numero_2,'=',divisao(numero_1,numero_2))        
    else:
        print('Opção Inválida')        
    sleep(1)
    resposta = input('Deseja continuar? [S/N].')        
    while resposta not in 'SsNn':
        resposta = input('Resposta Inválida, somente [S/N].')
    if resposta in 'Nn':
        break
print('Até mais')        
