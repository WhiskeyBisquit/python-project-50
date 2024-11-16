#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', dest='FORMAT', type=str, help="set format of output"
    )

    args = parser.parse_args()
    file_path1 = vars(args)['first_file']
    file_path2 = vars(args)['second_file']
    diff = generate_diff(file_path1, file_path2)
    print(diff)


if __name__ == '__main__':
    main()
