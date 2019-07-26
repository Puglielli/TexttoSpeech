import pyttsx3
from gtts import gTTS
import urllib3

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#engine.say("Hello World!")
#engine.say('My current speaking rate is ' + str(rate))

#engine.say("olá")
#engine.runAndWait()
#engine.stop()

def format(text):
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    text = text[:10]
    text = "audio_" + text + ".wav"
    return text



text = ('''
    Sua ligação será transferida para um consultor de serviço. Para a sua segurança a ligação será gravada. 
        ''')

tts = gTTS(text=text, lang='pt')
tts.save(format(text))
print("File saved!")
