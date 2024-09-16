#!/usr/bin/env python3
import argparse
from hexlet_code.gendiff import generate_diff
from hexlet_code.gendiff_yml import generate_diff_yml
from hexlet_code.read_file import load_file
from hexlet_code.read_file import load_file_yml


def parser_diff():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def main():
    args = parser_diff()
    if args.first_file.endswith('.yml') or args.first_file.endswith('.yaml'):
        dict1 = load_file_yml(args.first_file)
        dict2 = load_file_yml(args.second_file)
        diff = generate_diff_yml(dict1, dict2)

    elif args.first_file.endswith('.json'):
        dict1 = load_file(args.first_file)
        dict2 = load_file(args.second_file)
        diff = generate_diff(dict1, dict2)
    print(diff)
    

if __name__ == '__main__':
    main()
