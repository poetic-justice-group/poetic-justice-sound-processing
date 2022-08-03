import argparse
import os

from pjg_sound.audio_io import AudioWriter, AudioReader
from pjg_sound.sample_rate_changer import SampleRateChanger


def change_sample_rate(audio_file_path, sample_rate):
    audio_reader = AudioReader(audio_file_path)
    audio_segment = audio_reader.read()
    sample_rate_changer = SampleRateChanger(audio_segment)
    new_audio_segment = sample_rate_changer.resample(sample_rate)
    audio_writer = AudioWriter(new_audio_segment)
    basename, extension = os.path.splitext(audio_file_path)
    output_file_path = f'{basename}_sr={sample_rate}{extension}'
    audio_writer.write(output_file_path)


def change_sample_rate_2(audio_file_path, sample_rate):
    audio_reader = AudioReader(audio_file_path)
    audio_segment = audio_reader.read()
    audio_segment = audio_segment.set_frame_rate(sample_rate)
    basename, extension = os.path.splitext(audio_file_path)
    output_file_path = f'{basename}_sr={sample_rate}{extension}'
    audio_segment.export(output_file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str)
    parser.add_argument('-s', '--sample-rate', type=int)
    args = parser.parse_args()
    change_sample_rate_2(args.input_file, args.sample_rate)