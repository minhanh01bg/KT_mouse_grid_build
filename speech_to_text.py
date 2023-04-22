import os
import speech_recognition as sr
import time 
import wikipedia
import datetime
import json
import webbrowser
import requests
from gtts import gTTS
from youtube_search import YoutubeSearch
import pygame
import winsound
import json

frequency = 1500  # Set Frequency To 2500 Hertz
duration = 350  # Set Duration To 250 ms == 0.25 second
wikipedia.set_lang("vi")
language = 'vi'
# path = ChromeDriverManager().install()


def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text,lang = language,slow=False,tld="com")
    sound_file = "sound.mp3"
    tts.save(sound_file)

    pygame.init()

    # sound_file = sound_file
    sound = pygame.mixer.Sound(sound_file)

    sound.play()

    while pygame.mixer.get_busy():
        pygame.time.wait(100)
    os.remove(sound_file)
    pygame.quit()




def get_audio(check):
    r = sr.Recognizer()
    if check == True:
        winsound.Beep(frequency, duration)
    import time
    time.sleep(1)
    print("Tôi: ",end='')
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=3)
        try:
            text = r.recognize_google(audio,language="vi-VN")
            # print(text)
            text = text.lower()
            return text
        except:
            print("...")
            return 0

def stop():
    speak("tạm biệt bạn")

def get_number(text):
    if "một" in text or "1" in text:
        return 1
    elif "hai" in text or "2" in text:
        return 2
    elif "ba" in text or "3" in text:
        return 3
    elif "bốn" in text or "4" in text:
        return 4
    elif "năm" in text or "5" in text or "nam" in text:
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

def get_text(check):
    for i in range(2000000):
        text = get_audio(check)
        if text:
            return text.lower()
        if i < 5 and check == True:
            speak("Tôi không nghe rõ bạn nói.")
    time.sleep(2)
    # stop()
    return 0

def current_weather(check):
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text(check)
    # city = "hà nội"
    # print(f"Toi: {city}")
    # if not city:
    #     pass
    # api_key = "fe8d8c65cf345889139d8e545f57819a"
    api_key = "ce7491f834dcb997dc573482d7837bba"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    # save data weather to json file
    outfile = open('./data/weather.json', 'w')
    json.dump(data, outfile)
    outfile.close()

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
        Độ ẩm là {humidity} phần trăm.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        weather_dict = {
            "clear sky": "trời quang đãng",
            "few clouds": "trời có vài đám mây",
            "scattered clouds": "trời có nhiều đám mây rải rác",
            "broken clouds": "trời có mây rải rác",
            "overcast clouds": "trời u ám vì có mây dày đặc",
            "light rain": "trời mưa nhẹ",
            "moderate rain": "trời mưa vừa",
            "heavy intensity rain": "trời mưa to",
            "thunderstorm": "trời có sấm sét và mưa to ",
            # "snow": "trời có tuyết rơi",
            # "mist": "trời có sương mù",
            # "fog": "trời có sương mù",
            }
        if weather_description in weather_dict:
            content = content + f"\n        Thời tiết hiện tại là {weather_dict[weather_description]}"
        
        speak(content)
        time.sleep(20)
    else:
        speak("Không tìm thấy địa chỉ của bạn")

def weather(check):
    speak("bạn muốn xem thời tiết ở đâu.")
    text = get_text(check)
    url = f"https://nchmf.gov.vn/kttvSite/vi-VN/1/Search.html?s={text}&pageindex=1"
    webbrowser.open(url)
    speak(f"bạn đang xem thời tiết ở {text}")

def play_music(check):
    speak("bạn muốn nghe bài hát gì ạ.")
    mysong = get_text(check)
    print(f"{mysong}")
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
        
    url = "https://www.youtube.com" + result[0]["url_suffix"]
    webbrowser.open(url)
    print("Đang phát bài hát " + mysong)

def read_news(check):
    print("Bạn muốn đọc báo về gì")
    
    queue = get_text(check)
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

def read_news1(check):
    speak("bạn muốn đọc báo về gì")
    
    queue = get_text(check)

    print(f"{queue}")
    url = f"https://thanhnien.vn/tim-kiem.htm?keywords={queue}"
    webbrowser.open(url)
    speak(f"đang đọc báo về {queue}")

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
    else:
        speak("Tôi không hiểu bạn nói gì")

def get_time1():
    url = "https://time.is/vi/Hanoi"
    webbrowser.open(url)

def open_application(text):
    if "google" in text:
        speak("đang mở google")
        os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
    elif "word" in text:
        speak("đang mở word")
        os.startfile("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")
    elif "excel" in text:
        speak("đang mở excel")
        os.startfile("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
    else:
        speak("Ứng dụng bạn muốn mở không có trong danh sách")

# if __name__ == "__main__":
#     play_music()