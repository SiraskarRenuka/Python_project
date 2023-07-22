import speech_recognition as sr 
from  time import ctime
import webbrowser
import time
from gtts import gTTS  
import os
import random
import playsound as p

#first step to get text what we say
r = sr.Recognizer()  #initialize recognizer

#fuction to define/ record user voice or audio
def record_audio(ask = False):
    with sr.Microphone() as source:      #use microphone
        if ask:
            alexa_speak(ask)   # we can print also 
        audio = r.listen(source)  #create object for audio
        voice_data =''
        try:
            voice_data = r.recognize_google(audio) #create object for audio recoginition 
        except sr.UnknownValueError:
            alexa_speak('Sorry, I did not get the text')  #text is not clear then occur exception, we can print also 
        except sr.RequestError:
            alexa_speak('Sorry, my speech service is down') #if the server problem occur, we can print also 
        return voice_data
    
# define function to speak 
def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang = 'en')    # create objcet for speak
    r = random.randint(1, 1000000)  # used to define random intger from 1 to 1000000
    audio_file = 'audio-' +str(r) + '.mp3'  # create audio file
    tts.save(audio_file)   # save our audio file
    p.playsound(audio_file) # play audio file using playsound
    print(audio_string)  # print the text that alexa says
    os.remove(audio_file)  # remove audio file
    
#fuction to define respond
def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak("My name is Alexa")  

    #To display current time
    if 'what time is it' in voice_data:
        alexa_speak(ctime())   #display current time

    #To search something using speech recognition
    if 'search' in voice_data:
        search = record_audio("What do you want to search for ?")
        url = 'https://google.com/search?q=' + search    #create variable to open search result
        webbrowser.get().open(url)       #open url in webbrowser
        alexa_speak("Here is what I found for " + search)

    #To find location using speech recognition
    if 'find location' in voice_data:
        location = record_audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'   #create variable to open location result
        webbrowser.get().open(url)       #open url in google maps
        alexa_speak("Here is the location of " + location )

    #To exit
    if 'exit' in voice_data:
        exit()


time.sleep(1) 
alexa_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)




