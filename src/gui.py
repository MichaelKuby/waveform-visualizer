import tkinter as tk
from tkinter import filedialog, messagebox
from src.file_loader import load_wav_file
from src.plotter import draw_waveform


class WaveformGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Waveform Viewer")

        # Frame to hold buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Load file button
        self.load_button = tk.Button(button_frame, text="Load WAV File", command=self.load_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_canvas)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Metadata display
        self.info_label = tk.Label(root, text="No file loaded.", wraplength=400)
        self.info_label.pack()

        # Canvas for waveform drawing
        self.canvas_width = 1200
        self.canvas_height = 450
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(pady=10)

    def load_file(self):
        """Open file dialog to load a .wav file, process it, and display the waveform."""
        file_path = filedialog.askopenfilename(filetypes=[("WAV Files", "*.wav")])
        if not file_path:
            return  # User canceled

        try:
            sample_rate, audio_data = load_wav_file(file_path)
            if audio_data is None:
                messagebox.showerror(title="Error", message="Failed to load the WAV file.")
                return

            self.info_label.config(
                text=f"Loaded: {file_path.split("/")[-1]}\nSample Rate: {sample_rate} Hz\nSamples: {len(audio_data)}"
            )

            self.draw_waveform(audio_data)

        except Exception as e:
            messagebox.showerror(title="Error", message=f"Failed to load file: {e}")

    def draw_waveform(self, audio_data):
        """Passes the loaded waveform data to the plotter module for drawing."""
        self.canvas.delete("all")
        draw_waveform(self.canvas, audio_data)

    def reset_canvas(self):
        """Clears the canvas and resets the label to 'No file loaded'."""
        self.canvas.delete("all")  # Clear waveform drawing
        self.info_label.config(text="No file loaded.")  # Reset label
