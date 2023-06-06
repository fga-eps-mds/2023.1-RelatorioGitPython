from github import Github
import base64
import pandas as pd
import os
import re
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

g=Github(github_token)

repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")


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