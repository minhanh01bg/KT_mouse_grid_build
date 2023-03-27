import os
import playsound
import speech_recognition as sr
import time 
import sys 
import ctypes
import wikipedia
import datetime
import json
import re 
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch


wikipedia.set_lang("vi")
language = 'vi'
path = ChromeDriverManager().install()


def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text,lang = language,slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3",False)
    os.remove("sound.mp3")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ",end='')
        audio = r.listen(source,phrase_time_limit=2)
        try:
            text = r.recognize_google(audio,language="vi-VN")
            # print(text)
            text = text.lower()
            return text
        except:
            print("...")
            return 0

def stop():
    print("Tạm biệt bạn")
    # return SystemExit(0)

def get_number(text):
    if "một" in text or "1" in text:
        return 1
    elif "hai" in text or "2" in text:
        return 2
    elif "ba" in text or "3" in text:
        return 3
    elif "bốn" in text or "4" in text:
        return 4
    elif "năm" in text or "5" in text:
        return 5
    elif "sáu" in text or "6" in text:
        return 6
    elif "bảy" in text  or "7" in text:
        return 7
    elif "tám" in text or "8" in text:
        return 8
    elif "chín" in text  or "9" in text:
        return 9
    else:
        return -1

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        if i < 2:
            print("Bot: Tôi không nghe rõ bạn nói, bạn nói lại được không?")
    time.sleep(2)
    stop()
    return 0
# get_text()
def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        speak("Bạn cần Bot có thể giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            # if "điều khiển chuột" in text:
            if "chuột" in text:
                speak("Chọn số")
                text = get_text()
                if not text:
                    break
                number = get_number(text)
                if number == -1:
                    speak("Bạn chọn sai số")
                    break
                
                speak("Bạn chọn số {}".format(number))
            else:
                speak("Bạn cần Bot giúp gì ạ?")