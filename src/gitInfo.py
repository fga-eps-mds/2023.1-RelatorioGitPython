from pygit2 import Repository, discover_repository
from collections import defaultdict
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
from github import Github
from pygit2 import GIT_SORT_REVERSE, GIT_SORT_TIME
from pygit2 import *

load_dotenv()
#pegando o token do github
github_token = os.getenv('GITHUB_TOKEN')
#dando acesso a biblioteca
g=Github(github_token)
#escolhendo o repositorio a ser analisado
repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")

current_working_directory = os.getcwd()
repository_path = discover_repository(current_working_directory)
repository = Repository(repository_path)


def get_commits_by_user(usuario):
    hashes = []
    messages = []

    commits = repo.get_commits()
    count =0
    for commit in commits:
        if commit.author.login == usuario:
            messages.append(commit.commit.message)
            hashes.append(commit.sha[:6])
            count+=1

    df = pd.DataFrame({"message":messages}, index=hashes)
    print(count)
    return df


def get_commit_dates():
    datas = []
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        data = datetime.datetime.fromtimestamp(commit.commit_time)
        datas.append(data.strftime("%Y -%m -%d %H:%M:%S"))
    return datas

def get_commits_users():
    commit_users = set()
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        author = commit.author
        commit_users.add(f'{author.name}')
        for i in commit_users:
            if(author.name != i):
                commit_users.add(f'{author.name}')
    return commit_users


def get_commits_email():
    commit_users = set()
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        author = commit.author
        commit_users.add(f'{author.email}')
        for i in commit_users:
            if(author.email != i):
                commit_users.add(f'{author.email}')
    return commit_users

def get_coAuthor():
    coauthors = []
    hashes = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:
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

    df = pd.DataFrame({"authors": authors,"co-authors":coauthors}, index=hashes)

    return df

def issues_month(star_date: str, end_date: str):

    months_list = pd.period_range(start =star_date,end=end_date, freq='M')
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



    # print(df)
    plt.bar(months_list, df['num_issues'])
    plt.xlabel('Months')
    plt.ylabel('Issues')
    plt.title('Issues per month')
    plt.yticks(range(0,max(df['num_issues']+1)))
    plt.xticks(rotation=45)
    plt.show()

def calculate_commit_average():

    commits = repo.get_commits()

    commits_count = defaultdict(int)

    for commit in commits:

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

def commit_data(date: str):
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

    # columns = ['hash', 'message', 'author']
    # df = pd.DataFrame({"message": messages, "author": authors}, index=hashes)

    content = '#File Commit by date\n\n'

    for author, message in zip(authors, messages):
        content += f'## Author: {author} \n\n'

        content += '| -------- | \n'
        content += f'## Messages: {message} \n\n'

        content += '| -------- | \n'
        content += "\n"

    output = 'arquivo_data.md'

    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)

    #return df

def commit_palavra(string: str):

    hashes = []
    messages = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:

        commit_message = commit.commit.message
        #re.search(palavra, commit_message,re.IGNORECASE)!=None:

        if string in commit_message:

            hashes.append(commit.sha[:6])
            authors.append(commit.commit.author.name)
            messages.append(commit.commit.message)


    columns = ['hash','message','author']
    df = pd.DataFrame({"message":messages, "author": authors}, index=hashes)

    return df

def check_extension():
    try:
        extension_by_author = defaultdict(lambda: defaultdict(list))

        commits = repo.get_commits()

        for commit in commits:
            author = commit.author.login
            file_modify = commit.files

            for file in file_modify:
                extension = file.filename.split('.')[-1]
                filename = file.filename

                extension_by_author[author][extension].append(filename)

        content = '#File Extensions Report by Author\n\n'

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

def title_commits():

    commits = repo.get_commits()

    commit_titles = defaultdict(lambda: defaultdict(list))

    for commit in commits:
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





def commit_data2(date: str):
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


def calculate_commit_average(repo):
    commits = repo.get_commits()
    commits_count = defaultdict(int)

    for commit in commits:
        author = commit.author
        name = author.login if author else "Unknown"
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

    df['Average'] = average_total

    plt.bar(df['Author'], df['Commits'])
    plt.axhline(y=average_total, color='r', linestyle='-', label='Average')
    plt.xlabel('Author')
    plt.ylabel('Commits')
    plt.title('Commits per Author')
    plt.legend()
    plt.xticks(rotation=45)
    plt.savefig('commit_average_graph.png')
    plt.close()
