# 📖 BibleVerse Matcher

An AI-powered web app that listens to live or uploaded audio and displays matching Bible verses in real time using speech recognition and GPT-4.

## ✨ Features

- 🔤 Input text or 🎤 upload audio
- 🧠 Matches input to Bible verses (KJV)
- 🎙️ Optional microphone support for live audio
- 📡 Real-time verse suggestions during speech

## 🚀 How to Run

1. **Clone the repository**  
```bash
git clone https://github.com/itzdanieln/bible-verse-matcher.git
cd bible-verse-matcher

**Install dependencies**
pip install -r requirements.txt

Set your OpenAI API key
Create a .env file and add:
OPENAI_API_KEY=your-key-here

Run the app
python backend/app.py   # Start Flask backend
python -m streamlit run ui.py  # Start UI

📁 Project Structure
bash
Copy
Edit
bible-app/
├── backend/
│   ├── app.py          # Flask server
│   ├── ai_engine.py    # GPT-4 Bible matcher
│   ├── stt.py          # Speech-to-text
├── test/               # Tests
├── ui.py               # Streamlit UI
├── .env                # API key (not pushed)
├── .gitignore
├── requirements.txt

🙏 Acknowledgements
OpenAI GPT-4
Whisper (speech recognition)
Streamlit

Built by @itzdanieln
