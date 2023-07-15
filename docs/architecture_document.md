# Documento de Arquitetura

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-   | :-     | :-          | :-    |
| 25/04/2023 | 0.1 | Arquitetura a ser Avaliada | Gabriel Rosa |
| 07/05/2023 | 0.2 | Descrição das tecnologias | Gabriel Zaranza |
| 08/05/2023 | 0.3 | Adiação do diagrama de pacotes da R1| Gabriel Zaranza |
| 17/05/2023 | 0.4 | Adição da descrição de Orientação a Objetos | Gabriel Rosa |
| 05/07/2023 | 0.5 | Adicionando novas tecnologias e atualizando representação arquitetural | Gabriel Rosa |

## 1. Introdução

### 1.1 Objetivo
Este documento tem como objetivo passar uma visão geral do projeto que será implementado, para que os integrantes possam conhecer como a aplicação será subdivida e as funções de cada componente.

### 1.2 Escopo
Este documento aplica-se ao projeto da biblioteca em python para gerar relatório de repositórios git. Esse projeto será desenvolvido pelos alunos da disciplina Métodos de Desenvolvimento de Software, ministrada pela professora Carla Rocha, da Universidade de Brasília - Campus Gama.
## 2. Tecnologias

### Python
Python é uma linguagem de programação de alto nível, interpretada e orientada a objetos. Ela é projetada para ser fácil de ler, escrever e manter, o que a torna uma escolha popular para desenvolvimento de software em uma ampla variedade de áreas, desde aplicações desktop até inteligência artificial e análise de dados. Python possui uma sintaxe simples e clara, com uma grande quantidade de bibliotecas e módulos disponíveis, permitindo que desenvolvedores possam resolver problemas complexos de forma rápida e eficiente.

### PyGithub
A biblioteca PyGithub é uma ferramenta em Python que fornece uma interface de programação de aplicativos (API) para interagir com a plataforma GitHub. Ela simplifica a interação com a API do GitHub, permitindo que os desenvolvedores acessem, modifiquem e gerenciem repositórios, problemas, pull requests, releases, branches e colaboradores. Com a PyGithub, os desenvolvedores podem automatizar tarefas comuns do GitHub, como criar repositórios, adicionar colaboradores, listar problemas e abrir pull requests. A biblioteca possui uma sintaxe intuitiva, é bem documentada e oferece uma ampla gama de recursos para atender às necessidades específicas dos desenvolvedores. Em suma, a PyGithub é uma biblioteca poderosa em Python que facilita a integração com o GitHub, permitindo que os desenvolvedores aproveitem os recursos da plataforma e automatizem tarefas de gerenciamento de repositórios.

### Git
Git é um sistema de controle de versão distribuído de código aberto, desenvolvido inicialmente por Linus Torvalds em 2005. Ele permite que um ou mais desenvolvedores trabalhem em um mesmo código, rastreando as alterações feitas em cada versão e ajudando a coordenar e mesclar as mudanças de diferentes colaboradores. Com o Git, é possível criar e manter repositórios de código-fonte em que várias pessoas podem contribuir e compartilhar seu trabalho. O Git permite que diferentes branches (ramos) sejam criados para experimentar diferentes ideias e funcionalidades, sem afetar a versão principal do projeto. Também é possível criar tags (rótulos) para marcar pontos importantes na história do projeto, como releases ou versões estáveis.

### OS
A biblioteca OS (Operating System) é uma biblioteca padrão do Python que fornece uma interface de programação para interagir com o sistema operacional em que o Python está sendo executado. Com a biblioteca OS, é possível realizar operações como acessar o sistema de arquivos, manipular caminhos de arquivos, executar comandos do sistema e outras funcionalidades relacionadas ao sistema operacional.

### Pandas
A biblioteca pandas é uma biblioteca Python de código aberto destinada à análise e manipulação de dados. Ela oferece estruturas de dados eficientes para armazenar e manipular dados em tabelas, além de diversas funções para processamento de dados e operações de manipulação de tabelas.

### Matlibplot
Matplotlib é uma biblioteca popular em Python para visualização de dados. Com uma sintaxe simples e flexível, ela permite criar gráficos de linhas, barras, dispersão, histogramas e muito mais. Além disso, Matplotlib oferece controle detalhado sobre aspectos visuais, como cores, estilos e rótulos. Com suporte a diversos formatos de arquivo, é possível salvar os gráficos em diferentes extensões. Com essas funcionalidades, Matplotlib é uma escolha versátil para a criação de visualizações de dados claras e informativas em projetos de análise e ciência de dados.

## 3. Representação Arquitetural

### 3.1 Arquitetura em Camadas
A arquitetura ideal para este projeto poderia incluir a separação de camadas em módulos, com funções específicas para cada tarefa. Por exemplo, um módulo para coletar as informações do repositório, um módulo para gerar as estatísticas e um módulo para gerar o relatório. Uma possível abordagem é dividir a aplicação em três camadas: a camada de entrada, a camada de negócios e a camada de saída.

### 3.2.1 Camada de Entrada
Ela é responsável por fazer a validação dos dados de entrada, garantindo que eles estejam corretos antes de passá-los para a camada de negócios.

### 3.2.2 Camada de Negócio
A camada de negócios seria responsável por processar as informações recebidas da camada de entrada e gerar as estatísticas necessárias. Essa camada seria composta por vários módulos, cada um com uma responsabilidade específica. Por exemplo, poderia haver um módulo para coletar as informações do repositório, outro módulo para gerar as estatísticas e outro módulo para consolidar essas informações em um relatório.

### 3.2.3 Camada de Saída
A camada de saída seria responsável por exibir o relatório gerado pela camada de negócios. Ela poderia ser responsável por formatar o relatório de acordo com as especificações do projeto e exibi-lo na tela ou salvá-lo em um arquivo.

### 3.2 Orientação a Objetos 
Para o desenvolvimento da biblioteca, será utilizado o paradigma de Orientação a Objetos, os objetos são as principais unidades de estrutura e interação. Cada objeto é uma instância de uma classe, que define suas propriedades (atributos) e comportamentos (métodos). Os atributos representam as características do objeto, enquanto os métodos são as ações que ele pode executar. 


## 4. Metas e Restrições Arquiteturais

### 4.1 Suportabilidade
Este projeto poderá ser baixado através do comando pip do Python para a utilização da biblioteca.

### 4.2 Usuabilidade
A biblioteca deverá ser simples de ser utilizadas, com as funções bem definidas para cada atividade, de forma que não seja algo difícil de ser manipulado.

### 4.3 Ferramentas de Desenvolvimento 
O projeto será desenvolvimento em Python (versão 3.10), em conjunto com a biblioteca PyGitHub pegandos todas informações que são capazes de retirar da API.

### 4.4 Confiabilidade
A biblioteca terá uma cobertura de teste de 95%, buscando garantir que suas funcionalidades foram suficientemente testadas.
