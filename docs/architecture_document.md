# Documento de Arquitetura

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-   | :-     | :-          | :-    |
| 25/04/2023 | 0.1 | Arquitetura a ser Avaliada | Gabriel Rosa |
| 07/05/2023 | 0.2 | Descrição das tecnologias | Gabriel Zaranza |

## 1. Introdução

### 1.1 Objetivo
Este documento tem como objetivo passar uma visão geral do projeto que será implementado, para que os integrantes possam conhecer como a aplicação será subdivida e as funções de cada componente.

### 1.2 Escopo
Este documento aplica-se ao projeto da biblioteca em python para gerar relatório de repositórios git. Esse projeto será desenvolvido pelos alunos da disciplina Métodos de Desenvolvimento de Software, ministrada pela professora Carla Rocha, da Universidade de Brasília - Campus Gama.
## 2. Tecnologias

### Python
Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos. Ela é projetada para ser fácil de ler, escrever e manter, o que a torna uma escolha popular para desenvolvimento de software em uma ampla variedade de áreas, desde aplicações desktop até inteligência artificial e análise de dados. Python possui uma sintaxe simples e clara, com uma grande quantidade de bibliotecas e módulos disponíveis, permitindo que desenvolvedores possam resolver problemas complexos de forma rápida e eficiente.

### Git
Git é um sistema de controle de versão distribuído de código aberto, desenvolvido inicialmente por Linus Torvalds em 2005. Ele permite que um ou mais desenvolvedores trabalhem em um mesmo código, rastreando as alterações feitas em cada versão e ajudando a coordenar e mesclar as mudanças de diferentes colaboradores. Com o Git, é possível criar e manter repositórios de código-fonte em que várias pessoas podem contribuir e compartilhar seu trabalho. O Git permite que diferentes branches (ramos) sejam criados para experimentar diferentes ideias e funcionalidades, sem afetar a versão principal do projeto. Também é possível criar tags (rótulos) para marcar pontos importantes na história do projeto, como releases ou versões estáveis.

### Pygit2
O Pygit2 é uma biblioteca Python que fornece uma interface de programação para interagir com o sistema de controle de versão Git. Com o Pygit2, é possível ler, escrever e manipular repositórios Git diretamente do Python. Entre as principais funcionalidades do Pygit2, estão: criação e clonagem de repositórios Git, adição e remoção de arquivos e diretórios em um repositório Git, commits de alterações em arquivos, criação e fusão de branchesc acesso ao histórico de commits e suas informações, como autor, data e mensagem.

### OS
A biblioteca OS (Operating System) é uma biblioteca padrão do Python que fornece uma interface de programação para interagir com o sistema operacional em que o Python está sendo executado. Com a biblioteca OS, é possível realizar operações como acessar o sistema de arquivos, manipular caminhos de arquivos, executar comandos do sistema e outras funcionalidades relacionadas ao sistema operacional.

### Pandas
A biblioteca pandas é uma biblioteca Python de código aberto destinada à análise e manipulação de dados. Ela oferece estruturas de dados eficientes para armazenar e manipular dados em tabelas, além de diversas funções para processamento de dados e operações de manipulação de tabelas.

## 3. Representação Arquitetural

### 3.1 Arquitetura em Camadas
A arquitetura ideal para este projeto poderia incluir a separação de camadas em módulos, com funções específicas para cada tarefa. Por exemplo, um módulo para coletar as informações do repositório, um módulo para gerar as estatísticas e um módulo para gerar o relatório. Uma possível abordagem é dividir a aplicação em três camadas: a camada de entrada, a camada de negócios e a camada de saída.

### 3.2.1 Camada de Entrada
A camada de entrada seria responsável por receber as informações de entrada da linha de comando e passá-las para a camada de negócios. Ela também poderia ser responsável por fazer a validação dos dados de entrada, garantindo que eles estejam corretos antes de passá-los para a camada de negócios.

### 3.2.2 Camada de Negócio
A camada de negócios seria responsável por processar as informações recebidas da camada de entrada e gerar as estatísticas necessárias. Essa camada seria composta por vários módulos, cada um com uma responsabilidade específica. Por exemplo, poderia haver um módulo para coletar as informações do repositório, outro módulo para gerar as estatísticas e outro módulo para consolidar essas informações em um relatório.

### 3.2.3 Camada de Saída
A camada de saída seria responsável por exibir o relatório gerado pela camada de negócios. Ela poderia ser responsável por formatar o relatório de acordo com as especificações do projeto e exibi-lo na tela ou salvá-lo em um arquivo.

### 3.2 Diagrama de Pacotes
O *diagrama de pacotes* pode ser usado para representar as camadas do sistema e como os pacotes (ou módulos) estão organizados em cada camada. Por exemplo, pode ser criado um pacote para cada camada, como a camada de acesso aos dados, a camada de lógica de negócios e a camada de interface com o usuário. Esse diagrama pode ajudar a visualizar a estrutura do sistema e como as diferentes camadas se relacionam entre si.

### 3.3 Diagrama de Sequência
O *diagrama de sequência* pode ser usado para representar as interações entre os componentes do sistema em uma determinada funcionalidade. Por exemplo, pode ser criado um diagrama de sequência para representar como o programa coleta as informações do repositório Git, como as estatísticas são geradas e como o relatório é criado. Esse diagrama pode ajudar a entender o fluxo de execução do sistema e como as diferentes camadas se comunicam entre si.

## 4. Metas e Restrições Arquiteturais

### 4.1 Suportabilidade
Este projeto poderá ser baixado através do comando pip do Python para a utilização da biblioteca.

### 4.2 Usuabilidade
A biblioteca deverá ser simples de ser utilizadas, com as funções bem definidas para cada atividade, de forma que não seja algo difícil de ser manipulado.

### 4.3 Ferramentas de Desenvolvimento 
O projeto será desenvolvimento em Python (versão 3.10), em conjunto com a biblioteca PyGit, além da ferramenta Poetry para fazer o deploy dessa biblioteca e utilizaremos o Git que a partir do git log será possível pegar as informações do repositório e do usuário.

### 4.4 Confiabilidade
A biblioteca terá uma cobertura de teste, buscando garantir que suas funcionalidades foram suficientemente testadas.
