#! /usr/bin/python3
import argparse
import pathlib

from build_scripts.build import build
from build_scripts.build.config import FILENAME_TYPE_RAW_NAME, FILENAME_TYPE_PREPEND_AUTHOR


def main():
    parser = argparse.ArgumentParser(description='Incrementally build LatexPackages with PyTeX')
    input_group = parser.add_mutually_exclusive_group(required=True)
    output_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        '-s', '--source-dir',
        metavar='SRC_DIR',
        help='Relative or absolute path to source directory of .pysty or .pycls files',
        type=pathlib.Path,
        nargs='?',
        default='./src',
        dest='src_dir'
    )
    output_group.add_argument(
        '-b', '--build-dir',
        metavar='BUILD_DIR',
        help='Relativ or absolute path to output directory for processed packages and classes',
        type=pathlib.Path,
        nargs='?',
        default='./build',
        dest='build_dir'
    )
    parser.add_argument(
        '-r', '--recursive',
        help='Recursively search subdirectories for files. Default: false',
        action='store_true',
        dest='recursive'
    )
    input_group.add_argument(
        '-i', '--input-file',
        metavar='FILE',
        help='Filename to be built. Can be in valid .pysty or .pycls format',
        type=pathlib.Path,
        dest='input_file'
    )
    output_group.add_argument(
        '-n', '--name',
        help='Name of the package / class to be formatted.',
        type=str,
        choices=[FILENAME_TYPE_RAW_NAME, FILENAME_TYPE_PREPEND_AUTHOR],
        default=FILENAME_TYPE_PREPEND_AUTHOR,
        dest='latex_name'
    )
    parser.add_argument(
        '-g', '--git-version',
        help='Insert git version information into build. This assumes your input'
             'files are located in a git repository. Default: false',
        action='store_true',
        dest='use_git'
    )
    parser.add_argument(
        '-d', '--allow-dirty',
        help='If git flag is set, allow building of a dirty repo. Default: false',
        action='store_true',
        dest='allow_dirty'
    )
    parser.add_argument(
        '-p',
        '--pytex-version',
        help='Write PyTeX version information into built LaTeX files',
        action='store_true',
        dest='include_pytex_version'
    )
    parser.add_argument(
        '-t', '--build-time',
        help='Insert build time into built LaTeX files',
        action='store_true',
        dest='include_timestamp'
    )
    parser.add_argument(
        '-l', '--license',
        help='Insert MIT license into package header',
        action='store_true',
        dest='include_license'
    )
    parser.add_argument(
        '-a', '--author',
        help='Set author of packages',
        type=str,
        dest='author'
    )
    parser.add_argument(
        '-f', '--force',
        help='Overwrite unknown existing files without confirmation',
        action='store_true',
        dest='overwrite_existing_files'
    )
    args = parser.parse_args()
    build(**vars(args))


if __name__ == "__main__":
    main()
