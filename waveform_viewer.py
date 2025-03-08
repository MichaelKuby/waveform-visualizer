from src.gui import WaveformGUI
import tkinter as tk


def main():
    """Launch the waveform viewer GUI."""
    root = tk.Tk()
    app = WaveformGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
