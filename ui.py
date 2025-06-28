import streamlit as st
import requests
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile

st.set_page_config(page_title="AI Bible Verse Finder", layout="centered")
st.title("📖 AI-Powered Bible Verse Finder")
st.markdown("Enter text, record, or upload audio to find matching Bible passages (KJV).")

# === Input method ===
option = st.radio("Choose input method:", ("Text", "Voice (Upload)", "Voice (Mic Recording)"))

# === Text input ===
if option == "Text":
    user_text = st.text_input("🔤 Type something:")
    if st.button("🔍 Find Verse"):
        if user_text.strip():
            with st.spinner("Matching verse..."):
                res = requests.post("http://localhost:5000/text", json={"text": user_text})
                result = res.json()
                st.success("📖 Matched Verse:")
                st.write(result.get("verse", "No verse found."))
        else:
            st.warning("Please enter some text.")

# === Audio upload ===
elif option == "Voice (Upload)":
    uploaded_file = st.file_uploader("🎤 Upload audio file (WAV/MP3)", type=["wav", "mp3"])
    if st.button("🔍 Transcribe and Match") and uploaded_file:
        with st.spinner("Processing audio..."):
            res = requests.post(
                "http://localhost:5000/voice",
                files={"audio": (uploaded_file.name, uploaded_file, "multipart/form-data")}
            )
            result = res.json()
            st.success("📝 Transcribed Text:")
            st.write(result.get("text", "No transcription"))
            st.success("📖 Matched Verse:")
            st.write(result.get("verse", "No verse found."))

# === Mic recording ===
elif option == "Voice (Mic Recording)":
    duration = st.slider("🎙️ Recording duration (seconds):", 2, 10, 5)
    if st.button("🔴 Record from Mic"):
        st.info("Recording... Speak now.")
        try:
            fs = 16000  # Sample rate
            audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
            sd.wait()
            st.success("Recording complete!")

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
                wav.write(f.name, fs, audio)
                f.seek(0)
                with st.spinner("Transcribing..."):
                    res = requests.post(
                        "http://localhost:5000/voice",
                        files={"audio": ("mic_recording.wav", f, "multipart/form-data")}
                    )
                    result = res.json()
                    st.success("📝 Transcribed Text:")
                    st.write(result.get("text", "No transcription"))
                    st.success("📖 Matched Verse:")
                    st.write(result.get("verse", "No verse found."))

        except Exception as e:
            st.error(f"Recording failed: {e}")
