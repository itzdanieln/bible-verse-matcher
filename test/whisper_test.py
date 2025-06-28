import whisper
import os

# Load model
model = whisper.load_model("base")  # You can use "small", "medium", or "large" for better accuracy

# Path to your test audio file (must be WAV, MP3, or M4A etc.)
audio_path = "output.wav"

assert os.path.exists(audio_path), f"File not found: {audio_path}"

# Transcribe
result = model.transcribe(audio_path)

# Output
print("Transcription:")
print(result["text"])
