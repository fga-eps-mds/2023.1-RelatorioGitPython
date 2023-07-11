import pytest
from github import Github
from collections import defaultdict
from pygit2 import GIT_SORT_TIME, Repository, discover_repository
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import os
import sys
import re
from unittest.mock import Mock
from pandas.testing import assert_frame_equal

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


def get_commits_by_user(usuario: str, start_date: str, end_date: str):
    hashes = []
    messages = []

    commits = repo.get_commits()
    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            if commit.author.login.lower() == usuario.lower():
                messages.append(commit.commit.message)
                hashes.append(commit.sha[:6])

    df = pd.DataFrame({"Message":messages}, index=hashes)

    if df.empty is False:
        return df
    else:
        msg = "No commits with this user"
        return msg
    
def test_get_commits_by_user():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o repositório
    repo = g.get_repo(repo_name)

    usuario = 'rafa-kenji'
    start_date = '05-01-2023'
    end_date = '06-30-2023'

    result = get_commits_by_user(usuario, start_date, end_date)

    expected_messages = [
        'Merge pull request #58 from fga-eps-mds/refatoracao_biblioteca',
        'Correção da saída markdown\n\nCo-authored-by: Catlen Oliveira <99406424+catlenc@users.noreply.github.com>',
        'Merge pull request #52 from fga-eps-mds/pipeline-1',
        'Relacionar os commit por data\n\nCo-authored-by: Catlen Oliveira <99406424+catlenc@users.noreply.github.com>'
    ]
    expected_hashes = ['f8e353', 'fe0389', 'd49ca6', 'bdc947']
    expected_result = pd.DataFrame(
        {"Message": expected_messages},
        index=expected_hashes
    )

    if not result.equals(expected_result):
        print("Differences:")
        print(result.compare(expected_result))

    assert result.equals(expected_result)


def get_commit_dates():
    datas = []
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        data = datetime.fromtimestamp(commit.commit_time)
        datas.append(data.strftime("%Y-%m-%d %H:%M:%S"))
        if len(datas) == 3:  # Limita para as três primeiras datas
            #print(datas)
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
    expected_dates = ['2023-07-02 23:33:27', '2023-07-02 22:58:58', '2023-07-02 22:58:16']
    assert result == expected_dates


def get_commits_users(start_date: str, end_date: str):

    commit_users = []
    commits = repo.get_commits()
    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            author = commit.author.login
            if author in commit_users:
             continue

            commit_users.append(author)

    df = pd.DataFrame({"Users": commit_users})
    return df

def test_get_commits_users():
    # Chame a função para obter os usuários de commits
    result = get_commits_users('06-29-2023', '06-30-2023')

    # Defina o valor esperado para o resultado

    expected_users = ['GZaranza','lucaslobao-18','ViniciussdeOliveira','catlenc','FelipeDireito']
    expected_result = pd.DataFrame({"Users": expected_users})

    if not result.equals(expected_result):
        print("Differences:")
        print(result.compare(expected_result))    

    # Realize a comparação entre o resultado obtido e o valor esperado
    assert result.equals(expected_result)

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


def get_coAuthor(start_date: str, end_date: str):
    coauthors = []
    hashes = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            commit_message = commit.commit.message

            if 'Co-authored-by:' in commit_message:
                hashes.append(commit.commit.sha[:6])
                authors.append(commit.commit.author.name)

                lines = commit_message.splitlines()
                aux=[]
                for line in lines:
                    if line.startswith('Co-authored-by:'):
                        aux.append(line[16:].strip().split('<')[0])
                coauthors.append(aux)

    df = pd.DataFrame({"author": authors, "co-authors": coauthors}, index=hashes)

    if not df.empty:
        return df
    else:
        msg = "0 commits with Coauthors"
        return msg

