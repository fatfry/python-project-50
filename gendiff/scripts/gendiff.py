#!/usr/bin/env python3
from gendiff.differ import gendiff
from gendiff.cli import parse_args
from gendiff.gendiff_build import gendiff_diff


def main():
    args = parse_args()
    print(gendiff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
