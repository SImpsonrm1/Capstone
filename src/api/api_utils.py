# src/api/api_utils.py

from fastapi import FastAPI, File, UploadFile
from src.audio_processing.audio_utils import load_audio, save_audio
from src.tempo_analysis.tempo_utils import get_tempo
from src.drum_generation.drum_utils import generate_drum_loop

app = FastAPI()

@app.post("/generate_drum_loop/")
async def create_drum_loop(file: UploadFile = File(...)):
    # Load and save the incoming audio file temporarily
    audio = load_audio(file.file)
    save_audio(audio, "temp_audio.wav")
    
    # Get the tempo of the audio
    tempo = get_tempo("temp_audio.wav")
    
    # Generate drum loop
    drum_loop_path = generate_drum_loop(tempo)
    
    # Return the generated drum loop
    return {"drum_loop_path": drum_loop_path}
