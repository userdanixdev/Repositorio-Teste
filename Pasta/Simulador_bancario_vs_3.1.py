# Simulador Bancário Versão 3.1
# Modelando o programa com funções:

import textwrap

# Função Menu:
def menu():
    print(f'{'+'*40}\n{"Simulador Bancário Versão 3.1":^38}\n{'+'*40}')
    menu="""
            [d]\tDepositar
            [s]\tSacar
            [e]\tExtrato
            [q]\tSair
            
            Digite o comando abaixo:
            """
    return input(textwrap.dedent(menu)).upper()
    # A linha de return solicita entrada para o usuário e aguarda entrada

# Função depositar:                     
def depositar(saldo,valor,extrato,/): # saldo e valor são argumentos posicionais com base na ordem de chegada
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso')
    else:
        print('Operação falhou')                
    return saldo,extrato # A função irá retornar o saldo/extrato atualizado da conta
# Função sacar: O asterisco indica que todos os argumentos após ele devem ser passados como palavra-chave ao chamar a função
def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo # Tentativa de sacar um valor maior que o saldo
    excedeu_limite = valor > limite # Tentativa de sacar um valor superior ao limite e ao saque
    excedeu_saques = numero_saques >= limite_saques # Tentativa de de sacar superior ao limite de saques
    # Condicionais e respostas:
    if excedeu_saldo :
        print('Operação falha. Não tem saldo suficiente')        
    elif excedeu_limite:
        print('Operação falha. Saque maior que o limite.')        
    elif excedeu_saques:
        print('Operação falha. Limite de saques excedido.')        
    elif valor > 0:
        saldo = saldo - valor  # Se o valor for maior que zero o saldo é subtraido
        extrato = extrato + f'Saque:R$ {valor:.2f}' # 
        numero_saques = numero_saques + 1        
        print('Saque realizado com sucesso')
    else:
        print('Operação falhou. Valor informado inválido.')        
    return saldo, extrato
# Para a função abaixo, parâmetros antes de '/' são posicionais. Após o '*' argumentos são nomeados
def exibir_extrato(saldo,/,*,extrato):
    print(f'{"+"*50}\n{"Extrato":^48}\n{"+"*50}')
    print('Não foram realizadas movimentações.'if not extrato else extrato)
    print(f'Saldo:R$ {saldo:.2f}\n{'+'*50}')        
# Função principal:
def main():
    limite_saques = 3  # Constante
    saldo = 0
    limite = 100
    extrato = ''
    numero_saques = 0
    while True:
        opcao = menu()
        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))    
            saldo,extrato = depositar(saldo,valor,extrato)
        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques)
        elif opcao == 'E':
            exibir_extrato(saldo,extrato=extrato)
        elif opcao == 'Q':
            break
        else:
            print('Operação inválida.')

main() 
            
            
