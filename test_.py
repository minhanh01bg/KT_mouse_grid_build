import speech_recognition as sr
import winsound
import requests
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 450  # Set Duration To 250 ms == 0.25 second

def get_audio(check):
    r = sr.Recognizer()
    if check == True:
        winsound.Beep(frequency, duration)
    print("Tôi: ",end='')
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=4)
        # save audio file to mp3
        with open("./data/audio.mp3", "wb") as f:
            f.write(audio.get_wav_data())
        try:
            url = 'https://api.fpt.ai/hmi/asr/general'
            payload = open('./data/audio.mp3', 'rb').read()
            headers = {
                'api-key': 'rRUo4GpJrYNT745uHSMg8KSmLgmBhuQI'
            }

            response = requests.post(url=url, data=payload, headers=headers)

            # print(response.json())

            # import json
            # json.dump(response.json(), open('./data/c73aa685630987783156779fc73d1221.json', 'w', encoding='utf-8'), ensure_ascii=False)

            # print(json.loads(open('./data/c73aa685630987783156779fc73d1221.json', 'r', encoding='utf-8').read())['hypotheses'][0]['utterance'])

            print(response.json()['hypotheses'][0]['utterance'])
            text = response.json()['hypotheses'][0]['utterance']
            text = text.lower()
            return text
        except:
            print("...")
            return 0

get_audio(True)




