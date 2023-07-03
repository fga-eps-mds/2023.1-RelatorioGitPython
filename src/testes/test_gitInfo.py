import pytest
from github import Github
from collections import defaultdict
from pygit2 import GIT_SORT_TIME, Repository, discover_repository
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import os
import sys
import json

# Adicionar o diretório 'src' ao caminho de busca de módulos do Python
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)

dotenv_path = os.path.join(os.path.dirname(__file__), 'testes', '.env')
load_dotenv(dotenv_path)

github_token = os.getenv('GITHUB_TOKEN')

g = Github(github_token)

repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")

current_working_directory = os.getcwd()
repository_path = discover_repository(current_working_directory)
repository = Repository(repository_path)
'''
def get_commits_by_user(username):
    hashes = []
    messages = []

    commits = repo.get_commits()
    count = 0
    for commit in commits:
        if commit.commit.author.name == username:
            messages.append(commit.commit.message)
            hashes.append(commit.sha[:6])
            count += 1

    df = pd.DataFrame({"message": messages}, index=hashes)
    print(count)
    return df

def test_get_commits_by_user():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o repositório
    repo = g.get_repo(repo_name)

    result = get_commits_by_user('rafa-kenji')

    expected_result = pd.DataFrame(
        {"message": ['Merge pull request #58 from fga-eps-mds/refatoracao_biblioteca', 'Merge pull request #52 from fga-eps-mds/pipeline-1\n\nPipeline 1']},
        index=['f8e353', 'd49ca6']
    )

    assert str(result) == str(expected_result)

def get_commit_dates():
    datas = []
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        data = datetime.fromtimestamp(commit.commit_time)
        datas.append(data.strftime("%Y-%m-%d %H:%M:%S"))
        if len(datas) == 3:  # Limita para as três primeiras datas
            print(datas)
            break
    return datas

def test_get_commit_dates():
    # Chame a função para obter as datas
    result = get_commit_dates()

    # Verifique se o resultado é uma lista
    assert isinstance(result, list)

    # Verifique se o resultado contém três datas
    assert len(result) == 3

    # Verifique se as datas estão corretas (substitua pelas datas esperadas)
    expected_dates = ['2023-06-27 12:30:26', '2023-06-27 11:50:35', '2023-06-22 13:47:12']
    assert result == expected_dates

def get_commits_users():
    commit_users = set()
    count = 0
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        author = commit.author
        commit_users.add(author.name)
        count += 1
        if count == 3:  # Limita para os três primeiros usuários
            break
    return commit_users


def test_get_commits_users():
    # Chame a função para obter os usuários de commits
    result = get_commits_users()

    # Verifique se o resultado é um conjunto (set)
    assert isinstance(result, set)

    # Verifique se o resultado contém exatamente três usuários
    assert len(result) == 2

    # Defina o valor esperado para o resultado
    expected_result = {'Rafael Kenji'}

    # Realize a comparação entre o resultado obtido e o valor esperado
    assert result == expected_result

def get_commits_email():
    commit_emails = set()
    count = 0
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        author = commit.author
        commit_emails.add(author.email)
        count += 1
        if count == 3:  # Limite para três emails
            break
    return commit_emails

def test_get_commits_email():
    # Chame a função de teste com a lista de commits
    result = get_commits_email()

    # Defina o valor esperado para o resultado
    expected_result = {'rafak.taira@gmail.com'}

    # Realize a comparação entre o resultado obtido e o valor esperado
    assert result == expected_result

def get_coAuthor():
    coauthors = []
    hashes = []
    authors = []

    commits = repo.get_commits()
    count = 0

    for commit in commits:
        if count == 3:  # Limite para três coautores
            break

        commit_message = commit.commit.message

        if 'Co-authored-by:' in commit_message:
            hashes.append(commit.commit.sha[:6])
            authors.append(commit.commit.author.name)

            lines = commit_message.splitlines()
            aux = []
            for line in lines:
                if line.startswith('Co-authored-by:'):
                    aux.append(line[16:].strip().split('<')[0])
            coauthors.append(aux)

        count += 1

    df = pd.DataFrame({"authors": authors, "co-authors": coauthors}, index=hashes)

    return df


def test_get_coAuthor():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o objeto repo usando o nome do repositório
    repo = g.get_repo(repo_name)

    # Chame a função de teste com o objeto repo
    result = get_coAuthor()

    # Defina o valor esperado para o resultado
    expected_result = pd.DataFrame(
        {"authors": ['lucaslobao-18'], "co-authors": [['Catlen Oliveira ']]},
        index=['718b52']
    )

    # Realize a comparação entre o resultado obtido e o valor esperado
    assert result.equals(expected_result)
'''
def commit_palavra(string: str):

    hashes = []
    messages = []
    authors = []
    count = 0

    commits = repo.get_commits()

    for commit in commits:
        commit_message = commit.commit.message

        if string in commit_message:
            hashes.append(commit.sha[:6])
            authors.append(commit.commit.author.name)
            messages.append(commit.commit.message)
            count += 1

        if count == 3:
            break

    columns = ['hash','message','author']
    df = pd.DataFrame({"message": messages, "author": authors}, index=hashes)
    
    return df

def test_commit_palavra():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o repositório
    repo = g.get_repo(repo_name)

    result = commit_palavra('issues')

    expected_result = pd.DataFrame(
        {"message": [
            'Finaliza a funcao das issues com saida em markdown',
            'Cria as listas com issues assinadas e nao assinadas',
            'Cria funcao que busca as issues'
        ],
        "author": [
            'lucaslobao-18',
            'catlenc',
            'lucaslobao-18'
        ]},
        index=['718b52', 'f7bcfd', '6f0926']
    )

    # Remover parte adicional das mensagens de commit
    result['message'] = result['message'].str.split('\n\n', n=1, expand=True)[0]

    # Comparar o conteúdo da mensagem de commit e o índice
    assert result['message'].to_list() == expected_result['message'].to_list()
    assert result['author'].to_list() == expected_result['author'].to_list()
    assert result.index.to_list() == expected_result.index.to_list()

