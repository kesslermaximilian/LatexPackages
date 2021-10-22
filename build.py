#! /usr/bin/python3
import sys

from PyTeX.build import parse_and_build

if __name__ == "__main__":
    parse_and_build(sys.argv[1:])
