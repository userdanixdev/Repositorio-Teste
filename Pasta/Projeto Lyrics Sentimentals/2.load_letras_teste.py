#  Agora que você tem as letras das músicas salvas,
#  o próximo passo é processar essas letras para extrair informações relevantes.
#  Vamos dividir essa parte do projeto em etapas menores:
# 1.Carregar e Ler as Letras:
# 2.Criar uma função para ler as letras das músicas salvas.

import os

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

def main():
    print('Carregando letras de músicas de Metalcore...')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    lyrics_dir = os.path.join(current_dir,'lyrics')     
    lyrics_data = load_lyrics(lyrics_dir)
    if not lyrics_data:
        print("Nenhuma letra foi carregada. Verifique se o diretório 'lyrics' existe e contém arquivos de letras.")
        return
    
    for artist,songs in lyrics_data.items():
        print(f"\n{artist}:")
        for title,lyrics in songs.items():
            print(f"\nLetra de {title}:\n")
            print(lyrics[:100]+ '...')
            print('-'*40)

if __name__=='__main__':

    main()                               