def test_get_coAuthor():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o objeto repo usando o nome do repositório
    repo = g.get_repo(repo_name)

    # Chame a função de teste com o objeto repo
    result = get_coAuthor('06-28-2023', '06-29-2023')

    # Defina o valor esperado para o resultado
    expected_authors = ['lucaslobao-18', 'Vinicius de Oliveira Santos', 'Vinicius de Oliveira Santos', 'Vinicius de Oliveira Santos', 'Vinicius de Oliveira Santos', 'catlenc', 'lucaslobao-18']
    expected_coauthors = [['Catlen Oliveira'], ['Gabriel Zaranza'], ['Gabriel Zaranza'], ['Gabriel Zaranza'], ['Gabriel Zaranza'], ['lucaslobao-18, lucaslobao-18'], ['Catlen Oliveira']]
    expected_hashes = ['718b52', 'bf6229', '7ac306', '53546b', '715d50', 'f7bcfd', '6f0926']

    expected_result = pd.DataFrame({"author": expected_authors, "co-authors": expected_coauthors}, index=expected_hashes)
    expected_result = expected_result.reindex(index=result.index, columns=result.columns)

    # Converter listas de co-autores em strings separadas por vírgula e comparar valores independentemente da ordem
    result['co-authors'] = result['co-authors'].apply(lambda x: ', '.join(sorted([s.strip() for s in x])))
    expected_result['co-authors'] = expected_result['co-authors'].apply(lambda x: ', '.join(sorted([s.strip() for s in x])))

    if not result.equals(expected_result):
        print("Differences:")
        print(result.compare(expected_result))  
    
    assert_frame_equal(result, expected_result)


def commit_palavra(string: str, start_date: str, end_date: str):

    hashes = []
    messages = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:

            commit_message = commit.commit.message

            if string.lower() in commit_message.lower():

                hashes.append(commit.sha[:6])
                authors.append(commit.commit.author.name)
                messages.append(commit.commit.message)

    df = pd.DataFrame({"message":messages, "author": authors}, index=hashes)

    if df.empty is False:
        return df
    else:
        msg = "No commits with this word"
        return msg

def test_commit_palavra():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o repositório
    repo = g.get_repo(repo_name)

    result = commit_palavra('issues','06-28-2023', '06-29-2023')

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
    #result['message'] = result['message'].str.split('\n\n', n=1, expand=True)[0]
    result['message'] = result['message'].apply(lambda x: re.split('\n\n|\n', x, maxsplit=1)[0])


    # Comparar o conteúdo da mensagem de commit e o índice
    assert result['message'].to_list() == expected_result['message'].to_list()
    assert result['author'].to_list() == expected_result['author'].to_list()
    assert result.index.to_list() == expected_result.index.to_list()

def title_commits(start_date: str, end_date: str):

    commits = repo.get_commits()

    commit_titles = defaultdict(lambda: defaultdict(list))

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            author = commit.author
            if author:
                author_name = author.login
            else:
                author_name = 'Unknown'

            commit_title = commit.commit.message.splitlines()[0]

            if author_name in commit_titles:
                commit_titles[author_name].append(commit_title)
            else:
                commit_titles[author_name] = [commit_title]

    content = '#File Title Commits\n\n'
    for author, titles in commit_titles.items():
        content += f'## Usuário: {author}\n'
        content += f'### Títulos do commits:\n'
        for title in titles:
            content += f'- {title}\n'
        content += '\n'

    output = 'arquivo_title.md'

    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)

