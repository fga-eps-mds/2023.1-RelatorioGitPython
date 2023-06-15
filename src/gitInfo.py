from pygit2 import Repository, discover_repository
import pandas as pd
import os
from pygit2 import GIT_SORT_REVERSE, GIT_SORT_TIME
from pygit2 import *
import datetime
import matplotlib.pyplot as plt

current_working_directory = os.getcwd()
repository_path = discover_repository(current_working_directory)
repository = Repository(repository_path)


def all_commits(arquivo):
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
    f.close()

def get_commits():
    list = []
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        #print(str(commits.id) + ' - ' + commits.message)
        list.append(str(commits.id) + ' - ' + commits.message)
    return list


def get_commits_by_user(usuario):
    list = []
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        if commits.author.name == usuario:
            print(str(commits.id) + ' - ' + commits.message)
            list.append(str(commits.id) + ' - ' + commits.message)
    return list


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
    dates = []
    columns = ['hash','author','co-author']
# Obter o commit mais recente (HEAD)
    commit = repository.revparse_single('HEAD')

# Percorrer todos os commits
    for commit in repository.walk(commit.id, GIT_SORT_TOPOLOGICAL | GIT_SORT_REVERSE):
        commit_message = commit.message

        if 'Co-authored-by:' in commit_message:

            hashes.append(str(commit.hex)[:6])
            authors.append(commit.author.name)
            dates.append(datetime.datetime.fromtimestamp(commit.commit_time))

            lines = commit.message.splitlines()
            aux=[]
            for line in lines:
                if line.startswith('Co-authored-by:'):
                    aux.append(line[16:].strip().split('<')[0])
            coauthors.append(aux)
               

    df_coauthor = pd.DataFrame({"authors": authors,"co-authors":coauthors,"date": dates}, index=hashes)
    #print (df_coauthor)
    return df_coauthor

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
