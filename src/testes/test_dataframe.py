import pytest
from collections import defaultdict
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def commit_data(repo, date: str):
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
