import whisper

# Load model once (you can put this outside the function so it doesn't reload every time)
model = whisper.load_model("base")  # or "tiny" if you're on a low-end PC

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]
