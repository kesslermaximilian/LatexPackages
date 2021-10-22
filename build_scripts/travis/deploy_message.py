import os
from PyTeX.build.git_hook import get_latest_commit


def get_deploy_message(repo):
    old_msg = get_latest_commit(repo).message
    return "{old_msg}\n" \
           "\n" \
           "Build branch {branch} ({hexsha}) from {repo_name}" \
        .format(old_msg=old_msg,
                branch=os.environ['TRAVIS_BRANCH'],
                hexsha=get_latest_commit(repo).hexsha[0:7],
                repo_name='kesslermaximilian/LatexPackages')
