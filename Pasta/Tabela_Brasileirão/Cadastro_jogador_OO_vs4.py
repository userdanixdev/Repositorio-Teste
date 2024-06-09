# Cadastro Jogador de futebol : Versão 01

# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

#Versão 04: Refatoração modelada para Orientação a objeto:

from time import sleep
class Jogador:
    def __init__(self,nome,partidas):
        self.nome = nome
        self.partidas = partidas
        self.gols = []
        self.total_gols=0
        self.media_gols=0

    def adicionar_gols(self):
        '''Função que obtem número de gols por partida'''
        for i in range (self.partidas):
            sleep(0.3)
            n_gols=int(input(f'Quantos gols na {i+1}º partida? '))
            sleep(0.5)
            self.gols.append(n_gols)
        self.calcular_total_e_media()

    def calcular_total_e_media(self):
        '''Função que calcula a média de gols e o total'''                    
        self.total_gols=sum(self.gols)
        self.media_gols=self.total_gols/self.partidas

    def exibir_dados(self):
        '''Exibe os dados gerais do jogador'''        
        sleep(2)
        print(f'{"+"*30}\n{"Dados do jogador":^30}\n{"+"*30}')
        sleep(2)
        print(f'Nome: {self.nome}')
        print(f'Partidas: {self.partidas}')
        print(f'Gols: {self.gols}')
        print(f'Total de gols: {self.total_gols}')
        print(f'Média de gols por partida: {self.media_gols:.2f}')

    def exibir_partidas_gols(self):
        '''Exibe o número de gols por partida'''
        print(f'{"+"*30}\n{"Gols por partida":^30}\n{"+"*30}')
        sleep(2)
        for k,v in enumerate(self.gols):
            sleep(0.7)
            print(f'Na partida {k+1} fez {v} gols.')
        sleep(0.5)
        print(f'Total de {self.total_gols} gols.\nMédia de gols por partida: {self.media_gols:.2f} ')            

def cabecalho():
    '''Exibe o cabeçalho'''        
    print(f'{"="*30}\n{"Rendimento do jogador":^30}\n{"="*30}\n{"Insira os dados abaixo:"}')
    sleep(0.7)

def main():
    cabecalho()
    nome=input('Nome: ').capitalize()
    sleep(0.5)
    partidas = int(input('Quantidade de partidas: '))
    jogador = Jogador(nome,partidas)
    jogador.adicionar_gols()
    jogador.exibir_dados()
    jogador.exibir_partidas_gols()

main()    



