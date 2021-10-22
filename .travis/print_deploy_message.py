from deploy.deploy_message import get_deploy_message
import git

if __name__ == "__main__":
    repo = git.Repo(search_parent_directories=True)
    msg = get_deploy_message(repo)
    print(msg)
