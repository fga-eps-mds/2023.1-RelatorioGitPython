from pygit2 import Repository, discover_repository
import os
from pygit2 import GIT_SORT_REVERSE, GIT_SORT_TIME
from pygit2 import *

# Abrir o repositório Git
current_working_directory = os.getcwd()
repository_path = discover_repository(current_working_directory)
repository = Repository(repository_path)

# Obter o commit mais recente (HEAD)
commit = repository.revparse_single('HEAD')

# Percorrer todos os commits
for commit in repository.walk(commit.id, GIT_SORT_TOPOLOGICAL):
    # Comparar a mensagem do commit com a linha "Co-authored-by"
    commit_message = commit.message
    if 'Co-authored-by:' in commit_message:
        print(f'O commit {commit.hex} tem coautores.')
    else:
        print(f'O commit {commit.hex} não tem coautores.')
