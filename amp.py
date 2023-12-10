import json
import librosa

# load sound file function
def load_sound_file(file_path):
    # Load the audio file using librosa
    data, sr = librosa.load(str(file_path))

    with open('data.json', 'w') as file:
        json.dump(data, file)





