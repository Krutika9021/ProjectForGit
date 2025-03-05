import git
import os

def initialize_repo(repo_path):
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
    
    repo = git.Repo.init(repo_path)
    print(f"Initialized empty Git repository in {repo_path}")
    return repo

def create_file(repo_path, filename, content):
    file_path = os.path.join(repo_path, filename)
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Created file {filename}")
    return file_path

def commit_changes(repo, message):
    repo.git.add(A=True)
    repo.index.commit(message)
    print(f"Committed changes: {message}")

def show_commit_history(repo):
    print("Commit history:")
    for commit in repo.iter_commits():
        print(f"{commit.hexsha[:7]} - {commit.message.strip()}")

if __name__ == "__main__":
    repo_path = "./test_repo"
    repo = initialize_repo(repo_path)
    
    file_path = create_file(repo_path, "example.txt", "Hello, GitPython!")
    
    commit_changes(repo, "Initial commit")
    
    show_commit_history(repo)
