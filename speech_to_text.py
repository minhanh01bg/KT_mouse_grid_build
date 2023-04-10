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
import pyttsx3
import pygame

wikipedia.set_lang("vi")
language = 'vi'
path = ChromeDriverManager().install()


def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text,lang = language,slow=False)
    tts.save("sound.mp3")

    pygame.init()

    sound_file = "sound.mp3"
    sound = pygame.mixer.Sound(sound_file)

    sound.play()

    while pygame.mixer.get_busy():
        pygame.time.wait(100)
    os.remove("sound.mp3")
    pygame.quit()

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
    for i in range(10):
        text = get_audio()
        if text:
            return text.lower()
        if i < 2:
            print("Bot: Tôi không nghe rõ bạn nói, bạn nói lại được không?")
    time.sleep(2)
    stop()
    return 0

def current_weather():
    print("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    print(f"Toi: {city}")
    if not city:
        pass
    # api_key = "fe8d8c65cf345889139d8e545f57819a"
    api_key = "ce7491f834dcb997dc573482d7837bba"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        print(content)
        time.sleep(20)
    else:
        print("Không tìm thấy địa chỉ của bạn")

def weather():
    print("Bạn muốn xem thời tiết ở đâu.")
    text = get_text()
    url = f"https://nchmf.gov.vn/kttvSite/vi-VN/1/Search.html?s={text}&pageindex=1"
    webbrowser.open(url)
    print(f"Bạn đang xem thời tiết ở {text}")

def play_music():
    print("Bot: Bạn muốn nghe bài hát gì ạ.")
    mysong = get_text()
    print(f"{mysong}")
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
        
    url = "https://www.youtube.com" + result[0]["url_suffix"]
    webbrowser.open(url)
    print("Đang phát bài hát " + mysong)

def read_news():
    print("Bạn muốn đọc báo về gì")
    
    queue = get_text()
    print(f"Toi: {queue}")
    params = {
        # 'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        'apiKey': 'f77bb94ff7b24fd7a2031230edf0f017',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}""")
        if number <= 3:
            webbrowser.open(result['url'])

def read_news1():
    print("Bot: Bạn muốn đọc báo về gì")

    queue = get_text()

    print(f"{queue}")
    url = f"https://thanhnien.vn/tim-kiem.htm?keywords={queue}"
    webbrowser.open(url)
    print(f"Bot: Đang đọc báo về {queue}")

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        print("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
    elif "ngày" in text:
        print("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
    else:
        print("Tôi không hiểu bạn nói gì")

def get_time1():
    url = "https://time.is/vi/Hanoi"
    webbrowser.open(url)

def open_application(text):
    if "google" in text:
        print("Mở google")
        os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
    elif "word" in text:
        print("Mở word")
        os.startfile("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")
    elif "excel" in text:
        print("Mở excel")
        os.startfile("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
    else:
        print("Ứng dụng bạn muốn mở không có trong danh sách")

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