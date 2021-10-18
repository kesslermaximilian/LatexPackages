from .git_version import get_latest_commit


def is_recent(file, repo):
    modified_files = [item.a_path for item in repo.index.diff(None)]
    if file in modified_files:
        return True

    for parent in get_latest_commit(repo).parents:
        newly_committed_files = [item.a_path for item in repo.index.diff(parent)]
        if file in newly_committed_files:
            return True
    return False

