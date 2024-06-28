# A versão 3 tem como objetivo eliminar a manipulação de arquivos e usar dicionários para as
#  letras dentro da estrutura do código. Simplificando o código.

# Project Lyrics Sentimentals
# Versão 03:

import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

# Função para obter as letras das músicas. Através da API Lyrics.ovh:
# Obs: Não precisa de autenticação

def get_lyrics(artist,title):

    base_url = "https://api.lyrics.ovh/v1"
    endpoint = f"{base_url}/{artist}/{title}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data =  response.json()
        return data['lyrics']
    else:
        return None
    
# Função para salvar as letras das músicas em um dicinário:
def save_lyrics(lyrics_dict,artist,title,lyrics):

    if artist not in lyrics_dict:
        lyrics_dict[artist]= {}
    lyrics_dict[artist][title]=lyrics
    print(f"Letras de {title} por {artist} salvas no dicionário.")  

    return lyrics_dict

# Função para carregar as letras das músicas salvas no dicionário:
def load_lyrics(lyrics_dict):


    if lyrics_dict:
        print('Letras carregadas com sucesso.')
    elif not lyrics_dict:
        print('Nenhuma letra foi carregada.')    
    return lyrics_dict        

# Função para analisar o sentimento das letras das músicas:
def analyse_sentiment(lyrics_data):

    analyser = SentimentIntensityAnalyzer()
    sentiment_data = {}
    for artist,songs in lyrics_data.items():
        sentiment_data[artist] = {}
        for song, lyrics in songs.items():
            sentiment = analyser.polarity_scores(lyrics)
            sentiment_data[artist][song] = sentiment
    
    return sentiment_data       

# Função principal para coletar letras de músicas:
def collect_lyrics(lyrics_dict):

    print(f"{"+"*30}\n{"Busca de letras de Músicas": ^29}\n{"Análise de Sentimentos":^28}\n{"+"*30}")
    dots_()
    while True:
        artist = input('Digite o nome da banda/artista: ').strip()
        title = input('Digite o título da música: ').strip().capitalize()
        if not artist or not title:
            print('Artista e título são obrigatórios.')     
            continue
        lyrics = get_lyrics(artist,title)
        if lyrics:
            print(f"Letra de {title} por {artist}:\n {lyrics}")
            save_lyrics(lyrics_dict,artist,title,lyrics)
        else:
            print(f'letra não encontrada para {title} por {artist}')
        continuar = input('Deseja buscar outra letra? [S/N]: ').strip().lower()
        if continuar != 's':
            break

# Função para deletar as letras das músicas:
def delete_lyrics(lyrics_dict):
    lyrics_dict.clear()
    print('Todas as letras foram deletadas do dicionário.')                                

def analysis_lyrics(lyrics_data):
    # Verificar se há letras para analisar:
    if not lyrics_data:
        print('Nenhum letra carregada no momento.')
        return False
    
    # Analisar o sentimento das letras das músicas:
    sentiment_data =  analyse_sentiment(lyrics_data)

    # Mostrar o resultado de sentimento para todas as músicas:
    for artist,songs in sentiment_data.items():
        print(f"\nSentimento para as músicas de {artist}:")
        for song,sentiment in songs.items():
            neg_percent = sentiment['neg']*100
            pos_percent = sentiment['pos']*100
            neu_percent = sentiment['neu']*100
            compound_score = sentiment['compound']
            print(f"{song}:")
            print(f" Negativo: {neg_percent:.2f}%")
            print(f" Positivo: {pos_percent:.2f}%")
            print(f" Neutro:   {neu_percent:.2f}%")
            print(f" Compound: {compound_score:.4f}")

    return True

def dots_():
    for c in range(3):
        print(".",end='',flush=True)
        time.sleep(1)

def dots():
    for c in range(3):
        print(".",end='',flush=True)
        time.sleep(1)
    return print('\nCarregando dados\n\nAs letras estão prontas para serem avaliadas.')

def menu():
    lyrics_dict = {}
    lyrics_data = None
    while True:
        try:
            menu ='''
                +++++++++++ MENU +++++++++++
                [1] - Coletar letras
                [2] - Carregar letras
                [3] - Deletar letras
                [4] - Análise de Sentimento
                [5] - Sair
            \nEscolha:  '''
            opcoes = int(input(menu))
            if opcoes == 1:
                collect_lyrics(lyrics_dict)
            elif opcoes == 2:
                lyrics_data = load_lyrics(lyrics_dict)
                if lyrics_data:
                    dots()
            elif opcoes == 3:
                delete_lyrics(lyrics_dict)
            elif opcoes == 4:
                if lyrics_data:
                    analysis_lyrics(lyrics_data)
                else:
                    print('Nenhuma letra carregada no momento.')                    
            elif opcoes == 5:
                print('Saindo...')
                break
            else:
                print('Opção inválida. Escolha somente entre os números de 1 a 5.')
        except ValueError:
            print('Opção inválida. Insira somente números inteiros.')

if __name__=='__main__':
    menu()
                                                            
        

