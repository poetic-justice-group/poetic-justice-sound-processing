from pydub import effects

from pjg_sound.base_processor import BaseSoundProcessor


class Normalizer(BaseSoundProcessor):

    def __init__(self, audio_segment):
        self.normalized_filtered_audio_segment = None
        super().__init__(audio_segment)

    def normalize(self):
        self.normalized_filtered_audio_segment = effects.normalize(self.audio_segment)
        return self.normalized_filtered_audio_segment
