# Segundo versão aluguel de carros:

def calcular_preco_aluguel(km,dias):
    valor_diaria = 60
    valor_por_km = 0.15
    valor_percorrido_total = km * valor_por_km
    diaria_total = dias * valor_diaria
    preco_pagar = diaria_total + valor_percorrido_total
    return preco_pagar
def main():
    print('Bem vindo ao aluguel de carros: \n')
    km = float(input('Quantos Km a serem percorridos? '))
    dias = int(input('Quantos dias para ser alugado? '))
    preco_pagar = calcular_preco_aluguel(km,dias)
    print(f'Preço a pagar proporcional aos dias e a Kilometragem será de R$ {preco_pagar:.2f}')

main()    