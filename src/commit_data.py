from github import Github
import os
from datetime import datetime
from dotenv import load_dotenv
import io
from datetime import datetime

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

    # Criar o arquivo Markdown
    with io.open("commit_data.md", "w", encoding="utf-8") as file:
        file.write("# Commits do dia {}\n\n".format(date))

        if not hashes:
            file.write("Não houve commits no dia.\n")
        else:
            for i in range(len(hashes)):
                file.write("## Commit {}\n\n".format(i+1))
                file.write("- Hash: {}\n".format(hashes[i]))
                file.write("- Autor: {}\n".format(authors[i]))
                file.write("- Mensagem: {}\n\n".format(messages[i]))

commit_data('06-29-2023')