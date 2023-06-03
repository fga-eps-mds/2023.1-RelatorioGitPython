from pygit2 import Repository, discover_repository
from pygit2 import GIT_SORT_TIME
from pygit2 import *
from collections import defaultdict
import os
import pandas as pd
import matplotlib.pyplot as plt


 
current_working_directory = os.getcwd() 
repository_path = discover_repository(current_working_directory) 
repository = Repository(repository_path) 

def calculate_commit_average():
    
    commits_count = defaultdict(int)
    
    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        
        # Obter o email do autor
        name = commit.author.name
        
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

    df['Average'] = average_total # df da media total

    above_avg = df[df['Commits'] > df['Average']]
    below_avg = df[df['Commits'] < df['Average']]

    print(above_avg)
    print()
    print(below_avg)

    '''
    print('Média de Commits/Author do Repositório: ', average_total)

    acima_media = []
    abaixo_media = []

    for author, num_commits in commits_count.items():
        print(f'{author}: {num_commits}')
        if num_commits > average_total:
            acima_media.append(author)
        elif num_commits < average_total:
            abaixo_media.append(author)
    
    print('\n')

    print('Usuários acima da média\n')
    for author in acima_media: 
        print(author)

    print('\n')

    print('Usuários abaixo da média\n')
    for author in abaixo_media:
        print(author)
    '''
    
