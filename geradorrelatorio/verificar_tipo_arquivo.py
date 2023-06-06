import os
from collections import defaultdict
from github import Github
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token do GitHub do arquivo .env
github_token = os.getenv('GITHUB_TOKEN')

github = Github(github_token)

owner = 'fga-eps-mds'
repository = '2023.1-RelatorioGitPython'

def check_extension():
    try:
        repo = github.get_repo(f'{owner}/{repository}')
        
        extension_by_author = defaultdict(lambda: defaultdict(list))
        
        commits = repo.get_commits()

        for commit in commits:
            author = commit.author.login
            file_modify = commit.files

            for file in file_modify:
                extension = file.filename.split('.')[-1]
                filename = file.filename

                extension_by_author[author][extension].append(filename)
        
        content = '#File Extensions Report by Author\n\n'

        for author, extensions in extension_by_author.items():
            content += f'## Author: {author} \n\n'
            content += '| Extension / Files |\n'
            content += '| -------- | \n'
            for extension, files in extensions.items():
                file_list = '| \n'.join(files)
                content += f'| **{extension}** | \n'
                content += f' {file_list} | \n'
            content += "\n"

        output = 'arquivo.md'

        with open(output, 'w', encoding='utf-8') as f:
            f.write(content)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
