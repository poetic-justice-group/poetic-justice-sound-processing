import argparse

from sound.audio_io import AudioWriter, AudioReader
from sound.low_pass_filter import LowPassFilter


def low_pass_filter(audio_file_path, frequency):
    audio_reader = AudioReader(audio_file_path)
    audio_segment = audio_reader.read()
    low_pass_filter = LowPassFilter(audio_segment)
    filtered_audio_segment = low_pass_filter.filter(frequency)
    audio_writer = AudioWriter(filtered_audio_segment)
    audio_writer.write(f"{audio_file_path.split('.')[0]}_{frequency}.mp3")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str)
    parser.add_argument('-f', '--frequency', type=float)
    args = parser.parse_args()
    low_pass_filter(args.input_file, args.frequency)