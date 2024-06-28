# Após coletar os dados e salvar na área correta, basta carregá-los:
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_lyrics(directory):

    lyrics_data = {}
    if not os.path.exists(directory):
        print(f'Erro: O diretório especificado {directory} não foi encontrado.')
        return lyrics_data
    for artist in os.listdir(directory):
        artist_dir = os.path.join(directory,artist)
        if os.path.isdir(artist_dir):
            lyrics_data[artist]={}
            for song_file in os.listdir(artist_dir):
                if song_file.endswith('.txt'):
                    with open (os.path.join(artist_dir,song_file),'r',encoding='utf-8') as file:
                        title=song_file.replace('_',' ').replace('.txt','')
                        lyrics_data[artist][title]=file.read()
    return lyrics_data       

# Carregar os dados das letras de músicas:
current_dir = os.path.dirname(os.path.abspath(__file__))
lyrics_dir = os.path.join(current_dir, 'lyrics')
lyrics_data = load_lyrics(lyrics_dir)                 

def analyze_sentiment(lyrics_data):

    analyzer = SentimentIntensityAnalyzer()
    sentiment_data = {}
    for artist,songs in lyrics_data.items():
        sentiment_data[artist]={}
        for song,lyrics in songs.items():
            sentiment = analyzer.polarity_scores(lyrics)
            sentiment_data[artist][song]=sentiment
    return sentiment_data

def main():

    print('Carregando letras de músicas de Metalcore...')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lyrics_dir = os.path.join(current_dir,'lyrics') 
    lyrics_data = load_lyrics(lyrics_dir)
    if not lyrics_data:
        print("Nenhuma letra foi carregada. Verifique se o diretório 'lyrics' existe mesmo, talvez esteja no lugar errado.")           
        return

    sentiment_data = analyze_sentiment(lyrics_data)  

# Mostrar o resultado de sentimento para todas as músicas:
    for artist,songs in sentiment_data.items():
        print(f"\nSentimento para as músicas de {artist}:")
        for song,sentiment in songs.items():
            print(f"{song}: {sentiment}")

if __name__=='__main__':
    main()           
