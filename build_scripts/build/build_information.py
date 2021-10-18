import git
import datetime

from build_scripts.git_hook import git_describe, get_latest_commit

from .config import BUILD_DETAILS


def build_information():
    repo = git.Repo()
    repo_description = git_describe(get_latest_commit(repo))
    pytex_repo = repo.submodule('PyTeX').module()
    pytex_repo_description = git_describe(get_latest_commit(pytex_repo))
    return list(map(lambda line: line.format(
        build_time=datetime.datetime.now().strftime('%Y/%m/%d %H:%M'),
        pytex_version=pytex_repo_description,
        pytex_commit_hash=get_latest_commit(pytex_repo).hexsha[0:7],
        packages_version=repo_description,
        packages_commit_hash=get_latest_commit(repo).hexsha[0:7]
    ), BUILD_DETAILS)), repo_description
