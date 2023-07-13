import pytest
from datetime import datetime
from unittest.mock import MagicMock
from github import Github
import os

# from github import Github
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv

from src.grafico_issues import issues_month


load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

g = Github(github_token)

repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")




@pytest.fixture(scope="module")
def setup_repo():
    # Set up any necessary resources for testing the repository
    # For example, you can create test issues in the repository
    # and close them with specific closed_at dates.
    # Ensure to clean up after the tests are complete.
    # Return the repo object if needed in the tests.
    yield repo

    # Clean up any resources used for testing


@pytest.fixture(scope="module")
def setup_dates():
    # Set up any necessary date parameters for testing the function
    # Return a tuple of start_date and end_date as strings
    start_date = "2022-01-01"
    end_date = "2022-12-31"
    yield start_date, end_date

def test_issues_month(setup_repo, setup_dates):
    repo = setup_repo
    start_date, end_date = setup_dates

    result = issues_month(start_date, end_date)
    plt.close('all')

    # Perform assertions to validate the result
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0
    assert len(result.columns) == 1
    assert all(col in result.columns for col in ['num_issues'])
    assert all(isinstance(val, int) for val in result['num_issues'])
    assert all(idx.startswith(start_date[:4]) for idx in result.index)
