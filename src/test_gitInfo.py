import unittest
from unittest.mock import MagicMock
from collections import defaultdict
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
from github import Github
import gitInfo


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

        expected_messages = ['Commit 1', 'Commit 2', 'Commit 3']
        expected_hashes = ['hash1', 'hash2', 'hash3']

        result = gitInfo.get_commits_by_user(usuario, start_date, end_date)

        self.assertEqual(result['Message'].tolist(), expected_messages)
        self.assertEqual(result.index.tolist(), expected_hashes)

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

        expected_users = ['user1', 'user2']
        expected_result = pd.DataFrame({"Users": expected_users})

        result = gitInfo.get_commits_users(start_date, end_date)

        self.assertTrue(result.equals(expected_result))

    def test_get_coAuthor(self):
        start_date = '06-28-2023'
        end_date = '06-29-2023'

        commit1 = MagicMock()
        commit1.commit.author.date = datetime(2023, 6, 28)
        commit1.commit.message = 'Commit 1'

        commit2 = MagicMock()
        commit2.commit.author.date = datetime(2023, 6, 29)
        commit2.commit.message = 'Commit 2'

        commit3 = MagicMock()
        commit3.commit.author.date = datetime(2023, 6, 29)
        commit3.commit.message = 'Commit 3'

        commit4 = MagicMock()
        commit4.commit.author.date = datetime(2023, 6, 30)
        commit4.commit.message = 'Commit 4'

        self.repo.get_commits.return_value = [commit1, commit2, commit3, commit4]

        expected_authors = ['author1', 'author2']
        expected_coauthors = [['co-author1'], ['co-author2']]
        expected_hashes = ['hash1', 'hash2']

        expected_result = pd.DataFrame({"authors": expected_authors, "co-authors": expected_coauthors}, index=expected_hashes)

        result = gitInfo.get_coAuthor(start_date, end_date)

        self.assertTrue(result.equals(expected_result))
        
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

        expected_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        expected_months = ['Jan-2023', 'Feb-2023', 'Mar-2023', 'Apr-2023', 'May-2023', 'Jun-2023', 'Jul-2023', 'Aug-2023', 'Sep-2023', 'Oct-2023', 'Nov-2023', 'Dec-2023']

        gitInfo.issues_month(start_date, end_date)

        self.assertEqual(plt.xticks()[0].tolist(), expected_months)
        self.assertEqual(plt.yticks()[0].tolist(), expected_counts)

    def test_calculate_commit_average(self):
        start_date = '2023-01-01'
        end_date = '2023-12-31'

        commit1 = MagicMock(author=MagicMock(login='author1'))
        commit2 = MagicMock(author=MagicMock(login='author2'))
        commit3 = MagicMock(author=None)

        self.repo.get_commits.return_value = [commit1, commit2, commit3]

        expected_authors = ['author1', 'author2']
        expected_commits = [1, 1]
        expected_average = 1.0

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

        expected_hashes = ['hash1', 'hash2', 'hash3']
        expected_messages = ['Commit 1', 'Commit 2', 'Commit 3']

        gitInfo.commit_data(date)

        # Assert content of 'arquivo_data.md' file

        with open('arquivo_data.md', 'r') as f:
            content = f.read()

        expected_content = '#File Commit by date\n\n'
        expected_content += '## Author: author1 \n\n'
        expected_content += '| -------- | \n'
        expected_content += '## Messages: Commit 1 \n\n'
        expected_content += '| -------- | \n\n'
        expected_content += '\n'
        expected_content += '## Author: author2 \n\n'
        expected_content += '| -------- | \n'
        expected_content += '## Messages: Commit 2 \n\n'
        expected_content += '| -------- | \n\n'
        expected_content += '\n'
        expected_content += '## Author: author1 \n\n'
        expected_content += '| -------- | \n'
        expected_content += '## Messages: Commit 3 \n\n'
        expected_content += '| -------- | \n\n'
        expected_content += '\n'

        self.assertEqual(content, expected_content)

    def test_commit_palavra(self):
        start_date = '06-01-2023'
        end_date = '06-30-2023'
        string = 'bug'

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

        expected_hashes = ['hash1', 'hash2']
        expected_messages = ['Fixing bug 1', 'Bug fix']

        result = gitInfo.commit_palavra(string, start_date, end_date)

        self.assertEqual(result['message'].tolist(), expected_messages)
        self.assertEqual(result['author'].tolist(), ['author1', 'author2'])

    def test_check_extension(self):
        start_date = '06-01-2023'
        end_date = '06-30-2023'

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

        expected_content = '## File Extensions Report by Author\n\n'
        expected_content += '## Author: author1 \n\n'
        expected_content += '| Extension / Files |\n'
        expected_content += '| -------- | \n'
        expected_content += '| **py** | \n'
        expected_content += '| file1.py | \n'
        expected_content += '| file2.py | \n'
        expected_content += '\n'
        expected_content += '## Author: author2 \n\n'
        expected_content += '| Extension / Files |\n'
        expected_content += '| -------- | \n'
        expected_content += '| **java** | \n'
        expected_content += '| file3.java | \n'
        expected_content += '| **py** | \n'
        expected_content += '| file4.py | \n'
        expected_content += '\n'

        result = gitInfo.check_extension(start_date, end_date)

        self.assertEqual(result, expected_content)


if __name__ == '__main__':
    unittest.main()