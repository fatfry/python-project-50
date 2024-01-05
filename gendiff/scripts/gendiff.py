#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff.gendiff_build import gendiff_diff


def main():
    args = parse_args()
    print(gendiff_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
