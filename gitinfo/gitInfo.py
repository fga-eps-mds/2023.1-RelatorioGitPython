from collections import defaultdict
import pandas as pd
import os
import io
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
from github import Github

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

g=Github(github_token)

repo = os.getenv('REPO')

repo = g.get_repo(repo)


def get_commits_by_user(user: str, start_date: str, end_date: str):
    hashes = []
    messages = []

    commits = repo.get_commits()
    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            if commit.author.login.lower() == user.lower():
                messages.append(commit.commit.message)
                hashes.append(commit.sha[:6])

    df = pd.DataFrame({"Message":messages}, index=hashes)

    if df.empty is False:
        return df
    else:
        msg_error = "No commits with this user"
        return msg_error

def get_commits_users(start_date: str, end_date: str):

    commit_users = []
    commits = repo.get_commits()
    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            author = commit.author.login
            if author in commit_users:
             continue

            commit_users.append(author)

    df = pd.DataFrame({"Users": commit_users})
    return df

def get_coAuthor(start_date: str, end_date: str):
    coauthors = []
    hashes = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            commit_message = commit.commit.message

            if 'Co-authored-by:' in commit_message:
                hashes.append(commit.commit.sha[:6])
                authors.append(commit.commit.author.name)

                lines = commit_message.splitlines()
                aux=[]
                for row in lines:
                    if row.startswith('Co-authored-by:'):
                        aux.append(row[16:].strip().split('<')[0])
                coauthors.append(aux)

    df = pd.DataFrame({"authors": authors,"co-authors":coauthors}, index=hashes)

    if df.empty is False:
        return df
    else:
        msg = "0 commits with Coauthors"
        return msg


def issues_month(start_date: str, end_date: str):

    months_list = pd.period_range(start =start_date,end=end_date, freq='M')
    months_list = [month.strftime("%b-%Y") for month in months_list]

    issues = repo.get_issues(state='closed')

    count=[]


    for month in months_list:
        counter=0
        for issue in issues:
            if issue.pull_request is None and issue.closed_at.strftime("%b-%Y") == month:
                counter+=1
        count.append(counter)

    df = pd.DataFrame({"num_issues": count},index=months_list)

    plt.bar(months_list, df['num_issues'])
    plt.xlabel('Months')
    plt.ylabel('Issues')
    plt.title('Issues per month')
    plt.yticks(range(0,max(df['num_issues']+1)))
    plt.xticks(rotation=13)
    plt.savefig('closed_issues.png', format='png')

    return df

def calculate_commit_average(start_date: str, end_date: str):

    commits = repo.get_commits()

    commits_count = defaultdict(int)

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            author = commit.author
            name = author.login if author else "Unknown"

            commits_count[name] += 1


    total_commits = sum(commits_count.values())
    count_user = len(commits_count)

    average_total = total_commits / count_user

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
    plt.xticks(rotation=13)
    plt.savefig('commit_average.png', format='png')

    return df

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
        file.write("# Commits from day {}\n\n".format(date))

        if not hashes:
            file.write("There were no commits that day.\n")
        else:
            for i in range(len(hashes)):
                file.write("## Commit {}\n\n".format(i+1))
                file.write("- Hash: {}\n".format(hashes[i]))
                file.write("- Author: {}\n".format(authors[i]))
                file.write("- Message: {}\n\n".format(messages[i]))


def commit_palavra(string: str, start_date: str, end_date: str):

    hashes = []
    messages = []
    authors = []

    commits = repo.get_commits()

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:

            commit_message = commit.commit.message

            if string.lower() in commit_message.lower():

                hashes.append(commit.sha[:6])
                authors.append(commit.commit.author.name)
                messages.append(commit.commit.message)

    df = pd.DataFrame({"message":messages, "author": authors}, index=hashes)

    if df.empty is False:
        return df
    else:
        msg = "No commits with this word"
        return msg

def check_extension(start_date: str, end_date: str):
    try:
        extension_by_author = defaultdict(lambda: defaultdict(list))

        commits = repo.get_commits()

        for commit in commits:
            commit_date = commit.commit.author.date
            commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
            if commit_date_str >= start_date and commit_date_str <= end_date:
                author = commit.author.login
                file_modify = commit.files

                for file in file_modify:
                    extension = file.filename.split('.')[-1]
                    filename = file.filename

                    extension_by_author[author][extension].append(filename)

        content = '## File Extensions Report by Author\n\n'

        for author, extensions in extension_by_author.items():
            content += f'## Author: {author} \n\n'
            content += '| Extension / Files |\n'
            content += '| -------- | \n'
            for extension, files in extensions.items():
                file_list = '| \n'.join(files)
                content += f'| **{extension}** | \n'
                content += f' {file_list} | \n'
            content += "\n"

    except Exception as e:
        print(f'Error: {e}')

    return content

def title_commits(start_date: str, end_date: str):

    commits = repo.get_commits()

    commit_titles = defaultdict(lambda: defaultdict(list))

    for commit in commits:
        commit_date = commit.commit.author.date
        commit_date_str = datetime.strftime(commit_date, "%m-%d-%Y")
        if commit_date_str >= start_date and commit_date_str <= end_date:
            author = commit.author
            if author:
                author_name = author.login
            else:
                author_name = 'Unknown'

            commit_title = commit.commit.message.splitlines()[0]

            if author_name in commit_titles:
                commit_titles[author_name].append(commit_title)
            else:
                commit_titles[author_name] = [commit_title]

    content = '#File Title Commits\n\n'
    for author, titles in commit_titles.items():
        content += f'## User: {author}\n'
        content += f'### Commit title:\n'
        for title in titles:
            content += f'- {title}\n'
        content += '\n'

    return content


def generate_report(start_date: str, end_date: str):
    content = '## Report from ' + start_date + ' - ' + end_date + '\n\n'

    content += check_extension(start_date, end_date)
    content += '\n\n'

    content += '## List of commits with coauthor\n\n'

    coaut = get_coAuthor(start_date, end_date)

    content += '| Hash | Author | Coauthor |\n'
    content += '|------|--------|----------|\n'

    for index, row in coaut.iterrows():
        content += f'|{index}'
        for columm, value in row.items():
            content += f'|{value}'
            nothing = {columm}
        content += '|\n'

    content += '\n\n'

    content += '## Commits per person and general avarage\n\n'
    commits = calculate_commit_average(start_date, end_date)
    graph_path = 'commit_average.png'

    content += '| Index | Author | Commits | Averege |\n'
    content += '|-------|--------|---------|---------|\n'

    for index, row in commits.iterrows():
        content += f'|{index}'
        for columm, value in row.items():
            content += f'|{value}'
            nothing = {columm}
        content += '|\n'

    content += '\n\n'

    content += f'![Commit Average Graph]({graph_path})\n\n'
    output = 'gitInfo_report.md'

    with open(output, 'w', encoding='utf-8') as f:

        f.write(content)


def issues_open():
    issues = repo.get_issues(state='open')

    content = '## Issues opened assigned\n'

    content += '| Title | Number |\n'
    content += '|-------|--------|\n'

    for issue in issues:
        if issue.assignee:
            content += f'|{issue.title}|{issue.number}|\n'

    content += '\n\n'
    content += '## Issues opened not assigned\n'

    content += '| Title | Number |\n'
    content += '|-------|--------|\n'

    for issue in issues:
        if not issue.assignee:
            content += f'|{issue.title}|{issue.number}|\n'

    return content