### PYTUBE THE VIBE
import os
from pytube import YouTube,Playlist
from moviepy.editor import *
def multipleReplace(text):
    for char in ":.?,|#/*//\"\'":
        text = text.replace(char,"")
    return text

def toMp3(youtubeVideo,caminho,url,nomeArquivo):
            if (not(os.path.exists(caminho+nomeArquivo+".mp3"))):
                print(f'Downloading video: {playlist_url}')
                video=youtubeVideo.streams.filter(file_extension='mp4').first()
                video.download(caminho)
                videoclip=VideoFileClip(caminho+nomeArquivo+".mp4")
                audioclip=videoclip.audio
                audioclip.write_audiofile(caminho+nomeArquivo+".mp3")
                audioclip.close()
                videoclip.close()
                os.remove(caminho+nomeArquivo+".mp4")
def toMp4(youtubeVideo,caminho,url,nomeArquivo):
            if (not(os.path.exists(caminho+nomeArquivo+".mp3"))):
                print(f'Downloading video: {playlist_url}')
                video=youtubeVideo.streams.filter(file_extension='mp4').first()
                video.download(caminho)

playlist_url=""
caminho=""
def star(playlistUrl,downloadPath,format):
    ###playlist_url = "https://www.youtube.com/watch?v=3WG0T2RU6tQ&list=RD3WG0T2RU6tQ&start_radio=1&t=1&ab_channel=CatDealers"
    caminho ="D:\\THE VIBE\\"
    playlist_url=playlistUrl
    caminho=downloadPath.replace("\\","\\\\")
    print(downloadPath)
    print(caminho)
    diretorioPadrao=False
    while(not(diretorioPadrao)):
        if os.path.exists(caminho):
         print("O diretório  ---"+caminho+"--- existe.")
         caminho=caminho+"\\\\"
         diretorioPadrao=True
        else:
         print("O diretório ---"+caminho+"--- não existe.")
         caminho=input("INSIRA UM CAMINHO VALIDO PARA DOWNLOAD---")
    
    try:
      p =Playlist(playlist_url)
      print("CAMINHO DO ARQUIVO"+caminho)
      for url in p.video_urls:
          try:
           youtubeVideo = YouTube(url)
           nomeArquivo=multipleReplace(youtubeVideo.title)
          except VideoUnavailable:
           print(f'O video {url} está indisponivel e esta sendo ignorado.')
          else:
              if(format=="mp3"):
                toMp3(youtubeVideo,caminho,playlist_url,nomeArquivo)
              else:
                toMp4(youtubeVideo, caminho, url, nomeArquivo)
      return "VIDEOS BAIXADOS COM SUCESSO!!!!"
    except KeyError:
      print("ISTO NAO É UMA PLAYLIST VALIDA")### o programa entra nessa excessao se nao for possivel obter uma playlist válida e tenta baixar um unico video
      try:
          youtubeVideo = YouTube(playlist_url)
          nomeArquivo=multipleReplace(youtubeVideo.title)
      except VideoUnavailable:
           print(f'O Video {playlist_url} está indisponivel e esta sendo ignorado.')
           return "NAO FOI POSSIVEL BAIXAR O VIDEO {playlist_url} está indisponivel:" 
      else:
            if(format=="mp3"):
                toMp3(youtubeVideo,caminho,playlist_url,nomeArquivo)
            else:
                toMp4(youtubeVideo, caminho, url, nomeArquivo)
            print("*******ALL VIDEOS DOWNLOADED********")
            return "VIDEO : "+nomeArquivo+ " BAIXADO COM SUCESSO!!!!" 
def rule():
    print("what?")
      