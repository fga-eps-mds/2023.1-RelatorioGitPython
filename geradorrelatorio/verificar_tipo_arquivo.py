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

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

'''

def check_extension():
    # Criando o dicionário para armazenar o autor e as extensões
    extension_by_author = defaultdict(lambda: defaultdict(list))

    for commit in repository.walk(repository.head.target, GIT_SORT_TIME):
        # Pegando nome do autor do commit
        name_author = commit.author.name

        # Obter a árvore do repositório
        tree = commit.tree

        # Percorrer todos os caminhos na árvore
        for entry in tree:
            # Obter o caminho do arquivo
            file_path = entry.name

            # Obter a extensão do arquivo
            file_extension = file_path.split('.')[-1]

            # Adicionar a extensão do arquivo em relação ao nome do autor
            extension_by_author[name_author][file_extension].append(file_path)

    content = '# Relatório de Extensões de Arquivos por Autor\n\n'

    for author, extensions in extension_by_author.items():
        content += f'## Author: {author} \n\n'
        content += '| Extensão | Arquivos | \n'
        content += '| -------- | -------- | \n'
        for extension, files in extensions.items():
            file_list = '|'.join(files)
            content += f'| {extension} | {file_list} | \n'
        content += "\n"

    output = 'arquivo.md'

    with open(output, 'w') as f:
        f.write(content)

    return output

output_file = check_extension()
print(f"A saída foi gravada no arquivo: {output_file}")

'''
