from build_scripts.build import build
from pathlib import Path

if __name__ == "__main__":
    build(
        src_dir=Path('./src').resolve(),
        build_dir=Path('./build').resolve()
    )
