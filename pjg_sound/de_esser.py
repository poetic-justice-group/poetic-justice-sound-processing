import pydub

from pjg_sound.base_processor import BaseSoundProcessor


class DeEsser(BaseSoundProcessor):
    """
    Remove "sibilant" consonants like S
    (https://en.wikipedia.org/wiki/De-essing)
    """

    def process(self):
        return self.bandstop(self.audio_segment, 8000, 9000, order=4)

    def bandstop(self, seg, low, high, order=2):
        filter_fn = pydub.scipy_effects._mk_butter_filter([low, high], 'bandstop', order=order)
        return seg.apply_mono_filter_to_each_channel(filter_fn)