def test_title_commits():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o repositório
    repo = g.get_repo(repo_name)

    # Chame a função para gerar o arquivo de títulos dos commits
    title_commits('06-29-2023', '06-30-2023')

    # Verifique se o arquivo de saída foi criado
    output_file = 'arquivo_title.md'
    assert os.path.exists(output_file)

    # Verifique se o conteúdo do arquivo está correto
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    expected_content = '''#File Title Commits

## Usuário: GZaranza
### Títulos do commits:
- add o filtro de data nas defs tittle_commits, get_commits_by_user, commit_palavra
- Merge pull request #69 from fga-eps-mds/issue_65
- Merge branch 'main' into issue_65

## Usuário: lucaslobao-18
### Títulos do commits:
- Finaliza a funcao das issues com saida em markdown
- Cria funcao que busca as issues

## Usuário: ViniciussdeOliveira
### Títulos do commits:
- Refatorando e adicionando filtro data na função get_commits_users()
- Adicionando o filtro data na função get_coAuthor()
- Adicionando filtro data na função check_extension()
- Adicionando filtro de data na função calculate_commit_average()
- Merge pull request #68 from fga-eps-mds/grafico_no_markdown

## Usuário: catlenc
### Títulos do commits:
- Cria as listas com issues assinadas e nao assinadas

## Usuário: FelipeDireito
### Títulos do commits:
- Adiciona plot do grafico no markdown gerado
'''

    assert content.strip() == expected_content.strip()

    # Remover o arquivo de saída após o teste
    os.remove(output_file)

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

def issues_month(start_date: str, end_date: str):

    months_list = pd.period_range(start =start_date,end=end_date, freq='M')
    months_list = [month.strftime("%b-%Y") for month in months_list]

    issues = repo.get_issues(state='closed')

    count=[]


    for month in months_list:
        contador=0
        for issue in issues:
            if issue.pull_request is None and issue.closed_at.strftime("%b-%Y") == month:
                contador+=1
        count.append(contador)

    df = pd.DataFrame({"num_issues": count},index=months_list)

    return df


def test_issues_month():
    github_token = os.getenv('GITHUB_TOKEN')
    g = Github(github_token)

    repo_name = 'fga-eps-mds/2023.1-RelatorioGitPython'

    # Inicialize o objeto Github com o token de acesso pessoal
    g = Github(github_token)

    # Obtenha o objeto repo usando o nome do repositório
    repo = g.get_repo(repo_name)

    # Chame a função de teste
    result = issues_month('2023-01-01', '2023-06-30')

    # Defina o valor esperado para o resultado
    expected_issues = [0, 0, 0, 18, 14, 12]
    expected_months = ['Jan-2023', 'Feb-2023', 'Mar-2023', 'Apr-2023', 'May-2023', 'Jun-2023']

    expected_result = pd.DataFrame({"num_issues": expected_issues}, index=expected_months)

    # Verifique se o resultado é igual ao esperado
    assert_frame_equal(result, expected_result)

def issues_open():
    issues = repo.get_issues(state='open')

    content = '## Issues Abertas Assinadas\n'

    content += '| Titulo | Numero |\n'
    content += '|--------|--------|\n'

    for issue in issues:
        if issue.assignee:
            content += f'|{issue.title}|{issue.number}|\n'

    content += '\n\n'
    content += '## Issues Abertas Não Assinadas\n'

    content += '| Titulo | Numero |\n'
    content += '|--------|--------|\n'

    for issue in issues:
        if not issue.assignee:
            content += f'|{issue.title}|{issue.number}|\n'

    #Para testar a saída, descomente o print
    #print(content)
    return content

def test_issues_open():
    # Defina uma lista de objetos Issue simulando as issues do repositório
    issues = [
        {'title': 'Issue 1', 'number': 1, 'assignee': 'User 1'},
        {'title': 'Issue 2', 'number': 2, 'assignee': None},
        {'title': 'Issue 3', 'number': 3, 'assignee': 'User 2'}
    ]
    
    # Substitua a função repo.get_issues por uma função auxiliar que retorna as issues pré-definidas
    def get_issues(state):
        return [Mock(**issue) for issue in issues if state == 'open']
    
    # Chame a função de teste com a função auxiliar substituída
    result = issues_open(get_issues)
    
    # Defina a saída esperada
    expected_output = '''## Issues Abertas Assinadas

| Titulo | Numero |
|--------|--------|
|Issue 1|1|
|Issue 3|3|

## Issues Abertas Não Assinadas
| Titulo | Numero |
|--------|--------|
|Issue 2|2|
'''

    # Verifique se a saída da função é igual à saída esperada
    assert result == expected_output

