## REQUISITOS FUNCIONAIS

Uma biblioteca em python que gere relatórios estatíticos sobre commits executados em um repositório Git

A biblioteca vai gerar relatórios, a partir de um usuário específico ou de uma equipe inteira

A biblioteca deve ser capaz de gerar relatórios com base em diferentes intervalos de tempo na semana, no mês ou em um intervalo de tempo personalizado.

A biblioteca deve ser capaz de gerar relatórios com base em diferentes intervalos de tempo na semana, no mês ou em um intervalo de tempo personalizado.

A biblioteca deve ser fácil de usar e permitir que os usuários personalizem os relatórios gerados de acordo com suas necessidades.

## REQUISITOS DE DADOS


O relatorio produzido deve informar para cada repositório ou de cada usuário no diretório Git, o número de commits, nome, data, e-mail e mensagem do commit. 

Os relatórios devem der gerados em diferentes formatos, como arquivos de texto.


## REQUISITOS DE EXECUÇÃO
O usuário vai fornecer como entrada o repositório que ele deseja obter as informações.

A biblioteca vai gerar um relatório, em txt, contendo:
- O  número total de Commits 
- A data do último commit, o autor e o comentário
- O número total de commits de cada autor do repositório


## REQUISITOS NÃO FUNCIONAIS

A linguagem do programa será python.

O software desenvolvido será uma biblioteca em python.

Os dados serão pegos pelo git log.

Esse software será acessado po qualquer pessoa, mas ele será desenvolido tendo como publuco alvo pessoas com conhecimento em programação.
