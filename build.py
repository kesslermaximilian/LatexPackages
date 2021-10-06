from pathlib import *
import sys
sys.path.insert(0, 'PyTeX/')

from package_formatter import PackageFormatter
from replacements import make_default_commands

def build(build_dir: str):
    input_root = Path('./packages').resolve()
    output = input_root / build_dir
    for file in input_root.rglob('*.pysty'):
        formatter = PackageFormatter(package_name=file.with_suffix('').name)
        print('[PyTeX] Writing file {}'.format(formatter.file_name))
        make_default_commands(formatter)
        formatter.format_package(file, Path('./').resolve() / build_dir / str(file.parent.relative_to(input_root)))

if __name__ == "__main__":
    build('build')
