# Uma IMOBILIÁRIA paga aos seus corretores um salário base de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por cada imóvel vendido e 
# 5% do valor de venda.
# Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas.
# Ao fim, o programa deve calcular a quantidade de imóveis vendidos e o valor total de suas vendas. 
# No fim, o programa deve calcular e escrever o salário final do corretor de imóveis.

# Versão 02: Funções

def calculo_salario_corretor(nome_corretor,quant_imovel,vendas_imovel_total):
    salario_base = 1500
    comissao_por_imovel = 200
    adicional_venda = 0.05

    valor_vendas_imovel= quant_imovel * comissao_por_imovel
    total_vendas = adicional_venda * vendas_imovel_total
    salario_total_corretor =  valor_vendas_imovel + total_vendas + salario_base
    
    return salario_total_corretor

def main():
    print(f'{'+'*80}\n{"Bem vindo ao programa de comissões da imobiliária TerraNostra":^78}\n{'+'*80}\n')
    nome_corretor = input('Me informe o nome do corretor: ')
    quant_imovel = int(input('Me informe a quantidade de imóveis vendidos: '))
    vendas_imoveis_total = float(input('Me informe o valor total de vendas:  '))

    salario_final = calculo_salario_corretor(nome_corretor,quant_imovel,vendas_imoveis_total)
    print(f'O salário final do corretor {nome_corretor} foi de R$ {salario_final:.2f} reais.')

main()