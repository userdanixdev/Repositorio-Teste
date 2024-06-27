# Passos para Coleta de Letras de Músicas por API:
# Escolha da API:

# Encontre uma API que forneça acesso às letras de músicas. Existem várias opções disponíveis, como Musixmatch, Genius, Lyrics.ovh, entre outras. Cada uma tem suas próprias políticas de uso e limitações.
# Registro e Autenticação:

# Algumas APIs podem exigir registro para obter uma chave de API (API key). Registre-se na API escolhida e obtenha sua chave de API, se necessário. Isso geralmente envolve criar uma conta no site da API e gerar uma chave de acesso.
# Leitura da Documentação da API:

# Leia a documentação fornecida pela API para entender como fazer solicitações para obter as letras de músicas. Isso inclui os endpoints disponíveis, os parâmetros de consulta necessários, e exemplos de solicitações e respostas.
# Implementação em Python:

# Utilize bibliotecas Python como requests para fazer solicitações HTTP à API e json para lidar com os dados de resposta em formato JSON.

# Aqui está um exemplo básico de como você pode começar a implementar a coleta de letras de músicas usando
#  a API Lyrics.ovh, que é simples e não requer autenticação:

# Nesse caso vou usar o consumo de API pública, sem autenticação
# Instalei a dependência 'requests' que não estava instalada.

import requests
import os

def get_lyrics(artist, title):
    base_url = "https://api.lyrics.ovh/v1"
    endpoint = f"{base_url}/{artist}/{title}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return data['lyrics']
    else:
        return None

def save_lyrics(artist,title,lyrics):
    # Criar uma diretório atual:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Criar um diretório para as letras dentro do diretório atual:
    lyrics_dir=os.path.join(current_dir,'lyrics')
    os.makedirs(lyrics_dir,exist_ok=True)
    # Criar um diretorio para o artista se não existir:
    artist_dir=os.path.join(lyrics_dir,artist.replace(' ','_'))
    os.makedirs(artist_dir,exist_ok=True)
    # Criando um filename para a letra:
    filename = f"{title.replace(' ','')}.txt"
    file_path = os.path.join(artist_dir,filename)
    # Salvando a letra no arquivo:
    with open(file_path,'w',encoding='utf-8') as file:
        file.write(lyrics)
    print(f"Letras de {title} por {artist} salvas em {file_path}")

    
def main():
    print("Busca de Letras de Músicas de Metalcore")
    while True:
        artist = input("Digite o nome da banda/artista: ").strip()
        title = input("Digite o título da música: ").strip()
        if not artist or not title:
            print("Artista e título da música são obrigatórios!")
            continue
# Exemplo de uso:
#artist = "Architects"
#title = "Doomsday"

        lyrics = get_lyrics(artist, title)
        if lyrics:
            print(f"Letra de '{title}' por {artist}:\n{lyrics}")
            save_lyrics(artist,title,lyrics)
        else:
            print(f"Letra não encontrada para '{title}' por {artist}.")

        continuar = input('Deseja buscar outra letra? [S/N]').strip().lower()
        if continuar != 's':
            break

if __name__ == '__main__':
    main()

# Testando o Programa:
# Digite o nome da banda/artista: Por exemplo, digite Bring Me The Horizon.
# Digite o título da música: Por exemplo, digite Can You Feel My Heart.
# O programa fará uma solicitação à API Lyrics.ovh e, se encontrar a letra da música,
#  exibirá a letra no console. Se não encontrar, mostrará uma mensagem de erro.

