import speech_recognition as sr
import winsound
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 350  # Set Duration To 250 ms == 0.25 second

def get_audio(check):
    r = sr.Recognizer()
    if check == True:
        winsound.Beep(frequency, duration)
    import time
    time.sleep(1)
    print("Tôi: ",end='')
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=3)
        # save audio file to mp3
        with open("./data/audio.mp3", "wb") as f:
            f.write(audio.get_wav_data())
        try:
            import requests

            url = "https://viettelgroup.ai/voice/api/asr/v1/rest/decode_file"
            headers = {
                'token': 'anonymous',
                #'sample_rate': 16000,
                #'format':'S16LE',
                #'num_of_channels':1,
                #'asr_model': 'model code'
            }
            s = requests.Session()
            files = {'file': open('./data/audio.mp3','rb')}
            response = requests.post(url,files=files, headers=headers)

            print(response.json()[0]['result']['hypotheses'][0]['transcript'])
        except:
            print("...")
            return 0

get_audio(True)




