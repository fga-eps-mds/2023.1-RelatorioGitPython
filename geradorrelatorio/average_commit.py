from pygit2 import *
from collections import defaultdict
import os
import pandas as pd
import matplotlib.pyplot as plt
from github import Github
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token do GitHub do arquivo .env
github_token = os.getenv('GITHUB_TOKEN')

github = Github(github_token)

owner = 'fga-eps-mds'
repo = '2023.1-RelatorioGitPython'

def calculate_commit_average():

    repository = github.get_repo(f'{owner}/{repo}')
    
    commits_count = defaultdict(int)
    
    for commit in repository.get_commits():
        
        author = commit.author
        name = author.login if author else "Unknown"
        
        # Incrementa o numero de commits do autor
        commits_count[name] += 1
        

    total_commits = sum(commits_count.values())
    qtd_user = len(commits_count)

    average_total = total_commits / qtd_user

    data = {'Author': [], 'Commits': []}

    for author, num_commits in commits_count.items():
        data['Author'].append(author)
        data['Commits'].append(num_commits)
    
    df = pd.DataFrame(data)
    df = df.sort_values(by='Commits', ascending=False)

    print(df)

    df['Average'] = average_total # df da media total

    # Plotar um gráfico com as média de cada user

    plt.bar(df['Author'], df['Commits'])
    plt.axhline(y=average_total, color='r', linestyle='-', label='Average')
    plt.xlabel('Author')
    plt.ylabel('Commits')
    plt.title('Commits per Author')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()