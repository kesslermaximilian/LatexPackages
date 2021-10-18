import sys
from pathlib import Path

from build_scripts.build import build

if __name__ == "__main__":
    check_existence = True
    if len(sys.argv) == 2:
        if sys.argv[1] == '--only-new':
            check_existence = False
    build(
        src_dir=Path('./src').resolve(),
        build_dir=Path('./build').resolve(),
        check_existence=check_existence
    )
