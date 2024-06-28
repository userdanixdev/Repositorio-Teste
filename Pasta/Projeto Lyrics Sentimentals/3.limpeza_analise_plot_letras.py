# Passo 1: Análise de Frequência de Palavras:
# Vamos começar analisando a frequência de palavras nas letras das músicas. Para isso, usaremos a biblioteca collections do Python para contar as palavras.
# Passo 2: Limpeza e Preprocessamento das Letras
# Para uma análise precisa, precisamos limpar e preprocessar as letras, removendo pontuações, convertendo para minúsculas e removendo palavras comuns (stopwords).

# 1. Copiei o carregamento da letra do arquivo.py teste
# 2. Limpeza:

import os
import string   # Para a limpeza 
from collections import Counter   # Análise de frequencia de palavras
import matplotlib.pyplot as plt   # Gráficos
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_lyrics(directory):

    lyrics_data = {}
    if not os.path.exists(directory):
        print(f"Erro: O diretório especificado {directory} não foi encontrado.")
        return lyrics_data
    for artist in os.listdir(directory):
        artist_dir = os.path.join(directory,artist)
        if os.path.isdir(artist_dir):
            lyrics_data[artist]={}
            for song_file in os.listdir(artist_dir):
                if song_file.endswith('.txt'):
                    with open(os.path.join(artist_dir,song_file),'r',encoding='utf-8')as file:
                        title = song_file.replace('_',' ').replace('.txt','')
                        lyrics_data[artist][title] = file.read()
    return lyrics_data

def clean_txt(text):
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    words = text.split()
    return words

def analyze_sentiment(lyrics_data):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_data = {}
    for artist,songs in lyrics_data.items():
        sentiment_data[artist]= {}
        for song,lyrics in songs.items():
            sentiment = analyzer.polarity_scores(lyrics)
            sentiment_data[artist][song]=sentiment
    return sentiment_data

def analyze_word_frequency(lyrics_data):

    all_words=[]
    for artist,songs in lyrics_data.items():
        for title,lyrics in songs.items():
            words = clean_txt(lyrics)
            all_words.extend(words)
    word_counts = Counter(all_words)       
    return word_counts

def plot_word_frequency(word_counts,top_n=20):

    most_common_words = word_counts.most_common(top_n)             
    words = [word for word,count in most_common_words]
    counts = [count for word, count in most_common_words]

    plt.figure(figsize=(10,6))
    plt.bar(words,counts,color='skyblue')
    plt.xlabel('Palavras')
    plt.ylabel('Frequência')
    plt.title('Top 20 Palavras Mais Frequentes')
    plt.xticks(rotation=45)
    plt.show()

# Mesma função do arquivo teste 'load_letras.py':

def main():

    print('Carregando letras de músicas de Metalcore...')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lyrics_dir = os.path.join(current_dir,'lyrics')     
    lyrics_data = load_lyrics(lyrics_dir)
    if not lyrics_data:
        print("Nenhuma letra foi carregada. Verifique se o diretório 'lyrics' existe e contém arquivos de letras.")
        return
    
    #for artist,songs in lyrics_data.items():
    #   print(f"\n{artist}:")
     #   for title,lyrics in songs.items():
     #       print(f"\nLetra de {title}:\n")
      #      print(lyrics[:100]+ '...')
       #     print('-'*40)
    # Aqui está o pulo do gato:
   
    # Calculo das frequências e plote:           
    # word_counts = analyze_word_frequency(lyrics_data)
    # plot_word_frequency(word_counts)
    
    # Analisar o sentimento das letras
    sentiment_data = analyze_sentiment(lyrics_data)
    
    # Mostrar o resultado de sentimento para todas as músicas
    for artist, songs in sentiment_data.items():
        print(f"\nSentimentos para as músicas de {artist}:")
        for song, sentiment in songs.items():
            print(f"{song}: {sentiment}")

if __name__=='__main__':
    main()    