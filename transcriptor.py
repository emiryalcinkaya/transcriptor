import whisper
import re

# Load the Whisper model
model = whisper.load_model("medium")

# Input file
audio_path = "audio file name"

# Find the number in the file name
match = re.search(r'\d+', audio_path)
number = match.group() if match else "1"

# Create output file name automatically
output_file = f"transcript{number}.txt"

print("🎧 Transcription started.")

# Transcribe the audio
result = model.transcribe(
    audio_path, 
    task="transcribe",
    language="en" # If you want select to specific language you need to change (language="en or en etc.")
)

# Get the text result 
text = result["text"]

# Save the text to a file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Transcription completed!")
print(f"📄 Transcript saved as '{output_file}'.")