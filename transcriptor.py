import whisper
import re
import os

# Select and load the Whisper model
model_name = input("Select model (tiny/base/small/medium/large): ")
print("Loading model...")

model = whisper.load_model(model_name)

# Get audio file name
audio_path = input("Enter audio file name: ")

# Check if the file exists
if not os.path.exists(audio_path):
    print("❌ File not found.")
    exit()

# Select transcription language
language = input("Select language (en/tr/de/fr): ")

# Extract number from file name
match = re.search(r'\d+', audio_path)
number = match.group() if match else "1"

# Create transcript file name
output_file = f"transcript{number}.txt"

print("🎧 Transcription started.")

# Transcribe the audio
result = model.transcribe(
    audio_path, 
    task="transcribe",
    language=language
)

# Extract transcribed text
text = result["text"]

# Save the text to a file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Transcription completed!")
print(f"📄 Transcript saved as '{output_file}'.")