# Cadastro Jogador de futebol : Versão 03

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

#Versão 03: Refatoração modelada para objeto:

from time import sleep

class Jogador:
    def __init__(self,nome):
        self.nome = nome.capitalize()
        self.partidas=0
        self.gols=[]
        self.total_gols=0

    def adicionar_partidas(self,partidas):
        self.partidas = partidas
        for p in range(partidas):
            gols_na_partida=int(input(f'Quantos gols {p+1}º partida? '))
            self.gols.append(gols_na_partida)
            self.total_gols += gols_na_partida

    def exibir_dados(self):
        sleep(0.8)
        print(f'{"+"*50}\n{"Percorrendo o dicionário JOGADOR":^48}\n{"+"*50}')
        sleep(1)        
        print(f'Nome: {self.nome}')    
        print(f'Partidas: {self.partidas}')
        print(f'Gols: {self.gols}')
        print(f'Total de Gols: {self.total_gols}')
        sleep(1)
    
    def exibir_desempenho(self):
        print(f'O jogador {self.nome} tem {self.partidas} partidas. ')
        for c in range(self.partidas):
            print(f'Na partida {c+1} fez {self.gols[c]} gols.')
        print(f'Fez um total de {self.total_gols} gols.')

def main():
    print(f'{"+"*50}\n{"Rendimento do jogador":^48}\n{"+"*50}\nInsira os dados abaixo...')
    sleep(0.5)
    nome = input('Nome do jogador: ')
    jogador = Jogador(nome)

    sleep(0.3)
    partidas = int(input(f'Quantas partidas {jogador.nome} jogou? '))
    jogador.adicionar_partidas(partidas)

    jogador.exibir_dados()
    jogador.exibir_desempenho()

main()    