import os
import pathlib

from unittest import TestCase

from pydub import AudioSegment

from pjg_sound.low_pass_filter import LowPassFilter


class TestLowPassFilter(TestCase):

    def setUp(self) -> None:
        self.original_audio_segment = AudioSegment.from_mp3(os.path.join(pathlib.Path(__file__).parent.resolve(), '..',
                                                                         'freedom_sample.mp3'))
        self.low_pass_filter = LowPassFilter(self.original_audio_segment)
        self.frequency = 5_00

    def test_filter(self):
        self.low_pass_filter.filter(self.frequency)
        self.assertNotEqual(self.low_pass_filter.filtered_audio_segment, self.original_audio_segment)
