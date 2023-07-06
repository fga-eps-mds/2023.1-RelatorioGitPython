from github import Github
import pytest
from collections import defaultdict
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), 'testes', '.env')
load_dotenv(dotenv_path)

github_token = os.getenv('GITHUB_TOKEN')

g = Github(github_token)

def commit_data(repo, date: str):
    hashes = []
    messages = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")

        if commit_date_str == date:
            hashes.append(commit.sha[:6])
            authors.append(commit.commit.author.name)
            messages.append(commit.commit.message)

    content = '# File Commit by date\n\n'

    for author, message in zip(authors, messages):
        content += f'## Author: {author} \n\n'
        content += '| Message | \n'
        content += '| -------- | \n'
        content += f'{message} \n\n'
        content += '| -------- | \n\n'

    # Generate and save the graph
    calculate_commit_average(repo)
    graph_path = 'commit_average_graph.png'

    # Include the graph in the markdown file
    content += '## Graph\n\n'
    content += f'![Commit Average Graph]({graph_path})\n\n'

    output = 'arquivo_data.md'

    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)

    return hashes

def calculate_commit_average(start_date: str, end_date: str):
    repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")

    commits = repo.get_commits()

    commits_count = defaultdict(int)

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
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

    #print(df)

    df['Average'] = average_total # df da media total

    return df

def test_commit_data():
    
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o objeto repo usando o nome do repositório
    repo = g.get_repo(repo_name)

    # Chame a função de teste com o objeto repo
    result = commit_data(repo, '06-15-2023')

    expected_hashes = ['ad2ba3']
    assert result == expected_hashes

def test_calculate_commit_average():
    
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)
    
    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o objeto repo usando o nome do repositório
    repo = g.get_repo(repo_name)

    # Chame a função de teste com o objeto repo
    result = calculate_commit_average('06-29-2023', '06-30-2023')
    expected_users = ['GZaranza', 'lucaslobao-18', 'ViniciussdeOliveira', 'catlenc', 'FelipeDireito']
    expected_commits = [3, 2, 5, 1, 1]
    average_total = 2.4

    expected_result = pd.DataFrame({"Author": expected_users, "Commits": expected_commits, "Average": average_total}, index=[0,1,2,3,4])
    expected_result = expected_result.sort_values(by='Commits', ascending=False)

    if not result.equals(expected_result):
        print("Differences:")
        print(result.compare(expected_result))     

    assert result.equals(expected_result)