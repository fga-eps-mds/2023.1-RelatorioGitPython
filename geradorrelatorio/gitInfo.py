from pygit2 import Repository, discover_repository
import os
from pygit2 import GIT_SORT_REVERSE, GIT_SORT_TIME
from pygit2 import *
import datetime


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
