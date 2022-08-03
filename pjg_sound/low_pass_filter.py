from pydub import AudioSegment

from pjg_sound.base_processor import BaseSoundProcessor


class LowPassFilter(BaseSoundProcessor):

    def __init__(self, audio_segment: AudioSegment):
        self.filtered_audio_segment = None
        super().__init__(audio_segment)

    def filter(self, frequency):
        self.filtered_audio_segment = self.audio_segment.low_pass_filter(frequency)
        return self.filtered_audio_segment
