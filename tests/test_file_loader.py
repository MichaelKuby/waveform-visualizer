import unittest
import numpy as np
import os
from src.file_loader import load_wav_file
import scipy.io.wavfile as wav


class TestFileLoader(unittest.TestCase):
    """Unit tests for the load_wav_file function."""

    @classmethod
    def setUpClass(cls):
        """Set up temporary WAV files for testing."""
        cls.test_int16_file = "tests/test_audio_int16.wav"
        cls.test_int32_file = "tests/test_audio_int32.wav"
        cls.test_float32_file = "tests/test_audio_float32.wav"
        sample_rate = 44100
        duration = 1  # 1 second
        num_samples = sample_rate * duration

        # Generate test signals
        sine_wave_int16 = (np.sin(2 * np.pi * 440 * np.arange(num_samples) / sample_rate) * 32767).astype(np.int16)
        sine_wave_int32 = (np.sin(2 * np.pi * 440 * np.arange(num_samples) / sample_rate) * 2147483647).astype(np.int32)
        sine_wave_float32 = np.sin(2 * np.pi * 440 * np.arange(num_samples) / sample_rate).astype(np.float32)

        # Save test files
        wav.write(cls.test_int16_file, sample_rate, sine_wave_int16)
        wav.write(cls.test_int32_file, sample_rate, sine_wave_int32)
        wav.write(cls.test_float32_file, sample_rate, sine_wave_float32)

    @classmethod
    def tearDownClass(cls):
        """Clean up the test WAV files after tests."""
        for file in [cls.test_int16_file, cls.test_int32_file, cls.test_float32_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_load_int16_wav_file(self):
        """Test that int16 WAV files are normalized to [-1, 1]."""
        sample_rate, audio_data = load_wav_file(self.test_int16_file)
        self.assertEqual(sample_rate, 44100)
        self.assertTrue(np.all((audio_data >= -1.0) & (audio_data <= 1.0)))  # Normalization check

    def test_load_int32_wav_file(self):
        """Test that int32 WAV files are normalized to [-1, 1]."""
        sample_rate, audio_data = load_wav_file(self.test_int32_file)
        self.assertEqual(sample_rate, 44100)
        self.assertTrue(np.all((audio_data >= -1.0) & (audio_data <= 1.0)))  # Normalization check

    def test_load_float32_wav_file(self):
        """Test that float32 WAV files remain unchanged."""
        sample_rate, audio_data = load_wav_file(self.test_float32_file)
        self.assertEqual(sample_rate, 44100)
        self.assertTrue(np.all((audio_data >= -1.0) & (audio_data <= 1.0)))  # Should already be normalized
        self.assertEqual(audio_data.dtype, np.float32)  # Ensure dtype is unchanged

    def test_load_nonexistent_file(self):
        """Test handling of a nonexistent file."""
        sample_rate, audio_data = load_wav_file("nonexistent.wav")
        self.assertIsNone(sample_rate)
        self.assertIsNone(audio_data)

    def test_load_invalid_format(self):
        """Test handling of an invalid file format."""
        with open("tests/invalid_file.txt", "w") as f:
            f.write("This is not a WAV file.")

        sample_rate, audio_data = load_wav_file("tests/invalid_file.txt")
        self.assertIsNone(sample_rate)
        self.assertIsNone(audio_data)

        os.remove("tests/invalid_file.txt")  # Clean up


if __name__ == "__main__":
    unittest.main()
