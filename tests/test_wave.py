import numpy as np
import scipy.io.wavfile as wav


def create_test_wav(filename="test_wave.wav", duration=2.0, sample_rate=44100, freq=440):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * freq * t)  # Pure sine wave [-1,1]
    waveform_int16 = (waveform * np.iinfo(np.int16).max).astype(np.int16)
    wav.write(filename, sample_rate, waveform_int16)


# Generate the modified test file
create_test_wav("../data/test_wave.wav")
