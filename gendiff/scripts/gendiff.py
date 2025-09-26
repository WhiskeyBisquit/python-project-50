#!/usr/bin/env python3
import argparse

from gendiff.formatters.stylish import get_stylish
from gendiff.generate_diff import generate_diff
from gendiff.modules.parse import parse


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

    dict1 = parse(vars(args)['first_file'])
    dict2 = parse(vars(args)['second_file'])

    diff = generate_diff(dict1, dict2)

    print(get_stylish(diff))


if __name__ == '__main__':
    main()
