import os

from pydub import AudioSegment
from scipy.io import wavfile


class AudioReader(object):

    WAV = '.wav'
    MP3 = '.mp3'

    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        _, self.file_extension = os.path.splitext(audio_file_path)
        self.wav_file_path = self.audio_file_path if self.file_extension == self.WAV else None
        self.audio_segment = None
        self.sample_rate = None
        self.data = None

    def _convert_to_wav(self):
        audio_writer = AudioWriter(self.audio_segment)
        self.wav_file_path = f'{os.path.splitext(self.audio_file_path)[0]}.wav'
        audio_writer.write(self.wav_file_path, file_format='wav')

    def read(self):
        if self.file_extension == self.WAV:
            self.audio_segment = AudioSegment.from_wav(self.audio_file_path)
        elif self.file_extension == self.MP3:
            self.audio_segment = AudioSegment.from_mp3(self.audio_file_path)
            self._convert_to_wav()
        self.sample_rate, self.data = wavfile.read(self.wav_file_path)

        return self.audio_segment


class AudioWriter(object):

    def __init__(self, audio_segment):
        self.audio_segment = audio_segment

    def write(self, audio_file_path, file_format=None):
        _, file_extension = os.path.splitext(audio_file_path)
        file_format = file_format if file_format else file_extension.replace('.', '')
        return self.audio_segment.export(audio_file_path, format=file_format)
