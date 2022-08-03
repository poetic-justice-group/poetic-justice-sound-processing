import logging

import noisereduce as nr
import os

from scipy.io import wavfile
from pydub import AudioSegment

from pjg_sound.base_processor import BaseSoundProcessor

logger = logging.getLogger(__file__)


class NoiseReducer(BaseSoundProcessor):

    def __init__(self, audio_segment, sample_rate=None):
        # self.data = data
        self.sample_rate = sample_rate if sample_rate else audio_segment.frame_rate
        self.data_with_reduced_noise = None
        super().__init__(audio_segment)

    def reduce_noise(self):
        self.data_with_reduced_noise = nr.reduce_noise(y=self.audio_segment.get_array_of_samples(),
                                                       sr=self.sample_rate,
                                                       stationary=True,
                                                       prop_decrease=0.75,
                                                       # freq_mask_smooth_hz=500.,
                                                       # n_std_thresh_stationary=3.5,
                                                       # time_constant_s=5.,
                                                       # n_fft=512
                                                       )
        wavfile.write('temp.wav', self.sample_rate, self.data_with_reduced_noise)
        audio_segment = AudioSegment.from_wav('temp.wav')
        os.remove('temp.wav')
        return audio_segment
