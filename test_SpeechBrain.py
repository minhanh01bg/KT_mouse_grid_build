from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import librosa
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = Wav2Vec2Processor.from_pretrained("khanhld/wav2vec2-base-vietnamese-160h")
model = Wav2Vec2ForCTC.from_pretrained("khanhld/wav2vec2-base-vietnamese-160h")
model.to(device)

def transcribe(wav):
    input_values = processor(wav, sampling_rate=16000, return_tensors="pt").input_values
    logits = model(input_values.to(device)).logits
    pred_ids = torch.argmax(logits, dim=-1)
    pred_transcript = processor.batch_decode(pred_ids)[0]
    return pred_transcript


wav, _ = librosa.load('./data/audio.mp3', sr = 16000)
print(f"transcript: {transcribe(wav)}")

