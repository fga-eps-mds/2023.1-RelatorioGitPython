import os
from collections import defaultdict
from github import Github
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token do GitHub do arquivo .env
github_token = os.getenv('GITHUB_TOKEN')

github = Github(github_token)

owner = 'fga-eps-mds'
repository = '2023.1-RelatorioGitPython'

def title_commits():
    
    repo = github.get_repo(f'{owner}/{repository}')

    commits = repo.get_commits()

    commit_titles = defaultdict(lambda: defaultdict(list))

    for commit in commits:
        author = commit.author
        if author:
            author_name = author.login
        else:
            author_name = 'Unknown'

        commit_title = commit.commit.message

        if author_name in commit_titles:
            commit_titles[author_name].append(commit_title)
        else:
            commit_titles[author_name] = [commit_title]

    for author, titles in commit_titles.items():
        print(f'Usuário: {author}')
        print(f'Títulos do commits:')
        for title in titles:
            print(f'- {title}')
        print()


title_commits()