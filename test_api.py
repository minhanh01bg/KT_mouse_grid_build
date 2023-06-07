# import requests

# url = 'https://api.fpt.ai/hmi/asr/general'
# payload = open('./data/audio.mp3', 'rb').read()
# headers = {
#     'api-key': 'rRUo4GpJrYNT745uHSMg8KSmLgmBhuQI'
# }

# response = requests.post(url=url, data=payload, headers=headers)

# # print(response.json())

# # import json
# # json.dump(response.json(), open('./data/c73aa685630987783156779fc73d1221.json', 'w', encoding='utf-8'), ensure_ascii=False)

# # print(json.loads(open('./data/c73aa685630987783156779fc73d1221.json', 'r', encoding='utf-8').read())['hypotheses'][0]['utterance'])

# print(response.json()['hypotheses'][0]['utterance'])

# Import the json library

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