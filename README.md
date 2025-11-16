🎧 Whisper Transcription Script

This is a simple Python script that uses OpenAI Whisper to transcribe audio files into text.

The script automatically:
	•	Detects the number in the filename (e.g., ders2.m4a)
	•	Saves the result as transcript2.txt
	•	Creates clean text output using the Whisper "medium" model


🚀 Usage
1.	Install Whisper:
  pip install openai-whisper
  pip install torch

2.	Put your audio file in the same folder.

3.	Run the script:
  python3 transcriber.py

5.	Your transcript will be saved automatically.


⚙️ Optional

Force a specific language:
  language="tr"  # or "en", "de", etc.


📄 License

Personal and educational use.
