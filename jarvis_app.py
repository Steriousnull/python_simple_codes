import pyttsx3  #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import comtypes.client

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # Corrected hour extraction
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am Ryzen, Please tell me how may I help you")



def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")



    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()


        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = r'C:\Users\c24a1\Music\2024 music'
            print(songs)
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[0]))



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
 


        
