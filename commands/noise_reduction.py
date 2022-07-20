import argparse

from sound.audio_io import AudioWriter, AudioReader
from sound.noise_reduction import NoiseReducer


def noise_reduction(audio_file_path):
    audio_reader = AudioReader(audio_file_path)
    audio_segment = audio_reader.read()
    noise_reducer = NoiseReducer(audio_segment)
    filtered_audio_segment = noise_reducer.reduce_noise()
    audio_writer = AudioWriter(filtered_audio_segment)
    audio_writer.write(f"{audio_file_path.split('.')[0]}_noise_reduced.mp3")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str)
    args = parser.parse_args()
    noise_reduction(args.input_file)