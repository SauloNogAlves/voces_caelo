import librosa
from random import sample
import numpy as np
import soundfile as sf
import random
# pega o arquivo para ser randomizado
frequencia = 44100
quantas_partes_divide_audio = 500
array_audio, sr = librosa.load('som_base.wav', sr = frequencia)
#diz o tamanho do array
print(f"Tmaho do array do sinal {len(array_audio)}")
print(f"Tipo do array do sinal {type(array_audio)}")

# Tamanho do array do sinal 5425014 com sr 44100
divisor = (len(array_audio)//quantas_partes_divide_audio)
print(f"Audiio dividido em {divisor} partes e depois misturado")
list_valores = []

inicio = 0
fin = divisor
for i in range(0, divisor):
    list_valores.append(array_audio[inicio:fin])
    inicio = inicio + divisor
    fin = fin + divisor
random.shuffle(list_valores)
print(f"Tamanho a lista condesada: {len(list_valores)}")
print("Gerando ruído de fundo")
lista_expandida = []
for i in list_valores:
    lista_expandida.extend(i)

print(f"Tamanho da lista expandida: {len(lista_expandida)}")

audio_aleatorio = np.array(lista_expandida)

#transforma o array misturado em arquivo de audio novamente

sf.write('ruido_branco.wav', audio_aleatorio, frequencia)
#
print("Arquivo salvo com sucesso! Localise o arquivo ruido_branco.wav na pasta do projeto.")







