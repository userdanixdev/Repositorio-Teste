import requests
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from time import sleep

# Primeiro a função para obter as letras das músicas através de uma API Lyrics.ovh:
# Essa API não precisa de autenticação
def get_lyrics(artist,title):
    base_url = "https://api.lyrics.ovh/v1"
    endpoint = f"{base_url}/{artist}/{title}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return data['lyrics']
    else:
        return None

# Função para salvar as letras das músicas em arquivos de texto:
def save_lyrics(artist,title,lyrics):
    # Criar diretório atual:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Criar um diretório para as letras dentro do diretório atual:
    lyrics_dir = os.path.join(current_dir,'lyrics')
    os.makedirs(lyrics_dir,exist_ok=True)
    # Criar um diretório para o artista se não existir:
    artist_dir = os.path.join(lyrics_dir,artist.replace(' ','_'))
    os.makedirs(artist_dir,exist_ok=True)
    # Criar um filename para a letra:
    filename = f"{title.replace(' ','_')}.txt"
    file_path = os.path.join(artist_dir,filename)
    # Salvando a letra no arquivo:
    with open(file_path,'w',encoding='utf-8')as file:
        file.write(lyrics)
    print(f"Letras de {title} por {artist} salvas em {file_path}")

# Função para carregar as letras das músicas salvas em arquivos de texto:
def load_lyrics(directory):
    lyrics_data = {}
    if not os.path.exists(directory) :
        print(f'Erro: O diretório especificado {directory} não foi encontrado.')
        return lyrics_data
    for artist in os.listdir(directory):
        artist_dir = os.path.join(directory,artist)
        if os.path.isdir(artist_dir):
            lyrics_data[artist]= {}
            for song_file in os.listdir(artist_dir):
                if song_file.endswith('.txt'):
                    with open(os.path.join(artist_dir,song_file),'r',encoding='utf-8') as file:
                        title = song_file.replace('_',' ').replace('.txt','')
                        lyrics_data[artist][title] = file.read()
    return lyrics_data                                   

# Função para analisar o sentimento das letras das músicas:
def analyse_sentiment(lyrics_data):
    analyser = SentimentIntensityAnalyzer()
    sentiment_data = {}
    for artist,songs in lyrics_data.items():
        sentiment_data[artist]= {}
        for song,lyrics in songs.items():
            sentiment = analyser.polarity_scores(lyrics)
            sentiment_data[artist][song] = sentiment
    
    return sentiment_data            

# Função principal para coletar letras de músicas e analisar o sentimento:
def collect_lyrics():
    print(f"{"+"*30}\n{"Busca de letras de Músicas": ^29}\n{"Análise de Sentimentos":^28}\n{"+"*30}")
    dots_()
    while True:
            artist = input('Digite o nome da banda/artista: ').strip()
            title = input('Digite o título da música: ').strip()
            if not artist or not title:
                print('Artista e título da música são obrigatórios.')
                continue
            lyrics = get_lyrics(artist,title)
            if lyrics:
                print(f"Letra de {title} por {artist}:\n{lyrics}")
                save_lyrics(artist,title,lyrics)
            else:
                print(f'Letra não encontrada para {title} por {artist}')
            continuar = input('Deseja buscar outra letra? [S/N]: ').strip().lower()
            if continuar != 's':
                break

def prepare_lyrics():            
    # Carregar os dados das letras de músicas:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lyrics_dir = os.path.join(current_dir,'lyrics')
    lyrics_data = load_lyrics(lyrics_dir)
    if not lyrics_data:
        print("Nenhuma letra foi carregada. \nVerifique se o diretório lyrics existe mesmo,talvez esteja no lugar errado.\nOu foi deletado.")                                           
        return False
    return lyrics_data

def dots():
    for c in range(4):
        print(".",end='',flush=True)
        sleep(1)
    return print('\nCarregando dados\n\nAs letras estão prontas para serem avaliadas.')

def dots_():
    for c in range(4):
        print(".",end='',flush=True)
        sleep(1)


    
def analysis_lyrics(lyrics_data):
    # Verificar se há letras para analisar:
    if not lyrics_data:
        print('Nenhuma letra carregada no momento')
        return False
    # Analisar o sentimento das letras de músicas:
    analyser = SentimentIntensityAnalyzer()
    sentiment_data = {}
    # Mostrar o resultado de sentimento para todas as músicas:
    for artist, songs in lyrics_data.items():
        sentiment_data[artist] = {}
        for song, lyrics in songs.items():
            sentiment = analyser.polarity_scores(lyrics)
            sentiment_data[artist][song] = sentiment
    # Mostrar o resultado de sentimento para todas as músicas:
    for artist, songs in sentiment_data.items():
        print(f"\nSentimento para as músicas de {artist}:")
        for song, sentiment in songs.items():
            print(f"{song}: {sentiment}")            

# Função para deletar as letras das músicas:
def delete_lyrics():
    current_dir = os.path.dirname(os.path.abspath(__file__))            
    lyrics_dir = os.path.join(current_dir,'lyrics')
    if os.path.exists(lyrics_dir):
        for artist in os.listdir(lyrics_dir):
            artist_dir = os.path.join(lyrics_dir,artist)
            if os.path.isdir(artist_dir):
                for song_file in os.listdir(artist_dir):
                    file_path = os.path.join(artist_dir,song_file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"{file_path} foi deletado.")
                os.rmdir(artist_dir)
                print(f"{artist_dir} foi deletado")                        
        os.rmdir(lyrics_dir)
        print(f"{artist_dir} foi deletado")                                                    
    else:
        print("Nenhum diretório de letras encontrado para deletar.")        


def menu():
    while True:
        try:
            menu='''
            +++++++++++ MENU +++++++++++
            [1] - Coletar letras
            [2] - Carrega letras 
            [3] - Deletar letras
            [4] - Analise de Sentimentos
            [5] - Sair
            \nEscolha:  '''
            opcoes = int(input(menu))
            if opcoes == 1:
                collect_lyrics()
            elif opcoes == 2:
                lyrics_data=  prepare_lyrics()
                if prepare_lyrics():
                    dots()                
            elif opcoes == 3:
                delete_lyrics()
            elif opcoes == 4:
                lyrics_data = analysis_lyrics(lyrics_data)
                if lyrics_data:
                    analysis_lyrics(lyrics_data)   
                else: 
                    print('\nSempre carregue as letras antes de analisar o sentimento.')                                              
            elif opcoes == 5:
                print('Saindo...')
                break
            else:
                print('Opção inválida. Escolha um número de 1 a 5. ')    
        except ValueError:
            print('Opção inválida. Insira somente números inteiros.')
     

if __name__=='__main__':
    menu()            