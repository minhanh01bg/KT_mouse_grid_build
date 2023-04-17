# Import các thư viện
# import pygame
# # from pydub import AudioSegment
# # from pydub.playback import play as pydub_play
# import sounddevice as sd
# from gtts import gTTS
# import os
# # import simpleaudio as sa
# language = 'vi'
# def speak(text):
#     print("Bot: {}".format(text))
#     tts = gTTS(text=text,lang = language,slow=False)
#     tts.save("sound.mp3")
#     import pygame

#     pygame.init()

#     sound_file = "sound.mp3"
#     sound = pygame.mixer.Sound(sound_file)

#     sound.play()

#     while pygame.mixer.get_busy():
#         pygame.time.wait(100)
#     os.remove("sound.mp3")
#     pygame.quit()
# speak("Xin chào! Tôi là bot")


# Import necessary libraries
from pyvi import ViTokenizer
import gensim
import numpy as np
# from euclidean_norm import dot, euclidean_norm
# Load pre-trained Word2Vec model
model_path = './word2vec/model/wiki.vi.model.bin'
w2v_model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)


# Define function to preprocess text
def preprocess_text(text):
    text = ViTokenizer.tokenize(text)
    text = text.lower()
    return text

def balance_vector(vec):
    vec = np.array(vec)
    vec = vec/np.mean(vec)
    vec = np.reshape(vec, (-1,))
    return vec
def cosine_similarity(u, v):
    u_ext = np.expand_dims(u, axis=1)
    # print(u_ext)
    dot_product = np.dot(v, u_ext)
    norm_u_ext = np.linalg.norm(u_ext)
    norm_v = np.linalg.norm(v, axis=1)
    return dot_product / (norm_u_ext * norm_v)
def pad_vec(a,b):
    if a.shape[0] < b.shape[0]:
        a = np.pad(a, ((0, b.shape[0]-a.shape[0]), (0, 0)), 'constant')
    else:
        b = np.pad(b, ((0, a.shape[0]-b.shape[0]), (0, 0)), 'constant')

# Define function to calculate sentence similarity
def sentence_similarity(s1, s2):
    s1 = preprocess_text(s1).split()
    s2 = preprocess_text(s2).split()
    
    s1_vectors = []
    for word in s1:
        try:
            s1_vectors.append(w2v_model[word])
        except:
            pass
    
    s2_vectors = []
    for word in s2:
        try:
            s2_vectors.append(w2v_model[word])
        except:
            pass
    
    if len(s1_vectors) == 0 or len(s2_vectors) == 0:
        print(len(s1_vectors))
        print(len(s2_vectors))
        return 0
    
    if len(s1_vectors) == len(s2_vectors):
        print("equal:",end=" ")
        s1_vector = balance_vector(s1_vectors)
        s2_vector = balance_vector(s2_vectors)
    else:
        print("not equal:",end=" ")
        s1_vectors = np.array(s1_vectors)
        s2_vectors = np.array(s2_vectors)
        if s1_vectors.shape[0] < s2_vectors.shape[0]:
            s1_vectors = np.pad(s1_vectors, ((0, s2_vectors.shape[0]-s1_vectors.shape[0]), (0, 0)), 'constant')
        else:
            s2_vectors = np.pad(s2_vectors, ((0, s1_vectors.shape[0]-s2_vectors.shape[0]), (0, 0)), 'constant')
        # print(len(s1_vectors))
        # print(len(s1_vectors[0]))
        # print(len(s2_vectors))
        # print(len(s2_vectors[0]))
        s1_vector = s1_vectors
        s2_vector = s2_vectors
        s1_vector = np.mean(s1_vectors, axis=0)
        s2_vector = np.mean(s2_vectors, axis=0)
        # s1_vector = balance_vector(s1_vector)
        # s2_vector = balance_vector(s2_vector)
        
    cosine_similarity1 = np.dot(s1_vector, s2_vector) / (np.linalg.norm(s1_vector) * np.linalg.norm(s2_vector))
    # similarity = dot(s1_vector, s2_vector) / (euclidean_norm(s1_vector) * euclidean_norm(s2_vector))
    
    return cosine_similarity1


# Example sentences
s1 = 'Hôm nay trời nắng.'
s2 = 'Thời tiết hôm nay rất đẹp.'
s11 = 'Hôm nay trời nắng đẹp.'
s3 = 'Sân khấu rực rỡ ánh đèn.'
s4 = 'Sân khấu sáng loáng ánh đèn.'
s5 = 'Công ty ABC đang tuyển dụng nhân viên mới.'
s6 = 'Công ty XYZ đang tuyển dụng nhân viên.'
s7 = 'Thời tiết hôm nay rất xấu.'
s8 = 'Hôm nay trời mưa.'



s9="mưa"
s10="nắng"
# Calculate sentence similarity
# print(f"{s1} & {s2}:",sentence_similarity(s1, s2)) # 0.8084618
# print(f"{s1} & {s11} :",sentence_similarity(s1, s11)) # 1.0 (same sentence
# print(f"{s1} & {s3}:",sentence_similarity(s1, s3)) # 0.34951764
# print(f"{s1} & {s4}:",sentence_similarity(s1, s4)) # 0.756798
# print(f"{s1} & {s5}:",sentence_similarity(s1, s5)) # 0.019295293
# print(f"{s5} & {s6}:",sentence_similarity(s5, s6)) # 0.7776596
# print(f"{s1} & {s7}:",sentence_similarity(s1, s7)) # 0.03189189
# print(f"{s1} & {s8}:",sentence_similarity(s1, s8)) # 0.27018103

# print(f"{s9} & {s10} :",sentence_similarity(s9, s10)) # 0.27018103

str1 = "chọn ô 1"
str2 = "chọn o1"

str3 = "di chuyển đến ô"
str4 = "di chuyển đến o"
str44= "đi đến ô"
str5 = "chuyển đến o"
str6 = "đọc tin tức"
str7 = "đọc báo"

str8 = "chọn chuột trái"
str9 = "chọn chuột phải"
print(f"{str1} & {str2}: ",sentence_similarity(str1, str2)) 
print(f"{str3} & {str4}: ",sentence_similarity(str3, str4)) 
print(f"{str3} & {str44}: ",sentence_similarity(str3, str44))
print(f"{str4} & {str5}: ",sentence_similarity(str4, str5))
print(f"{str5} & {str6}: ",sentence_similarity(str5, str6))
print(f"{str6} & {str7}: ",sentence_similarity(str6, str7))
print(f"{str8} & {str9}: ",sentence_similarity(str8, str9))




# u = np.array([1, 2])
# v = np.array([[3, 4], [5, 6]])
# similarity = cosine_similarity(u, v)
# print(similarity)
# # print(np.mean(similarity))
