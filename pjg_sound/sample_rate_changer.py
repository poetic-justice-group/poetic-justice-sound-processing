from pjg_sound.base_processor import BaseSoundProcessor


class SampleRateChanger(BaseSoundProcessor):

    def resample(self, sample_rate):
        return self.audio_segment.set_frame_rate(sample_rate)