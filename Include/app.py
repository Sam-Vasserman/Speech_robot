import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import random
import requests
from Include.dict import sites, apps, dictionary, greetings, anekdot
from google_trans_new import google_translator

translator = google_translator()

def translators(word, number):

    #функция переводчика. У меня есть интерфейс, но функция не подлючена к нему. Интерфейс называется translate.py #
    # 3 если с иврита на русский 4 если с русского на иврит 5 если с иврита на английский 6 если с английского на иврит#
    pronounce=''
    if number == 'с английского на русский':
        translate_text = translator.translate(word, lang_src = 'en', lang_tgt = 'rus')
        pronounce = translator.translate(word, lang_src='en', lang_tgt='rus', pronounce=True)
        print(translate_text, pronounce)
    elif number == 'с русского на английский':
        translate_text = translator.translate(word, lang_src='rus', lang_tgt='en')
        pronounce = translator.translate(word, lang_src='rus', lang_tgt='en', pronounce=True)
        print(translate_text, pronounce)
    elif number == 'с иврита на русский':
        translate_text = translator.translate(word, lang_src='he', lang_tgt='rus')
        print(translate_text, pronounce)
    elif number == 'с руссого на иврит':
        translate_text = translator.translate(word, lang_src='rus', lang_tgt='he')
        print(translate_text, pronounce)
    elif number == 'с иврита на английский':
        translate_text = translator.translate(word, lang_src='he', lang_tgt='en')
        print(translate_text, pronounce)
    elif number == 'с английского на иврит':
        translate_text = translator.translate(word, lang_src='en', lang_tgt='he')
        print(translate_text, pronounce)

def talk(words):

    # Возможность программы говорить #

    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Привет, спроси меня что-то")

def command():

    # Слушает человека #

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажи что-то")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали", task)
    except sr.UnknownValueError:
        talk("Я вас не понимаю")
        task = command()

    return task

def openWebSite(task):

    #  Открывает сайт#

    if task in sites:
        talk("Уже открываю")
        webbrowser.open(sites['task'])

def openApp(task):

    # Открыть приложение на компьютере #

    if apps[task] == 0 or apps[task] ==4:
        os.startfile(r'"C:\Users\Sweet\AppData\Roaming\Telegram Desktop\Telegram.exe"')
    elif apps[task] == 1 or apps[task] ==5:
        os.startfile(r'C:\Users\Sweet\AppData\Local\Viber\Viber.exe')
    elif apps[task] == 2 or apps[task] == 6:
        os.startfile(r'C:\Users\Sweet\AppData\Roaming\Zoom\bin\Zoom.exe')

def makeSomething(task):
    # Выбор человека и расспределение по функциям. #
    if task in dictionary:
        talk(dictionary[task])
        if task == 'открой веб-сайт':
            talk("Какой именно сайт вы хотите, чтобы я открыла?")
            url = command()
            if url == 'google':
                talk("Что найти в гугле?")
                url = command()
                webbrowser.open('https://www.google.com/search?q=' + url)
            else:
                webbrowser.open(sites[url])

    elif task in apps:
        openApp(task)

    elif task == 'открой почту':
        webbrowser.open('https://mail.google.com/')

    elif task == 'какая погода сегодня':
        webbrowser.open('https://pogoda.co.il/israel/')

    elif task == 'какая погода на завтра':
        webbrowser.open('https://meteo.orbita.co.il/')

    elif task == 'привет':
        talk(random.choice(greetings))

    elif task == 'расскажи анекдот':
        talk(random.choice(anekdot))

    elif task == 'открой переводчик' or task =='переводчик':
        talk("С какого языка на какой перевести?")
        number = command()
        talk('напиши что я могу перевести')
        translators(command(), number)
    else:
        talk('У вас нет такой программы или приложения или я еще просто слишком маленькая, чтобы уметь так')


while True:
    makeSomething(command())
