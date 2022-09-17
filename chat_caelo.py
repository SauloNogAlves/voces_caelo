import librosa
from random import sample
import numpy as np
import soundfile as sf
import random
import speech_recognition as ser
from datetime import datetime
# pega o arquivo para ser randomizado

pergunta = 'Devo participar do estudo com o Adriano do canal ponto de espiritualidade?'

frequencia = 44100
quantas_partes_divide_audio = 500
array_audio, sr = librosa.load('som_base.wav', sr = frequencia)
#diz o tamanho do array
#print(f"Tmaho do array do sinal {len(array_audio)}")
#print(f"Tipo do array do sinal {type(array_audio)}")

# Tamanho do array do sinal 5425014 com sr 44100
print(f"Gerando o áudio referente a pergunta: {pergunta}")
divisor = (len(array_audio)//quantas_partes_divide_audio)
#print(f"Audiio dividido em {divisor} partes e depois misturado")
list_valores = []

inicio = 0
fin = divisor
for i in range(0, divisor):
    list_valores.append(array_audio[inicio:fin])
    inicio = inicio + divisor
    fin = fin + divisor
random.shuffle(list_valores)
#print(f"Tamanho a lista condesada: {len(list_valores)}")
#print("Gerando ruído de fundo")
lista_expandida = []
for i in list_valores:
    lista_expandida.extend(i)

#print(f"Tamanho da lista expandida: {len(lista_expandida)}")

audio_aleatorio = np.array(lista_expandida)

#transforma o array misturado em arquivo de audio novamente

sf.write('ruido_branco.wav', audio_aleatorio, frequencia)
#
print("O áudio foi gerado com sucesso.")

#ouvindo e transcrevendo o áudio embaralhado

rec = ser.Recognizer()
data = datetime.now()
#audio_para_leitura = 'som_base.wav'
audio_para_leitura = 'ruido_branco.wav'
#audio_para_leitura = 'gravacao_14092022.wav'
#audio_para_leitura = 'muito_alto_equivocado12092022.wav'
try:
   with ser.AudioFile(audio_para_leitura) as mic:
      print(f"Estou lendo o arquivo: {audio_para_leitura} na data: {data}")
      #ouvindo o audio
      audio = rec.record(mic)
      #transformando em texto
      print('O texto da transcrição do áudio será impresso abaixo:')
      texto = rec.recognize_google(audio, language="pt-BR")
      print(texto)
except:
    texto = "Não consegui transcrever esse áudio"
    print(texto)

transcricao = f"Data: {data}; Pergunta: {pergunta}; Resposta: {texto}\n"

arquivo = open("conversas.txt", "a")
arquivo.write(transcricao)
arquivo.close()








