import git as GitPy

class Git:
    def __init__(self, path):
        self.repo = GitPy.Repo(path)

    def clone(self, url, path):
        return GitPy.Repo.clone_from(url, path)

    def get_branches(self):
        return self.repo.branches

    def get_commits(self, branch):
        return self.repo.iter_commits(branch)

    def get_commit(self, commit):
        return self.repo.commit(commit)

    def get_file(self, commit, file):
        return self.repo.git.show(f'{commit}:{file}')