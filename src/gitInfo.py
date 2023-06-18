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


""" def all_commits(arquivo):
    list = []
    cont = 0
    
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        list.append(str(commits.id) + ' - ' + commits.message)
        cont = cont+1
    with open ("{}.txt".format(arquivo), "w") as f:
        for commit in list:
            f.write(commit + '\n')
        f.write('numero de commits totais ' + str(cont))
    f.close()


def email_commits(arquivo, email):
    list = []
    cont = 0
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        if commits.author.email == email:
            list.append(str(commits.id) + ' - ' + commits.message)
            cont = cont + 1
    with open ("{}.txt".format(arquivo), "w") as f:
        for commit in list:
            f.write(commit + '\n')
        f.write('numero de commits totais ' + str(cont))
    f.close() """

""" def get_commits():
    list = []
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        #print(str(commits.id) + ' - ' + commits.message)
        list.append(str(commits.id) + ' - ' + commits.message)
    return list """


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