import wave
def get_audio(audio):
    # Lấy dữ liệu sóng dạng byte từ đối tượng audio
    wave_data = audio.get_wav_data()

    # Ghi dữ liệu sóng vào file
    with wave.open("myrecording.wav", "wb") as wav_file:
        wav_file.setnchannels(audio._input_stream._audio_channels)
        wav_file.setsampwidth(audio._input_sample_width)
        wav_file.setframerate(audio._input_rate)
        wav_file.writeframes(wave_data)
