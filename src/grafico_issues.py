from github import Github
import base64
import pandas as pd
import re
import matplotlib
import datetime
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

g=Github(github_token)

repo = g.get_repo("fga-eps-mds/2023.1-RelatorioGitPython")

def issues_month(star_date: str, end_date: str):
    
    months_list = pd.period_range(start =star_date,end=end_date, freq='M')
    months_list = [month.strftime("%b-%Y") for month in months_list]

    issues = repo.get_issues(state='closed')
    
    count=[]


    for month in months_list:
        contador=0
        for issue in issues:
            if issue.pull_request is None and issue.closed_at.strftime("%b-%Y") == month:
                contador+=1
        count.append(contador)

    df = pd.DataFrame({"num_issues": count},index=months_list)    



    # print(df)
    plt.bar(months_list, df['num_issues'])
    plt.xlabel('Months')
    plt.ylabel('Issues')
    plt.title('Issues per month')
    plt.yticks(range(0,max(df['num_issues']+1)))
    plt.xticks(rotation=45)
    plt.show()