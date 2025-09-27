#!/usr/bin/env python3
import argparse

from gendiff.generate_diff import generate_diff


def main(arg_list=None):
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--fomat", dest='FORMAT', type=str, help='set format of output'
        )

    args = parser.parse_args(arg_list)

    file_path1 = vars(args)['first_file']
    file_path2 = vars(args)['second_file']
    formatter = vars(args)['FORMAT'] or 'stylish'

    diff = generate_diff(file_path1, file_path2, formatter)

    print(diff)


if __name__ == '__main__':
    main()
