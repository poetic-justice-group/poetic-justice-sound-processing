from pydub import AudioSegment


class LowPassFilter(object):

    def __init__(self, audio_segment: AudioSegment):
        self.audio_segment = audio_segment
        self.filtered_audio_segment = None

    def filter(self, frequency):
        self.filtered_audio_segment = self.audio_segment.low_pass_filter(frequency)
        return self.filtered_audio_segment
