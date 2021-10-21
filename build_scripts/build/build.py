from pathlib import Path
import git

import PyTeX

from build_scripts.git_hook import get_latest_commit, is_recent

from .build_information import build_information


def build(src_dir: Path, build_dir: Path, check_existence: bool = True):
    print('[PyTeX] Getting git repository information...')
    extra_header, repo_description = build_information()
    print('[PyTeX] Building version {version} of LatexPackages'.format(version=repo_description))
    print('[PyTeX] Latest commit message: ' + get_latest_commit(git.Repo()).message.strip())
    if git.Repo().is_dirty(untracked_files=True):
        extra_header += ['WARNING: Local changes to git repository detected.',
                         '         The build will not be reproducible (!)']
    num_packages = 0
    num_skipped_packages = 0
    num_classes = 0
    num_skipped_classes = 0

    for file in src_dir.rglob('*.pysty'):
        output_dir = build_dir / str(file.parent.relative_to(src_dir))
        if not is_recent(file, git.Repo()):
            if not check_existence:
                print('[PyTex] Skipping file {file} since it was not modified since last build'.format(file=file.name))
                num_skipped_packages += 1
                continue
            else:
                if (output_dir / ('mkessler-' + str(file.with_suffix('.sty').name))).exists():
                    print('[PyTex] Skipping file {file} since it was not modified since '
                          'last build and already exists'.format(file=file.name))
                    num_skipped_packages += 1
                    continue

        num_packages += 1
        formatter = PyTeX.PackageFormatter(
            package_name=file.with_suffix('').name,
            extra_header=extra_header)
        print('[PyTeX] Writing file {}'.format(formatter.file_name))
        formatter.make_default_macros()
        formatter.format_file(file, output_dir)
    for file in src_dir.rglob('*.pycls'):
        output_dir = build_dir / str(file.parent.relative_to(src_dir))
        if not is_recent(file, git.Repo()):
            if not check_existence:
                print('[PyTex] Skipping file {file} since it was not modified since last build'.format(file=file.name))
                num_skipped_classes += 1
                continue
            else:
                if (output_dir / ('mkessler-' + str(file.with_suffix('.cls').name))).exists():
                    print('[PyTex] Skipping file {file} since it was not modified since '
                          'last build and already exists'.format(file=file.name))
                    num_skipped_classes += 1
                    continue
        output_dir = build_dir / str(file.parent.relative_to(src_dir))
        num_classes += 1
        formatter = PyTeX.ClassFormatter(
            class_name=file.with_suffix('').name,
            extra_header=extra_header)
        print('[PyTeX] Writing class file {}'.format(formatter.file_name))
        formatter.make_default_macros()
        formatter.format_file(input_path=file, output_dir=output_dir)
    build_info = {
        'build_time': '',
        'packages': {
            'built': '',
            'skipped': ''
        },
        'classes': {
          'built': '',
          'skipped': ''
        },
        'LatexPackages': {
            'version': '',
            'branch': '',
            'commit': '',
            'dirty': ''
        },
        'PyTeX': {
            'version': '',
            'branch': '',
            'commit': '',
            'dirty': ''
        }
    }
    print(f'[PyTeX] Successfully built {num_packages} packages (skipped {num_skipped_packages}) '
          f'and {num_classes} classes (skipped {num_skipped_classes}) in {build_dir}/')
