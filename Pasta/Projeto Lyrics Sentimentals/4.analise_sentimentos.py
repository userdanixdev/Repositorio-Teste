# Agora que temos as letras das músicas carregadas, podemos seguir para os próximos passos do projeto:
# Análise de Frequência de Palavras: Contar a frequência das palavras nas letras para identificar as mais comuns.
# Análise de Sentimento: Analisar o sentimento das letras para identificar temas e emoções predominantes.
# Visualizações Gráficas: Criar gráficos para visualizar os dados coletados.

# Abaixo está o código para contar a frequência das palavras nas letras carregadas:

# Contagem das palavras:
from wordcloud import WordCloud
import string
import os
import re
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

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

# Carregar os dados das letras de músicas
current_dir = os.path.dirname(os.path.abspath(__file__))
lyrics_dir = os.path.join(current_dir, 'lyrics')
lyrics_data = load_lyrics(lyrics_dir)

def word_frequency(lyrics_data):

    all_words = []
    for artist, songs in lyrics_data.items():
        for song,lyrics in songs.items():
            words = re.findall(r'\b\w+\b', lyrics.lower())
            all_words.extend(words)
    word_count = Counter(all_words)
    return word_count

# Calcular a frequência das palavras:
word_counts = word_frequency(lyrics_data)
# MOstrar as 10 palavras mais comuns:
print(word_counts.most_common(10))

def analyze_sentiment(lyrics_data):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_data = {}
    for artist,songs in lyrics_data.items():
        sentiment_data[artist]= {}
        for song,lyrics in songs.items():
            sentiment = analyzer.polarity_scores(lyrics)
            sentiment_data[artist][song]=sentiment
    return sentiment_data

# Analisar o sentimento das letras:
sentiment_data = analyze_sentiment(lyrics_data)
# Mostrar o resultado de sentimento para a primeira música de um artista:
first_artist = list(sentiment_data.keys())[0]
first_song = list(sentiment_data[first_artist].keys())[0]
print(f"Sentimento para {first_artist} - {first_song}: {sentiment_data[first_artist][first_song]}")             


def plot_word_frequency(word_counts, top_n=10):

    common_words = word_counts.most_common(top_n)
    words = [word for word, count in common_words]
    counts = [count for word, count in common_words]

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color='blue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top Word Frequencies in Metalcore Lyrics')
    plt.show()

# Plotar a frequência das palavras
# plot_word_frequency(word_counts)

def generate_wordcloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud das Palavras Mais Frequentes')
    plt.show()

# Gerar e exibir a nuvem de palavras
generate_wordcloud(word_counts)