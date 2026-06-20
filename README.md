<div align="center">

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="120">

# 🎧 Whisper Audio Transcriptor

<img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
<img src="https://img.shields.io/badge/OpenAI-Whisper-412991">
<img src="https://img.shields.io/badge/Status-Active-success">

A lightweight Python application that automatically converts audio files into text using OpenAI Whisper.

</div>

---

## About

This project uses OpenAI Whisper to transcribe audio files into text.

The application automatically detects numbers in audio file names and generates matching transcript files. Users can select different Whisper models and transcription languages directly from the terminal.

---

## Features

- Audio-to-text transcription
- OpenAI Whisper integration
- Multiple Whisper model support
- Multiple language support
- Automatic transcript file naming
- File existence validation
- Simple terminal interface

---

## Requirements

Install the required dependencies:

```bash
pip install openai-whisper
```

Install FFmpeg:

### macOS

```bash
brew install ffmpeg
```

### Windows

Download and install FFmpeg from:

https://ffmpeg.org/download.html

---

## Usage

Run the application:

```bash
python transcriptor.py
```

Example:

```text
Select model (tiny/base/small/medium/large): medium
Enter audio file name: lecture2.m4a
Select language (en/tr/de/fr): en
```

Generated output:

```text
transcript2.txt
```

---

## Supported Models

```text
tiny
base
small
medium
large
```

---

## Technologies Used

- Python
- OpenAI Whisper
- FFmpeg
- Regular Expressions (re)

---

## Author

**Emir Yalçınkaya**

Software Engineering Student

GitHub: https://github.com/emiryalcinkaya