# Gerador de Relatório Git

## :pencil2: Descrição do Projeto

Trabalho referente a disciplina de Métodos de Desenvolvimento de Software, Ministrada pela prof. Carla Rocha, na Universidade de Brasília - FGA. 
Este projeto visa criar uma biblioteca Python para gerar relatórios automáticos sobre as participações dos desenvolvedores em um repositório/projeto. Como por exemplo, listar a quantidade de commits e issues por cara desenvolvedor.

## :dart: Objetivo

A biblioteca "pyGitInfo" tem o objetivo de fornecer funcionalidades para análise e extração de informações relacionadas a repositórios Git. Ela oferece uma variedade de funções que podem ser utilizadas para extrair dados sobre commits, coautores, problemas (issues), além de realizar análises estatísticas e geração de relatórios.

Alguns dos principais objetivos da biblioteca são:

- Facilitar a busca e análise de informações sobre commits realizados em um repositório Git, permitindo filtrar por usuário, período de tempo e palavras-chave nas descrições dos commits.

- Identificar commits que possuem coautores, ou seja, colaboradores que contribuíram para um commit específico.

- Gerar estatísticas sobre o número de commits por usuário e calcular a média de commits para avaliar o desempenho de cada colaborador em relação à média geral.

- Analisar problemas (issues) relacionados ao repositório, verificando quantos foram fechados em determinado período e gerando gráficos para visualização.

- Classificar os arquivos que estão sendo commitados pelos contribuidores de acordo com suas extensões, permitindo identificar quais tipos de arquivos são mais comumente modificados.

- Gerar relatórios completos que combinam várias análises, como commits com coautores, média geral de commits e informações sobre problemas, fornecendo uma visão abrangente do repositório Git.

Em resumo, a biblioteca tem como objetivo simplificar e automatizar a extração e análise de informações em repositórios Git, facilitando o entendimento e a avaliação do histórico de desenvolvimento de um projeto. 

## :computer: Tecnologias

![Python](https://img.shields.io/badge/-python-14354C?style=for-the-badge&logo=python&labelColor=0D1117)&nbsp;
![GIT](https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white)&nbsp;  
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)&nbsp;

## 🤝 Desenvolvedores do Projeto

<table>
  <tr>
    <td align="center" style="vertical-align:top"><a href="https://github.com/gabrielrosa09"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/gabrielrosa09" width="100px;" alt="foto"/><br /><sub><b>Gabriel<br>Rosa</b></sub></a><br /></td>
    <td align="center" style="vertical-align:top"><a href="https://github.com/GZaranza"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/GZaranza" width="100px;" alt="foto"/><br /><sub><b>Gabriel <br> Zaranza</b></sub></a><br /></td>
    <td align="center" style="vertical-align:top"><a href="https://github.com/lucaslobao-18"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/lucaslobao-18" width="100px;" alt="foto"/><br /><sub><b>Lucas <br> Andrade</b></sub></a><br /></td>
    <td align="center" style="vertical-align:top"><a href="https://github.com/catlenc"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/catlenc" width="100px;" alt="foto"/><br /><sub><b>Catlen <br> Cleane</b></sub></a><br /></td>
    <td align="center" style="vertical-align:top"><a href="https://github.com/rafa-kenji"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/rafa-kenji" width="100px;" alt="foto"/><br /><sub><b>Rafael <br> Kenji</b></sub></a><br /></td>
    <td align="center" style="vertical-align:top"><a href="https://github.com/ViniciussdeOliveira"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/ViniciussdeOliveira" width="100px;" alt="foto"/><br /><sub><b>Vinícius <br> de Oliveira</b></sub></a><br /></td>
    <td align="center" style="vertical-align:top"><a href="https://github.com/FelipeDireito"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/FelipeDireito" width="100px;" alt="foto"/><br /><sub><b>Felipe <br> Direito</b></sub></a><br /></td>
  </tr>
</table>

## :clipboard: Contribuição

Contribuições são sempre bem-vindas!

Veja o [guia de contribuição](/CONTRIBUTING.md) para saber como começar.

Por favor, siga o [código de conduta](docs/CODE_OF_CONDUCT.md) desse projeto.

## :books: Documentation  

### Overview

Imagine a scrum master, having to gather metrics about his team, he needs to check the number of commits per member, what is the general average of the team, which issues are still to be done, all this would take some time and scrum effort master.

