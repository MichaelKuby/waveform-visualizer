import numpy as np
import scipy.io.wavfile as wav


def load_wav_file(file_path):
    """
    Load a .wav file and return the sample rate and normalized audio data.

    Args:
        file_path (str): Path to the .wav file.

    Returns:
        tuple: (sample_rate, audio_data) where audio_data is normalized between -1 and 1.
    """
    try:
        sample_rate, audio_data = wav.read(file_path)

        # Normalize based on data type to range [-1, 1]
        if audio_data.dtype == np.int16:
            audio_data = audio_data.astype(np.float32) / np.iinfo(np.int16).max
        elif audio_data.dtype == np.int32:
            audio_data = audio_data.astype(np.float32) / np.iinfo(np.int32).max
        elif audio_data.dtype == np.uint8:  # Unsigned 8-bit PCM
            audio_data = (audio_data.astype(np.float32) - 128) / 128  # Convert to range [-1, 1]
        elif np.issubdtype(audio_data.dtype, np.floating):  # Floating-point PCM
            pass  # Should be in [-1, 1] already
        else:
            raise ValueError(f"Unsupported audio format: {audio_data.dtype}")

        return sample_rate, audio_data

    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None, None
