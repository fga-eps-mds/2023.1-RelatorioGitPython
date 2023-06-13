from github import Github
import base64
import pandas as pd
import re
import matplotlib
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

g=Github(github_token)

repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")

def issues_month(star_date: str, end_date: str):
    
    months_list = pd.period_range(start =star_date,end=end_date, freq='M')
    months_list = [month.strftime("%b-%Y") for month in months_list]

    issues = repo.get_issues(state='closed')
    
    issues_list =[]
    
    count=[]


    for month in months_list:
        contador=0
        for issue in issues:
            if issue.pull_request is None and issue.closed_at.strftime("%b-%Y") == month:
                contador+=1
        count.append(contador)

    df = pd.DataFrame({"num issues": count},index=months_list)    



    print(df)
   

issues_month('2022-05-05','2023-12-06')