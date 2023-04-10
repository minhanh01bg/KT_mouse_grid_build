# Import các thư viện
import pygame
# from pydub import AudioSegment
# from pydub.playback import play as pydub_play
import sounddevice as sd
from gtts import gTTS
import os
# import simpleaudio as sa
language = 'vi'
def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text,lang = language,slow=False)
    tts.save("sound.mp3")
    import pygame

    pygame.init()

    sound_file = "sound.mp3"
    sound = pygame.mixer.Sound(sound_file)

    sound.play()

    while pygame.mixer.get_busy():
        pygame.time.wait(100)
    os.remove("sound.mp3")
    pygame.quit()
speak("Xin chào! Tôi là bot")
# Phát âm thanh bằng pydub
# sound = AudioSegment.from_file("sound.mp3", format="mp3")
# pydub_play(sound)

# # Phát âm thanh bằng sounddevice
# data, fs = sd.read("path/to/file.wav", dtype='float32')
# sd.play(data, fs)
# sd.wait()

# # Phát âm thanh bằng simpleaudio
# wave_obj = sa.WaveObject.from_wave_file("path/to/file.wav")
# play_obj = wave_obj.play()
# play_obj.wait_done()
