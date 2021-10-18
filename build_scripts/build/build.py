from pathlib import Path
import git

import PyTeX

from build_scripts.git_hook.git_version import get_latest_commit

from .build_information import build_information


def build(src_dir: Path, build_dir: Path):
    print('[PyTeX] Getting git repository information...')
    extra_header, repo_description = build_information()
    print('[PyTeX] Building version {version} of LatexPackages'.format(version=repo_description))
    print('[PyTeX] Latest commit message: ' + get_latest_commit(git.Repo()).message.strip())
    if git.Repo().is_dirty(untracked_files=True):
        extra_header += ['WARNING: Local changes to git repository detected.',
                         '         The build will not be reproducible (!)']
    num_packages = 0
    num_classes = 0

    for file in src_dir.rglob('*.pysty'):
        num_packages += 1
        formatter = PyTeX.PackageFormatter(
            package_name=file.with_suffix('').name,
            extra_header=extra_header)
        print('[PyTeX] Writing file {}'.format(formatter.file_name))
        formatter.make_default_macros()
        formatter.format_file(file, build_dir / str(file.parent.relative_to(src_dir)))
    for file in src_dir.rglob('*.pycls'):
        num_classes += 1
        formatter = PyTeX.ClassFormatter(
            class_name=file.with_suffix('').name,
            extra_header=extra_header)
        print('[PyTeX] Writing class file {}'.format(formatter.file_name))
        formatter.make_default_macros()
        formatter.format_file(file, build_dir / str(file.parent.relative_to(src_dir)))
    print(f'[PyTeX] Successfully built {num_packages} packages and {num_classes} classes in {build_dir}/')