The pyGitInfo library aims to facilitate all this analysis of repositories on github, bringing insights about each contributor and their respective participation in the repository. It has features for analyzing commits, files, issues, Pull Requests and much of what is used in a repository. 

### Installation and Configuration  

**Installing the library**  
To install the library, use the following command in your terminal

```python
pip install pyGitInfo
```

**Configuring the library**  
Create a file **.env** inside the "gitinfo" folder. In that file you need to add your GITHUB_TOKEN and your repository directory 'REPO'  

The file looks like this:  

```python

GITHUB_TOKEN = "ghp_ap0JAORWzs**********************" #your personal access token
REPO = "fga-eps-mds/2023.1-RelatorioGitPython" #Your project directory on Github

```  

### Library use

After downloading and configuring the library, we can start using it.  

First let's import the library into the project.  

```python
from pyGitInfo import *
```  

### Notes/Standardization  

**Date:** The default format for passing dates is "month-day-year" Ex: "06-07-2023" is equivalent to June 07, 2023  

### Functions and Returns  

- **get_commits_by_user()**  
  Allows you to search for commits by user, passing 3 strings as a parameter, the user's name (str), a start date and an end date.  

  ```python
  get_commits_by_user('name_user','date_init','date_end')
  ```  
  
  This function returns _DataFrame_ from the _Pandas_ library or an error message  

- **get_commits_users()**  
  Allows you to search for commits from all contributors, passing as a parameter 2 strings that define the time range, a start date and an end date.  

  ```python
  get_commits_users('date_init','date_end')
  ```  

  This function returns _DataFrame_ from the _Pandas_ library  

- **get_coAuthor()**  
  Search all commits with Coauthor, passing as parameters 2 strings that define the time range, a start date and an end date.  

  ```python
  get_coAuthor('date_init','date_end')
  ```  

  This function returns a _DataFrame_ from the _Pandas_ library or an error message  

- **issues_month()**  
  This function verifies how many Issues were closed per month, within the stipulated period. The function receives 2 date strings as a parameter, the start and end date.

  ```python
  issues_month('date_init','date_end')
  ```  

  The function returns _DataFrame_ from the _Pandas_ library and also generates a png graphic

- **calculate_commit_average()**  
  Calculates the average commits across all contributors and shows who is above or below that average. You must pass the analysis period as a parameter with 2 strings representing the dates

  ```python
  calculate_commit_average('date_init','date_end')
  ```  

  The function returns _DataFrame_ from the _Pandas_ library and also generates a png graphic

- **commit_data()**  
  Searches for all commits on a specific day, the function receives a string with the desired date as a parameter.

  ```python
  commit_data('date')
  ```  

  The function generates a markdown file with the information

- **commit_palavra()**  
  Searches for all commits (within a time range) that have the desired word in their description. This function receives 3 strings as a parameter, the first with the 'word' to be searched for, and the 2 'dates' referring to the time interval

  ```python
  commit_palavra('palavra','date_init','date_end')
  ```  

  The function returns a _DataFrame_ from the _Pandas_ library or an error message  

- **check_extension()**  
  It does a search for the files that are being committed by each contributor and classifies them according to their extension. You must pass the time interval for the analysis (2 strings of 'date')

  ```python
  check_extension('date_init','date_end')
  ```  

  The function returns a variable with the content written in markdown format

- **title_commits()**  
  Searches all commit titles, by user, thus facilitating the visualization of what each contributor has done (Requires a time interval) 2 strings 'data'

  ```python
  title_commits('date_init','date_end')
  ```  

  The function returns a variable with the content written in markdown format  

- **gerenate_report()**  
  Combines the functions of commit with coauthor and overall average to generate a more complete report. The function receives as parameter 2 date strings with the time interval to be analyzed ('initial_date','final_date')

  ```python
  gerenate_report('date_init','date_end')
  ```  

  Generates a "gitInfo_report.md" markdown with information about commits with coauthor and the number of commits per user

- **issues_open()**  
  Searches all Issues that are open but have not yet been signed by anyone. It takes nothing as a parameter.

  ```python
  issues_open()
  ```  

  The function returns a variable with the content written in markdown format

## :mag_right: Licença  

  Este projeto está sob [licença](/LICENSE). Acesse para mais informações.
