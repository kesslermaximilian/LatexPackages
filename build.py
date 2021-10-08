from pathlib import *
import sys
import git
from datetime import *

sys.path.insert(0, 'PyTeX/')

from package_formatter import PackageFormatter
from class_formatter import ClassFormatter
from git_version import git_describe, get_latest_commit

BUILD_DETAILS = [
    "Build details:",
    "  Build time: {build_time}",
    "  PyTeX version: {pytex_version} (commit {pytex_commit_hash})",
    "  LatexPackages version: {packages_version} (commit {packages_commit_hash})"
]


def build_details():
    repo = git.Repo()
    repo_description = git_describe(get_latest_commit(repo))
    pytex_repo = repo.submodule('PyTeX').module()
    pytex_repo_description = git_describe(get_latest_commit(pytex_repo))
    return list(map(lambda line: line.format(
        build_time=datetime.now().strftime('%Y/%m/%d %H:%M'),
        pytex_version=pytex_repo_description,
        pytex_commit_hash=get_latest_commit(pytex_repo).hexsha[0:7],
        packages_version=repo_description,
        packages_commit_hash=get_latest_commit(repo).hexsha[0:7]
    ), BUILD_DETAILS)), repo_description


def build(build_dir: str):
    input_root = Path('./packages').resolve()
    output = input_root / build_dir
    print('[PyTeX] Getting git repository information...')
    extra_header, repo_description = build_details()
    print('[PyTeX] Building version {version} of LatexPackages'.format(version=repo_description))
    print('[PyTeX] Latest commit message: ' + get_latest_commit(git.Repo()).message.strip())
    if git.Repo().is_dirty():
        extra_header += ['WARNING: Local changes to git repository detected.',
                         '         The build will not be reproducible (!)']
    num_packages = 0
    num_classes = 0
    for file in input_root.rglob('*.pysty'):
        num_packages += 1
        formatter = PackageFormatter(package_name=file.with_suffix('').name, extra_header=extra_header)
        print('[PyTeX] Writing file {}'.format(formatter.file_name))
        formatter.make_default_macros()
        formatter.format_file(file, Path('./').resolve() / build_dir / str(file.parent.relative_to(input_root)))
    for file in input_root.rglob('*.pycls'):
        num_classes += 1
        formatter = ClassFormatter(class_name=file.with_suffix('').name, extra_header=extra_header)
        print('[PyTeX] Writing class file {}'.format(formatter.file_name))
        formatter.make_default_macros()
        formatter.format_file(file, Path('./').resolve() / build_dir / str(file.parent.relative_to(input_root)))
    print(f'[PyTeX] Successfully built {num_packages} packages and {num_classes} classes in {build_dir}/')


if __name__ == "__main__":
    build('build')
