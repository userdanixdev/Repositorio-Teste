# Simulador Bancário:
# Versão 01: 

menu=""""
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=>"""
saldo = 0
limite = 500
extrato=""
numero_saques = 0
limite_saques =  3

while True:
    opcao= input(menu)
    if opcao == 'd':
        valor=float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n "
        else:
            print ('Operação falhou. O valor informado é invalido.')            
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))            
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques
        if excedeu_saldo:
            print('Operação falhou. Você não tem saldo suficiente')
        elif excedeu_limite:
            print('Operação falhou. O valor do saque excedeu o limite.')            
        elif excedeu_saques:
            print('Operação falhou. Número máximo de saques excedido.')            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"            
            numero_saques += 1
        else:
            print('Operação falhou. O valor informado é invalido.')            
    elif opcao == 'e':
        #print(f'{'+'*42}\n{"Extrato":^40}\n{'+'*42}')
        print(f'{'+'*42}\n{"Extrato":^40}\n{'+'*42}\n{"Não foram realizadas transações"}\n'if not extrato else extrato)
        print(f'Saldo:R$ {saldo:.2f}\n{'+'*40}')
    elif opcao == 'q':
        print('Obrigado por utilizar nossos serviços. Volte sempre.')        
        break
    else:
        print('Opção invalida. Selecione a opção correta.')
    continuar = input('Deseja continuar outra operação? [S/N] ')        
    if continuar.lower() != 's':
        print('Obrigado por utilizar nossos serviços. volte sempre ')
        break


    