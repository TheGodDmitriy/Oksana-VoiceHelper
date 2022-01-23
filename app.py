import speech_recognition as sr
from os import system
import sys
import webbrowser
import pyttsx3
from datetime import datetime
import time
import datetime
import random
import pywhatkit
from fuzzywuzzy import fuzz
from random import choice
import wikipedia
from colorama import init
init()
from colorama import Fore
from pyowm import OWM
from pyowm.utils.config import get_default_config
import keyboard
import subprocess
import psutil
import os


class Speaking:

    def talk(self,words):
        engine.say(words)
        engine.runAndWait()

class MicRecognition:

    def command(self):
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source)
            print(Fore.CYAN + 'Оксана: ...')
            audio = rec.listen(source)
        try:
            text = rec.recognize_google(audio, language="ru-RU").lower()
            print(Fore.YELLOW + 'Вы:  ' + text[0].upper() + text[1:])

            print('Нажмите "Enter" чтобы продолжить!')
            #Если не распознался тест из аудио
        except sr.UnknownValueError:
            text = random.choice("Прости, я тебя не понимаю.", "Мне не понятен твой вопрос.")
            print(Fore.CYAN + 'Оксана: ' + text)
            talk(text)
                #Начинаем заново слушать
            text = command()

        return text

class Functions:

    def shut(self):
        speak.talk("Подтвердите действие!")
        text = mic.command()
        print(Fore.YELLOW + text)
        if (fuzz.ratio(text, 'подтвердить') > 60) or (fuzz.ratio(text, "подтверждаю") > 60):
            speak.talk('Действие подтверждено')
            speak.talk('До скорых встреч!')
            system('shutdown /s /f /t 10')
            self.quite()
        elif fuzz.ratio(text, 'отмена') > 60:
            speak.talk("Действие не подтверждено")
        else:
            speak.talk("Действие не подтверждено")

    def weather(self, city):
        config_dict = get_default_config()
        config_dict['language'] = 'ru'

        owm = OWM('b3c43004803c76a31c2d338df6c88b06', config_dict)
        mgr = owm.weather_manager()

        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place(city)
        w = observation.weather

        detail = w.detailed_status         # 'clouds'
        temp = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

        speak.talk('Сейчас в городе ' + city + ' ' + detail + ' и температура ' + str(temp['temp']) + ' по Цельсию')

    def dream(self):
        speak.talk('Подтвердите действие!')
        text = mic.command()
        print(Fore.YELLOW + text)
        if (fuzz.ratio(text, 'подтвердить') > 60) or (fuzz.ratio(text, "подтверждаю") > 60):
            speak.talk('Действие подтверждено')
            speak.talk('До скорых встреч!')
            system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            self.quite()
        elif fuzz.ratio(text, 'отмена') > 60:
            speak.talk("Действие не подтверждено")
        else:
            speak.talk("Действие не подтверждено")

    def restart(self):
        speak.talk('Подтвердите действие!')
        text = mic.command()
        print(Fore.YELLOW + text)
        if (fuzz.ratio(text, 'подтвердить') > 60) or (fuzz.ratio(text, "подтверждаю") > 60):
            speak.talk('Действие подтверждено')
            speak.talk('До скорых встреч!')
            system(['shutdown', '-r' '-t' ,'0'])
            self.quite()
        elif fuzz.ratio(text, 'отмена') > 60:
            speak.talk("Действие не подтверждено")
        else:
            speak.talk("Действие не подтверждено")

    def quite(self):
        quit = choice(['Надеюсь мы скоро увидимся', 'Рада была помочь', 'Я отключаюсь'])
        print(Fore.CYAN + quit)
        speak.talk(quit)
        engine.stop()
        system('cls')
        sys.exit(0)

    def open_steam(self):
        subprocess.call('D:/Steam/steam.exe')
        time.sleep(5)
        for process in (process for process in psutil.process_iter() if process.name()=="steam.exe"):
            process.kill()

    def open_telegram(self):
        subprocess.call('D:/Telegram Desktop/Telegram.exe')
        time.sleep(5)
        for process in (process for process in psutil.process_iter() if process.name()=="steam.exe"):
            process.kill()

    def open_discord(self):
        subprocess.call('C:/Users/Дмитрий/AppData/Local/Discord/Update.exe --processStart Discord.exe')
        time.sleep(5)
        for process in (process for process in psutil.process_iter() if process.name()=="steam.exe"):
            process.kill()

    def open_taskmgr(self):
        os.startfile('C:/WINDOWS/system32/Taskmgr.exe','runas')

    def who(self):
        print(Fore.CYAN + 'Да, мой повелитель?')
        speak.talk('Да, мой повелитель?')

    def music(self, text):
        song = text.replace('включи музыку', '')
        print(Fore.CYAN + 'Включаю музыку' + song)
        speak.talk('включаю музыку' + song)
        pywhatkit.playonyt(song)

    def browser(self):
        print(Fore.CYAN + 'Открываю Google')
        speak.talk('Открываю Google')
        webbrowser.open('https://www.google.com/')

    def vk(self):
        print(Fore.CYAN + 'Открываю Вконтакте')
        speak.talk('Открываю Вконтакте')
        webbrowser.open('https:vk.com/feed')

    def twitch(self):
        print(Fore.CYAN + 'Открываю Twitch')
        speak.talk('Открываю Twitch')
        webbrowser.open('https://www.twitch.tv/')

    def wiki(self, info):
        speak.talk('Произвожу поиск в Wikipedia')
        wikipedia.set_lang("ru")
        print(Fore.CYAN + wikipedia.summary(info, sentences=1))
        speak.talk(wikipedia.summary(info, sentences=1))

    def mail(self):
        print(Fore.CYAN + 'Открываю почту')
        speak.talk('Открываю почту')
        webbrowser.open('http:gmail.com/')

    def youtube(self):
        print(Fore.CYAN + 'Открываю Youtube')
        speak.talk('Открываю Youtube')
        webbrowser.open('https://youtube.com/')

    def game(self):
        money = random.randint(1, 2)
        if money == 1:
            speak.talk('У вас решка!')
        else:
            speak.talk('Выпал орел!')


    def makeSomething(self, text):

        if 'оксана' == text:
            self.who()

        elif 'включи музыку' in text:
            self.music(text = text)

        elif 'открой браузер' == text:
            self.browser()

        elif 'открой вконтакте' == text:
            self.vk()

        elif 'открой twitch' == text:
            self.twitch()

        elif 'что значит' in text:
            self.wiki(info = text.replace('что значит', ''))

        elif 'кто такой' in text:
            self.wiki(info = text.replace('кто такой', ''))

        elif 'что такое' in text:
            self.wiki(info = text.replace('что такое', ''))

        elif 'открой почту' == text:
            self.mail()

        elif 'открой youtube' == text:
            self.youtube()

        elif 'погода' == text:
            speak.talk('Произнисите город!')
            city = mic.command()
            city = city.upper()
            self.weather(city=city)

        elif 'подбрось монетку' == text:
            self.game()

        elif 'открой steam' == text:
            self.open_steam()

        elif 'открой telegram' == text:
            self.open_telegram()

        elif 'открой discord' == text:
            self.open_discord()

        elif 'запусти диспетчер задач' == text:
            self.open_taskmgr()

        elif 'включи спящий режим' == text:
            self.dream()

        elif 'перезагрузи компьютер' == text:
            self.restart()

        elif 'выключи компьютер' == text:
            self.shut()

        elif 'пока' == text:
            speak.talk('Пока-пока!')
            self.quite()


if __name__ == '__main__':

    speak = Speaking()
    mic = MicRecognition()
    func = Functions()

    engine = pyttsx3.init('sapi5')                    # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
    words = engine.getProperty('voices')
    engine.setProperty("rate", 145)         # gets you the details of the current voices
    engine.setProperty('voice', words[9].id)

    key = 'Enter'

    speak.talk('Привет, меня зовут Оксана! Что я могу для вас сделать?')
    print(Fore.CYAN + 'Привет, меня зовут Оксана! Что я могу для вас сделать?')
    print(Fore.YELLOW + 'Нажмите "Enter" чтобы продолжить!')


    while True:
        if keyboard.is_pressed(key):
            func.makeSomething(mic.command())
