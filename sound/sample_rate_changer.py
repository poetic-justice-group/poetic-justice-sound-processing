class SampleRateChanger(object):

    def __init__(self, audio_segment):
        self.audio_segment = audio_segment

    def resample(self, sample_rate):
        return self.audio_segment.set_frame_rate(sample_rate)