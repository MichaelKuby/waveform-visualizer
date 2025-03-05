from src.file_loader import load_wav_file


def main():
    """Test the core logic without a GUI."""
    file_path = "data/audio_test_case_2.wav"  # Change to an actual .wav file
    sample_rate, audio_data = load_wav_file(file_path)

    print(f"Loaded file: {file_path}")
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Number of Samples: {len(audio_data)}")


if __name__ == "__main__":
    main()
