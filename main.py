import speech_recognition as sr
from datetime import datetime

rec = sr.Recognizer()
data = datetime.now()
#audio_para_leitura = 'som_base.wav'
#audio_para_leitura = 'ruido_branco.wav'
audio_para_leitura = 'gravacao_14092022.wav'
#audio_para_leitura = 'muito_alto_equivocado12092022.wav'
try:
   with sr.AudioFile(audio_para_leitura) as mic:
      print(f"Estou lendo o arquivo: {audio_para_leitura} na data: {data}")
      #ouvindo o audio
      audio = rec.record(mic)
      #transformando em texto
      print('O texto da transcrição do áudio será impresso abaixo:')
      texto = rec.recognize_google(audio, language="pt-BR")
      print(texto)
except sr.UnknownValueError:
   print("Não consegui transcrever esse áudio")
except sr.RequestError as e:
   print(f"Deu o seguinte erro ao solicitar o serviço de transcrição: {e}")







