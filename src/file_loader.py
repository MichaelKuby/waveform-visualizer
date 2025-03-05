import scipy.io.wavfile as wav
import numpy as np


def load_wav_file(file_path):
    """
    Load a .wav file and return the sample rate and audio data.

    Args:
        file_path (str): Path to the .wav file.

    Returns:
        tuple: (sample_rate, audio_data)
    """
    try:
        sample_rate, audio_data = wav.read(file_path)

        # Normalize audio data if it's in an integer format. Otherwise, we assume  it's already normalized.
        if audio_data.dtype == np.int16:
            audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max
        elif audio_data.dtype == np.int32:
            audio_data = audio_data.astype(np.float32) / np.iinfo(np.int32).max

        return sample_rate, audio_data
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None, None
