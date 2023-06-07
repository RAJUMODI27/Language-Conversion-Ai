import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from translate import Translator
from playsound import playsound


def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    print(translation)
    return translation

def speakers(user_words, lang):
    tts = gTTS(text=user_words, lang=lang)
    tts.save("temp.mp3")
    playsound("temp.mp3")

def speaker(user_words):
    engine= pyttsx3.init()
    engine.say(user_words)
    engine.runAndWait()


def command():
    speaker("Hello sir, this is VOice Translation AI, ")
    speaker("Sir can you please choose the output language which are displayed on screen ")
    languages = {
        "English": "en",
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Dutch": "nl",
        "Russian": "ru",
        "Japanese": "ja",
        "Chinese (Simplified)": "zh-CN",
        "Chinese (Traditional)": "zh-TW",
        "Korean": "ko",
        "Arabic": "ar",
        "Hindi": "hi",
        "Bengali": "bn",
        "Tamil": "ta",
        "Urdu": "ur"
    }
    print(*languages.keys())
    lan=input("Write your language's specific key")
    for lans,key in languages.items():
        if lans==lan:
            speaker(f"Sir.., your  Out put language is {lans}")
            speaker("You may start Speaking now")
            y=takeCommand()
            tr=translate_text(y,key)
            speakers(tr,key)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=5 )  # Add timeout parameter

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f"User spoke: {query}\n")

        return query

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
command()

