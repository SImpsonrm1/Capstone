# src/audio_processing/audio_utils.py

from pydub import AudioSegment

def load_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    return audio

def save_audio(audio, output_path):
    audio.export(output_path, format="wav")
