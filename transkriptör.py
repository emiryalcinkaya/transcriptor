import whisper
import re

# Load the Whisper model
model = whisper.load_model("medium")

# Input file
audio_path = "ders2.m4a"

# Find the number in the file name
match = re.search(r'\d+', audio_path)
number = match.group() if match else "1"

# Create output file name automatically
output_file = f"transcript{number}.txt"

print("🎧 Transkript başlıyor.")

# Transcribe the audio
# If you want select to specific language you need to write (language="tr or en etc.")
result = model.transcribe(
    audio_path, 
    task="transcribe",
)

# Get the text result 
text = result["text"]

# Save the text to a file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Transkript tamamlandı!")
print(f"Metin '{output_file}' dosyası olarak kaydedildi.")