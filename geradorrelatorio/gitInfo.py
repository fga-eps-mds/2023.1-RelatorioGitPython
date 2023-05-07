from pygit2 import Repository, discover_repository
import os
from pygit2 import GIT_SORT_REVERSE, GIT_SORT_TIME


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
        f.write('numero de commits totais \n' + str(cont))
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
        f.write('numero de commits totais \n' + str(cont))
    f.close()

def get_commits():
    list = []
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        print(str(commits.id) + ' - ' + commits.message)
        list.append(str(commits.id) + ' - ' + commits.message)
    return list


def get_commits_by_user(usuario):
    list = []
    for commits in repository.walk(repository.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
        if commits.author.name == usuario:
            print(str(commits.id) + ' - ' + commits.message)
            list.append(str(commits.id) + ' - ' + commits.message)
    return list
