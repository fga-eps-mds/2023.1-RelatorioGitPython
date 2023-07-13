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