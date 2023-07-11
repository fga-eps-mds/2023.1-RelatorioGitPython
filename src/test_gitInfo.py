import unittest
from unittest.mock import MagicMock
import pandas as pd
from pandas.testing import assert_frame_equal
from pandas.core.frame import DataFrame
import re
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
from github import Github
import gitInfo
import difflib
import numpy as np
from numpy.testing import assert_array_equal
import os
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')
repo_link = os.getenv('REPO')

g = Github(github_token)
repo = g.get_repo(repo_link)


class TestGitFunctions(unittest.TestCase):

    def setUp(self):
        self.repo = MagicMock()

    def test_get_commits_by_user(self):
        usuario = 'rafa-kenji'
        start_date = '05-01-2023'
        end_date = '06-30-2023'

        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 5, 15)
        commit1.author.login.lower.return_value = 'rafa-kenji'
        commit1.commit.message = 'Commit 1'

        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 10)
        commit2.author.login.lower.return_value = 'rafa-kenji'
        commit2.commit.message = 'Commit 2'

        commit3 = MagicMock()
        commit3.commit.author.date = datetime(2023, 6, 20)
        commit3.author.login.lower.return_value = 'rafa-kenji'
        commit3.commit.message = 'Commit 3'

        commit4 = MagicMock()
        commit4.commit.author.date = datetime(2023, 7, 5)
        commit4.author.login.lower.return_value = 'john-doe'
        commit4.commit.message = 'Commit 4'

        self.repo.get_commits.return_value = [commit1, commit2, commit3, commit4]

        expected_messages = [
            'Merge pull request #58 from fga-eps-mds/refatoracao_biblioteca\n\nRefatoracao biblioteca',
            'Correção da saída markdown\n\nCo-authored-by: Catlen Oliveira <99406424+catlenc@users.noreply.github.com>',
            'Merge pull request #52 from fga-eps-mds/pipeline-1\n\nPipeline 1',
            'Relacionar os commit por data\n\nCo-authored-by: Catlen Oliveira <99406424+catlenc@users.noreply.github.com>'
        ]

        expected_hashes = ['f8e353', 'fe0389', 'd49ca6', 'bdc947']

        result = gitInfo.get_commits_by_user(usuario, start_date, end_date)

        self.assertSequenceEqual(result['Message'].tolist(), expected_messages, "\n\n".join(list(difflib.unified_diff(expected_messages, result['Message'].tolist()))))
        self.assertEqual(result.index.tolist(), expected_hashes)

    def test_not_get_commits_by_user(self):
        user = 'john_doe'
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        # Simulação de commits
        commit1 = MagicMock()
        commit1.commit.author.date = '2023-01-05'
        commit1.author.login = 'john_doe'
        commit1.sha = 'abc123'
        commit1.commit.message = 'Commit 1'

        commit2 = MagicMock()
        commit2.commit.author.date = '2023-01-10'
        commit2.author.login = 'jane_smith'
        commit2.sha = 'def456'
        commit2.commit.message = 'Commit 2'

        repo = MagicMock()
        repo.get_commits.return_value = [commit1, commit2]

        # Chama a função
        result = gitInfo.get_commits_by_user(user, start_date, end_date)

        # Verifica o resultado
        expected_result = "No commits with this user"
        self.assertEqual(result, expected_result)

    def test_get_commits_users(self):
        start_date = '06-29-2023'
        end_date = '06-30-2023'

        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 6, 29)
        commit1.author.login = 'user1'

        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 30)
        commit2.author.login = 'user2'

        commit3 = MagicMock()
        commit3.commit.author.date = datetime(2023, 7, 1)
        commit3.author.login = 'user1'

        commit4 = MagicMock()
        commit4.commit.author.date = datetime(2023, 7, 2)
        commit4.author.login = 'user3'

        self.repo.get_commits.return_value = [commit1, commit2, commit3, commit4]

        expected_users = ['GZaranza', 'lucaslobao-18', 'ViniciussdeOliveira', 'catlenc', 'FelipeDireito']
        expected_result = pd.DataFrame({"Users": expected_users})

        result = gitInfo.get_commits_users(start_date, end_date)

        assert_frame_equal(result, expected_result, check_like=True)

    def test_get_coAuthor(self):
        start_date = '06-30-2023'
        end_date = '07-01-2023'

        commits = [
            MagicMock(commit=MagicMock(author=MagicMock(date=datetime(2023, 6, 30)), message='Commit message 1')),
            MagicMock(commit=MagicMock(author=MagicMock(date=datetime(2023, 7, 1)), message='Commit message 2'))
        ]

        repo = MagicMock()
        repo.get_commits.return_value = commits

        result = gitInfo.get_coAuthor(start_date, end_date)

        expected_authors = ['author1', 'author2']
        expected_coauthors = ['coauthor1', 'coauthor2']
        expected_hashes = ['hash1', 'hash2']
        expected_result = pd.DataFrame({"Hash": expected_hashes, "Author": expected_authors, "Coauthor": expected_coauthors})

        assert_frame_equal(result, expected_result, check_like=True)

    def test_issues_month(self):
        start_date = '2023-01-01'
        end_date = '2023-12-31'

        issues = [
            MagicMock(closed_at=datetime(2023, 1, 5)),
            MagicMock(closed_at=datetime(2023, 2, 10)),
            MagicMock(closed_at=datetime(2023, 3, 15)),
            MagicMock(closed_at=datetime(2023, 4, 20)),
            MagicMock(closed_at=datetime(2023, 5, 25)),
            MagicMock(closed_at=datetime(2023, 6, 30)),
            MagicMock(closed_at=datetime(2023, 7, 5)),
            MagicMock(closed_at=datetime(2023, 8, 10)),
            MagicMock(closed_at=datetime(2023, 9, 15)),
            MagicMock(closed_at=datetime(2023, 10, 20)),
            MagicMock(closed_at=datetime(2023, 11, 25)),
            MagicMock(closed_at=datetime(2023, 12, 31)),
        ]

        self.repo.get_issues.return_value = issues

        expected_counts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        expected_months = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

        gitInfo.issues_month(start_date, end_date)

        x_ticks = [str(tick) for tick in plt.xticks()[0]]
        assert_array_equal(np.array(x_ticks), np.array(expected_months))

        y_ticks = plt.yticks()[0]
        assert_array_equal(y_ticks, np.array(expected_counts))
        
    def test_calculate_commit_average(self):
        start_date = '06-29-2023'
        end_date = '06-30-2023'
    
        commit1 = MagicMock(author=MagicMock(login='author1'))
        commit2 = MagicMock(author=MagicMock(login='author2'))
        commit3 = MagicMock(author=MagicMock(login='author3'))
        commit4 = MagicMock(author=MagicMock(login='author4'))
        commit5 = MagicMock(author=MagicMock(login='author5'))
        commit6 = MagicMock(author=MagicMock(login='author6'))
        commit7 = MagicMock(author=MagicMock(login='author7'))
        commit8 = MagicMock(author=MagicMock(login='author8'))
    
        self.repo.get_commits.return_value = [commit1, commit2, commit3, commit4, commit5, commit6, commit7, commit8]
    
        expected_authors = ['ViniciussdeOliveira', 'GZaranza', 'lucaslobao-18', 'catlenc', 'FelipeDireito']
    
        expected_commits = [5, 3, 2, 1, 1]
        expected_average = 2.4
    
        result = gitInfo.calculate_commit_average(start_date, end_date)
    
        self.assertEqual(result['Author'].tolist(), expected_authors)
        self.assertEqual(result['Commits'].tolist(), expected_commits)
        self.assertEqual(result['Average'].tolist(), [expected_average] * len(expected_authors))

    def test_commit_data(self):
        date = '06-15-2023'
    
        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 6, 15)
        commit1.commit.author.name = 'author1'
        commit1.sha = 'hash1'
        commit1.commit.message = 'Commit 1'
    
        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 20)
        commit2.commit.author.name = 'author2'
        commit2.sha = 'hash2'
        commit2.commit.message = 'Commit 2'
    
        commit3 = MagicMock()
        commit3.commit.author.date = datetime(2023, 6, 25)
        commit3.commit.author.name = 'author1'
        commit3.sha = 'hash3'
        commit3.commit.message = 'Commit 3'
    
        commit4 = MagicMock()
        commit4.commit.author.date = datetime(2023, 7, 1)
        commit4.commit.author.name = 'author3'
        commit4.sha = 'hash4'
        commit4.commit.message = 'Commit 4'
    
        self.repo.get_commits.return_value = [commit1, commit2, commit3, commit4]
    
        gitInfo.commit_data(date)
    
        # Assert content of 'arquivo_data.md' file
    
        with open('arquivo_data.md', 'r') as f:
            content = f.read()
    
        expected_content = '# File Commit by date\n\n'
        expected_content += '## Author: FelipeDireito \n\n'
        expected_content += '| -------- | \n'
        expected_content += '## Messages: Merge pull request #54 from fga-eps-mds/grafico_issues\n\n'
        expected_content += 'Grafico issues top \n\n'
        expected_content += '| -------- | \n'
    
        self.assertEqual(content.strip(), expected_content.strip())
    
    def test_commit_palavra(self):
        start_date = '06-28-2023'
        end_date = '06-29-2023'
        string = 'issues'
    
        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 6, 10)
        commit1.commit.author.name = 'author1'
        commit1.sha = 'hash1'
        commit1.commit.message = 'Fixing bug 1'
    
        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 15)
        commit2.commit.author.name = 'author2'
        commit2.sha = 'hash2'
        commit2.commit.message = 'Bug fix'
    
        commit3 = MagicMock()
        commit3.commit.author.date = datetime(2023, 6, 20)
        commit3.commit.author.name = 'author1'
        commit3.sha = 'hash3'
        commit3.commit.message = 'Feature update'
    
        self.repo.get_commits.return_value = [commit1, commit2, commit3]
    
        expected_messages = ['Finaliza a funcao das issues com saida em markdown', 'Cria as listas com issues assinadas e nao assinadas', 'Cria funcao que busca as issues']
        expected_authors = ['lucaslobao-18', 'catlenc', 'lucaslobao-18']
        expected_indexes = ['718b52', 'f7bcfd', '6f0926']
    
        result = gitInfo.commit_palavra(string, start_date, end_date)
    
        result['message'] = result['message'].apply(lambda x: re.split('\n\n|\n', x, maxsplit=1)[0])
        result_messages = result['message'].tolist()
    
        diff = difflib.ndiff(expected_messages, result_messages)
        diff_str = '\n'.join(diff)
    
        self.assertEqual(expected_messages, result_messages, f"\nDiff:\n{diff_str}")
        self.assertEqual(result['author'].tolist(), expected_authors)
        self.assertEqual(result.index.tolist(), expected_indexes)
        
    def test_not_commit_palavra_no_match(self):
        string = 'abecedario'
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        # Simulação de commits
        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 1, 5)
        commit1.commit.message = 'Fixing issue'

        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 1, 10)
        commit2.commit.message = 'Refactoring code'

        repo = MagicMock()
        repo.get_commits.return_value = [commit1, commit2]

        # Chama a função
        result = gitInfo.commit_palavra(string, start_date, end_date)

        # Verifica o resultado
        expected_result = "No commits with this word"
        self.assertEqual(result, expected_result)
    
    def test_check_extension(self):
        start_date = '06-28-2023'
        end_date = '06-29-2023'
    
        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 6, 10)
        commit1.author.login = 'author1'
        commit1.files = [MagicMock(filename='file1.py'), MagicMock(filename='file2.py')]
    
        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 15)
        commit2.author.login = 'author2'
        commit2.files = [MagicMock(filename='file3.java'), MagicMock(filename='file4.py')]
    
        commit3 = MagicMock()
        commit3.commit.author.date = datetime(2023, 6, 20)
        commit3.author.login = 'author1'
        commit3.files = [MagicMock(filename='file5.py'), MagicMock(filename='file6.js')]
    
        self.repo.get_commits.return_value = [commit1, commit2, commit3]
    
        expected_content = '''## File Extensions Report by Author

## Author: GZaranza 

| Extension / Files |
| -------- | 
| **py** | 
 src/gitInfo.py| 
src/main.py| 
src/gitInfo.py | 
| **md** | 
 arquivo.md | 
| **python** | 
 tempCodeRunnerFile.python | 

## Author: lucaslobao-18 

| Extension / Files |
| -------- | 
| **py** | 
 src/gitInfo.py| 
src/main.py| 
src/gitInfo.py| 
src/main.py | 

## Author: ViniciussdeOliveira 

| Extension / Files |
| -------- | 
| **py** | 
 src/gitInfo.py| 
src/gitInfo.py| 
src/gitInfo.py| 
src/gitInfo.py| 
src/gitInfo.py | 

## Author: catlenc 

| Extension / Files |
| -------- | 
| **py** | 
 src/gitInfo.py | 

## Author: FelipeDireito 

| Extension / Files |
| -------- | 
| **py** | 
 src/gitInfo.py | 

'''
    
        result = gitInfo.check_extension(start_date, end_date)
    
        self.maxDiff = None
        self.assertMultiLineEqual(result, expected_content)
        
    def test_title_commits(self):
        start_date = '06-28-2023'
        end_date = '06-29-2023'
    
        # Mock commits
        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 6, 28)
        commit1.author.login = 'author1'
        commit1.commit.message = 'Commit message 1'
    
        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 29)
        commit2.author.login = 'author2'
        commit2.commit.message = 'Commit message 2'
    
        commits = [commit1, commit2]
    
        # Mock repository
        repo = MagicMock()
        repo.get_commits.return_value = commits
    
        # Call the function and get the result
        result = gitInfo.title_commits(start_date, end_date)
    
        # Define the expected content
        expected_content = '''#File Title Commits

## User: GZaranza
### Commit title:
- Merge pull request #69 from fga-eps-mds/issue_65
- Merge branch 'main' into issue_65

## User: lucaslobao-18
### Commit title:
- Finaliza a funcao das issues com saida em markdown
- Cria funcao que busca as issues

## User: ViniciussdeOliveira
### Commit title:
- Refatorando e adicionando filtro data na função get_commits_users()
- Adicionando o filtro data na função get_coAuthor()
- Adicionando filtro data na função check_extension()
- Adicionando filtro de data na função calculate_commit_average()
- Merge pull request #68 from fga-eps-mds/grafico_no_markdown

## User: catlenc
### Commit title:
- Cria as listas com issues assinadas e nao assinadas

## User: FelipeDireito
### Commit title:
- Adiciona plot do grafico no markdown gerado

'''

        # Compare the result with the expected content
        self.maxDiff = None
        self.assertEqual(result, expected_content)
    
    def test_issues_open(self):
        # Mock get_issues result
        issue1 = MagicMock()
        issue1.title = 'Ajuste final gitINfo'
        issue1.number = 71
        issue1.assignee = MagicMock()
    
        issue2 = MagicMock()
        issue2.title = 'Configuração para empacotamento da biblioteca'
        issue2.number = 66
        issue2.assignee = MagicMock()
    
        issue3 = MagicMock()
        issue3.title = 'Atualizar as estórias de usuário'
        issue3.number = 64
        issue3.assignee = MagicMock()
    
        issue4 = MagicMock()
        issue4.title = 'Desenvolver testes unitários'
        issue4.number = 56
        issue4.assignee = MagicMock()
    
        issue5 = MagicMock()
        issue5.title = 'Criar a documentação da biblioteca'
        issue5.number = 50
        issue5.assignee = MagicMock()
    
        issue6 = MagicMock()
        issue6.title = 'Ajuste final'
        issue6.number = 72
        issue6.assignee = None
    
        issues = [issue1, issue2, issue3, issue4, issue5, issue6]
    
        # Mock repository
        repo = MagicMock()
        repo.get_issues.return_value = issues
    
        # Call the function
        result = gitInfo.issues_open()
    
        # Construir o conteúdo esperado usando issues
        expected_content = '## Issues opened assigned\n'
        expected_content += '| Title | Number |\n'
        expected_content += '|-------|--------|\n'
        for issue in issues:
            if issue.assignee:
                expected_content += f'|{issue.title}|{issue.number}|\n'
    
        expected_content += '\n\n'
        expected_content += '## Issues opened not assigned\n'
        expected_content += '| Title | Number |\n'
        expected_content += '|-------|--------|\n'
        for issue in issues:
            if not issue.assignee:
                expected_content += f'|{issue.title}|{issue.number}|\n'
    
        # Compare the result with the expected content
        self.maxDiff = None
        self.assertMultiLineEqual(result, expected_content)
    
    def test_generate_report(self):
        start_date = '06-28-2023'
        end_date = '06-29-2023'
    
        # Mock check_extension function
        mock_check_extension = MagicMock(return_value='Mocked extension report')
        gitInfo.check_extension = mock_check_extension
    
        # Mock get_coAuthor function
        mock_get_coAuthor = MagicMock(return_value=pd.DataFrame({
            'Hash': ['hash1', 'hash2'],
            'Author': ['author1', 'author2'],
            'Coauthor': ['coauthor1', 'coauthor2']
        }))
        gitInfo.get_coAuthor = mock_get_coAuthor
    
        # Mock calculate_commit_average function
        mock_calculate_commit_average = MagicMock(return_value=pd.DataFrame({
            'Index': ['index1', 'index2'],
            'Author': ['author1', 'author2'],
            'Commits': [5, 10],
            'Averege': [7.5, 7.5]
        }))
        gitInfo.calculate_commit_average = mock_calculate_commit_average
    
        # Call the function and generate the report
        gitInfo.generate_report(start_date, end_date)
    
        # Read the generated report file
        with open('gitInfo_report.md', 'r', encoding='utf-8') as f:
            result = f.read()
    
        # Define the expected content
        expected_content = '''## Report from 06-28-2023 - 06-29-2023

Mocked extension report

## List of commits with coauthor

| Hash | Author | Coauthor |
|------|--------|----------|
|0|hash1|author1|coauthor1|
|1|hash2|author2|coauthor2|


## Commits per person and general avarage

| Index | Author | Commits | Averege |
|-------|--------|---------|---------|
|0|index1|author1|5|7.5|
|1|index2|author2|10|7.5|


![Commit Average Graph](commit_average.png)

'''

        # Compare the result with the expected content
        self.assertEqual(result, expected_content)
    
        # Cleanup: delete the generated report file
        os.remove('gitInfo_report.md')


if __name__ == '__main__':
    unittest.main()

