import argparse
import os

from pjg_sound.audio_io import AudioWriter, AudioReader


def convert_format(audio_file_path, new_file_format):
    audio_reader = AudioReader(audio_file_path)
    audio_segment = audio_reader.read()
    audio_writer = AudioWriter(audio_segment)
    output_file_path = f'{os.path.splitext(audio_file_path)[0]}.{new_file_format}'
    audio_writer.write(output_file_path, file_format=new_file_format)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str)
    parser.add_argument('-n', '--new-file-format', type=str)
    args = parser.parse_args()
    convert_format(args.input_file, args.new_file_format)