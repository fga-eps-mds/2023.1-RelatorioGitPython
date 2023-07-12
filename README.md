# Gerador de Relatório Git

## :pencil2: Descrição do Projeto

Trabalho referente a disciplina de Métodos de Desenvolvimento de Software, Ministrada pela prof. Carla Rocha, na Universidade de Brasília - FGA. 
Este projeto visa criar uma biblioteca Python para gerar relatórios automáticos sobre as participações dos desenvolvedores em um repositório/projeto. Como por exemplo, listar a quantidade de commits e issues por cara desenvolvedor.

## :dart: Objetivo

Elaborar uma ferramenta offline, que, por linha de comando, a partir do _git log_ de um repositório, gere relatório (txt) com estatísticas de um ususário específico ou da esquipe inteira.  

## :computer: Tecnologias

![Python](https://img.shields.io/badge/-python-14354C?style=for-the-badge&logo=python&labelColor=0D1117)&nbsp;
![GIT](https://img.shields.io/badge/Git-E34F26?style=for-the-badge&logo=git&logoColor=white)&nbsp;  

## :hammer: Usabilidade

Antes de tudo, você precisará ter o [Python](https://www.python.org/downloads/) previamente instalado.

Após clonar o repositótio em sua máquina, siga os passos a seguir.

### Passo 1

Crie um arquivo **.env** e insira a informação a seguir:

``` bash
GITHUB_TOKEN = <seu_token>
```

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

## :books: Documentação  

### Visão Geral

Imagine um scrum master, tendo que levantar métricas sobre a sua equipe, ele precisa verificar o número de commits por integrantes, qual é a média geral da equipe, quais as issues ainda estão por fazer, tudo isso levaria algum tempo e um esforço do scrum master.  

A biblioteca Gitpython tem por objetivo facilitar toda essa análise de repositórios no github, trazendo insights sobre cada contribuinte e sua respectiva participação no repositório. Ela dispõem de funcionalidades para análise de commits, arquivos, issues, Pull Requests e boa parte do que é utilizado em um repositório.  

### Instalação e Configuração  

**Configurando a biblioteca**  
Crie um arquivo **.env** dentro da pasta "gitinfo". Nesse arquivo você precisa adicionar o seu GITHUB_TOKEN e o diretório do seu repositório 'REPO'  

O Arquivo fica assim:  

```python

GITGUB_TOKEN = "ghp_ap0JAORWzs**********************" #your personal access token
REPO = "fga-eps-mds/2023.1-RelatorioGitPython" #Your project directory on Github

```  

### Uso da biblioteca

Após baixar e configurar a biblioteca podemos começar a usar.  

Primeiro vamos importar a biblioteca para o projeto.

```python
from gitInfo import *
```  

### Observações/Padronização  

**Data:** O formato padrão para passar datas é "mês-dia-ano" Ex: "06-07-2023" equivale ao dia 07 de junho de 2023  

### Funções e Retornos  

- **get_commits_by_user()**  
  Permite que você busque os commits por usuário, passando como parâmetro 3 strings, o nome do usuário (str), uma data inicial e uma data final.  

  ```python
  get_commits_by_user('name_user','date_init','date_end')
  ```  
  
  essa função retorna _DataFrame_ da biblioteca _Pandas_ ou uma mensagem de erro  

- **get_commits_users()**  
  Permite que você busque os commits de todos os contribuintes, passando como parâmetro 2 strings que definem o range temporal, uma data inicial e uma data final.  

  ```python
  get_commits_users('date_init','date_end')
  ```  

  essa função retorna _DataFrame_ da biblioteca _Pandas_  

- **get_coAuthor()**  
  Busque todos os commits com Coauthor, passando como parâmetro 2 strings que definem o range temporal, uma data inicial e uma data final.  

  ```python
  get_coAuthor('date_init','date_end')
  ```  

  Essa função retorna um _DataFrame_ da biblioteca _Pandas_ ou uma mensagem de erro  

- **issues_month()**  
  Essa função veifica quantas Issues foram fechadas por mês, dentro do período estipulado. A função recebe como parâmetro 2 strings de data, a data inicial e a final.

  ```python
  issues_month('date_init','date_end')
  ```  

  A função retorna _DataFrame_ da biblioteca _Pandas_ e também gera um gráfico png

- **calculate_commit_average()**  
  Calcula a média de commits entre todos os contribuintes e mostra quem está acima ou abaixo dessa média. Deve passar como parâmetro o período de análise com 2 strings representando as datas

  ```python
  calculate_commit_average('date_init','date_end')
  ```  

  A função retorna _DataFrame_ da biblioteca _Pandas_ e também gera um gráfico png

- **commit_data()**  
  Busca todos os commits em um dia expecífico, a função recebe como parâmetro uma string com a data desejada.

  ```python
  commit_data('date')
  ```  

  A função gera um arquivo markdown com as informações

- **commit_palavra()**  
  Busca todos os commits (dentro de um intervalo de tempo) que têm a palavra desejada em sua descrição. Essa função recebe como parâmetro 3 strings, a primeira com a 'palavra' que será buscada, e as 2 'datas' referente ao intervalo de tempo

  ```python
  commit_palavra('palavra','date_init','date_end')
  ```  

  A função retorna um _DataFrame_ da biblioteca _Pandas_ ou uma mensagem de erro  

- **check_extension()**  
  Faz uma busca pelos arquivos que estão sendo commitados por cada contribuinte e classifíca-os de acordo com a sua extenção. Deve-se passar o intervalo de tempo para a análise (2 strings de 'data')

  ```python
  check_extension('date_init','date_end')
  ```  

  A função retorna uma variável com o conteúdo escrito em formato markdown

- **title_commits()**  
  Busca todos os titulos de commits, por usuário, facilitando assim a vizualização do que cada contribuinte tem feito (Necessita de um intervalo temporal) 2 strings 'data'

  ```python
  title_commits('date_init','date_end')
  ```  

  A função retorna uma variável com o conteúdo escrito em formato markdown  

- **gerenate_report()**  
  Combina as funções de commit com coauthor e média geral para gerar um relatório mais completo. A função recebe como parâmetro 2 strings de data com o intervalo de tempo que será analisado ('data_inicial',' data_final')

  ```python
  gerenate_report('date_init','date_end')
  ```  

  Gera um markdown "gitInfo_report.md" com as informações de commits com coauthor e da quantidade de commits por usuário

- **issues_open()**  
  Busca todas as Issues que estão abertas mas ainda não foram assinadas por ninguém. Não recebe nada como parâmetro.

  ```python
  issues_open()
  ```  

  A função retorna uma variável com o conteúdo escrito em formato markdown

### Atualização e Suporte

## :mag_right: Licença  

  Este projeto está sob [licença](/LICENSE). Acesse para mais informações.
