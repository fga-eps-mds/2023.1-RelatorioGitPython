from github import Github
import base64
import pandas as pd
import os
import re
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

g = Github(github_token)

repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")


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

    for author in commit_data.items():
            content += f'## Author: {author} \n\n'
            content += '| Author / Files |\n'
            content += '| -------- | \n'
    for message in commit_data.items():
            content += f'## Messages: {message} \n\n'
            content += '| Message / Files |\n'
            content += '| -------- | \n'
            content += "\n"

    output = 'arquivo.md'

    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)

    #return df

commit_data("06-05-2023")
