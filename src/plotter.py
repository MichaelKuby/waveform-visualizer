import numpy as np


def draw_waveform(canvas, audio_data):
    """
    Manually draw the waveform on a Tkinter Canvas with adaptive scaling.
    Adapts scaling based on the file's amplitude.
    """
    canvas.update()
    width = canvas.winfo_width()  # right side of the canvas
    height = canvas.winfo_height()  # bottom of the canvas

    audio_scaled = adjust_audio_amplitude_to_fit_canvas(audio_data=audio_data)
    audio_scaled = map_audio_to_pixel_coordinates(audio_data=audio_scaled, canvas_height=height, compression_factor=1.0)
    downsampled_audio, time_scaled = downsample_to_match_canvas_width(audio_data=audio_scaled, canvas_width=width)
    draw_canvas_waveform(canvas, downsampled_audio, time_scaled)

    canvas.update_idletasks()


def draw_canvas_waveform(canvas, downsampled_audio, time_scaled):
    print(f"Drawing waveform with {len(downsampled_audio)} points (adaptive scaling)")
    # Draw the waveform
    for i in range(len(time_scaled) - 1):
        canvas.create_line(
            float(time_scaled[i]), float(downsampled_audio[i]),
            float(time_scaled[i + 1]), float(downsampled_audio[i + 1]),
            fill="blue"
        )


def downsample_to_match_canvas_width(audio_data, canvas_width):
    # Reduce the number of points to match canvas width
    num_samples = len(audio_data)
    step = max(1, num_samples // canvas_width)  # Only take one sample per pixel
    downsampled_audio = audio_data[::step]  # Downsample the waveform
    time_scaled = np.linspace(0, canvas_width, len(downsampled_audio))  # Scale to canvas width
    return downsampled_audio, time_scaled


def map_audio_to_pixel_coordinates(audio_data, canvas_height, compression_factor=1.0):
    # Map the audio values to the pixel coordinates of the canvas
    audio_data = ((audio_data * compression_factor) + 1) / 2 * canvas_height  # Map to [0, height]
    return audio_data


def adjust_audio_amplitude_to_fit_canvas(audio_data):
    # Normalize audio data to [-1, 1] range
    max_amplitude = np.max(np.abs(audio_data))  # Find the peak value
    if max_amplitude > 0:
        audio_scaled = audio_data / max_amplitude  # Normalize between -1 and 1
    else:
        audio_scaled = audio_data  # Avoid division by zero
    return audio_scaled
