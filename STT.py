import whisper
model = whisper.load_model("base")
result = model.transcribe("/Users/lizhuoran/Desktop/PY/4.mp3")
print(result["text"])

