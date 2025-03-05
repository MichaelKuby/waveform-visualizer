import numpy as np


def extract_segment(audio_data, sample_rate, start_time, end_time):
    """
    Extract a time segment from the waveform.

    Args:
        audio_data (numpy array): Audio samples (mono).
        sample_rate (int): Sample rate of the audio.
        start_time (float): Start time in seconds.
        end_time (float): End time in seconds.

    Returns:
        numpy array: Extracted segment.
    """
    start_sample = int(start_time * sample_rate)
    end_sample = int(end_time * sample_rate)
    return audio_data[start_sample:end_sample]


def get_time_axis(audio_data, sample_rate):
    """
    Generate a time axis for the waveform to ensure time-based visualization.

    Args:
        audio_data (numpy array): Audio samples.
        sample_rate (int): Sample rate of the audio.

    Returns:
        numpy array: Time values corresponding to each sample.
    """
    return np.linspace(0, len(audio_data) / sample_rate, len(audio_data))