def gerar_relatorio():
    content = '## Relatório Geral\n\n'

    content += check_extension()
    content += '\n\n'

    content += '## Lista de Commits com Coauthor\n\n'

    # Parte funcionando COAUTHOR ------------------------------------------

    coaut = get_coAuthor()

    content += '| Hash | Author | Coauthor | Data |\n'
    content += '|------|--------|----------|------|\n'

    for indice, linha in coaut.iterrows():
        content += f'|{indice}'
        for coluna, valor in linha.items():
            content += f'|{valor}'
            nada = {coluna}
        content += '|\n'

    content += '\n\n'

    # Parte funcionando COAUTHOR ------------------------------------------

    # Parte Média ---------------------------------------------------------

    content += '## Commits por pessoa e Média Geral\n\n'
    commits = calculate_commit_average()
    graph_path = 'commit_average_graph.png'

    content += '| índice | Author | Commits | Avarege |\n'
    content += '|--------|--------|---------|---------|\n'

    for indice, linha in commits.iterrows():
        content += f'|{indice}'
        for coluna, valor in linha.items():
            content += f'|{valor}'
            nada = {coluna}
        content += '|\n'

    content += '\n\n'
    # print(content)

    content += f'![Commit Average Graph]({graph_path})\n\n'
    output = 'relatorio_geral.md'

    with open(output, 'w', encoding='utf-8') as f:

        f.write(content)

def test_gerar_relatorio():
    # Caso de teste da função gerar_relatorio
    expected_content = '## Relatório Geral\n\n'
    expected_content += check_extension()
    expected_content += '\n\n'
    expected_content += '## Lista de Commits com Coauthor\n\n'
    expected_content += '| Hash | Author | Coauthor | Data |\n'
    expected_content += '|------|--------|----------|------|\n'
    expected_content += '| 718b52 | lucaslobao-18 | Catlen Oliveira | ...\n'
    # Definir o conteúdo esperado completo

    # Chamar a função gerar_relatorio
    result = gerar_relatorio()

    # Verificar se o resultado é igual ao conteúdo esperado
    assert result == expected_content

def check_extension(start_date: str, end_date: str):
    try:
        extension_by_author = defaultdict(lambda: defaultdict(list))

        commits = repo.get_commits()

        for commit in commits:
            commit_date = commit.commit.author.date
            commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
            if commit_date_str >= start_date and commit_date_str <= end_date:
                author = commit.author.login
                file_modify = commit.files

                for file in file_modify:
                    extension = file.filename.split('.')[-1]
                    filename = file.filename

                    extension_by_author[author][extension].append(filename)

        content = '## File Extensions Report by Author\n\n'

        for author, extensions in extension_by_author.items():
            content += f'## Author: {author} \n\n'
            content += '| Extension / Files |\n'
            content += '| -------- | \n'
            for extension, files in extensions.items():
                file_list = '| \n'.join(files)
                content += f'| **{extension}** | \n'
                content += f' {file_list} | \n'
            content += "\n"

        output = 'arquivo.md'

        with open(output, 'w', encoding='utf-8') as f:
            f.write(content)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    return content

def test_check_extension():
    # Caso de teste da função check_extension
    start_date = '06-01-2023'
    end_date = '06-30-2023'

    # Chamar a função check_extension
    result = check_extension(start_date, end_date)

    # Verificar se o resultado não é vazio
    assert result != ''

    # Verificar se o arquivo foi criado corretamente
    assert os.path.exists('arquivo.md')
    assert os.path.isfile('arquivo.md')

    # Verificar se o conteúdo do arquivo é igual ao resultado retornado
    with open('arquivo.md', 'r', encoding='utf-8') as f:
        file_content = f.read()

    assert file_content == result