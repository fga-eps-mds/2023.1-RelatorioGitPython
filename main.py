from pygit2 import Repository, discover_repository
import os
from pygit2 import GIT_SORT_REVERSE, GIT_SORT_TIME


current_working_directory = os.getcwd()
repository_path = discover_repository(current_working_directory)
repo = Repository(repository_path)

i = 0
email = 'lucaslobao14df@gmail.com'


with open('commits.txt', 'w') as f:
   for commit in repo.walk(repo.head.target, GIT_SORT_TIME | GIT_SORT_REVERSE):
      print(commit.message)
      if commit.author.email == email:    
         f.write(str(commit.id)+' - ' + commit.message + '\n\n')
         i = i + 1
   
   f.write(str(i)+' numero de commits totais \n')
