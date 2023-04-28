# Documento de Arquitetura

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-   | :-     | :-          | :-    |
| 25/04/2023 | 0.1 | Arquitetura a ser Avaliada | Gabriel Rosa |

## 1. Introdução

### 1.1 Objetivo
Este documento tem como objetivo passar uma visão geral do projeto que será implementado, para que os integrantes possam conhecer como a aplicação será subdivida e as funções de cada componente.

### 1.2 Escopo
Este documento aplica-se ao projeto da biblioteca em python para gerar relatório de repositórios git. Esse projeto será desenvolvido pelos alunos da disciplina Métodos de Desenvolvimento de Software, ministrada pela professora Carla Rocha, da Universidade de Brasília - Campus Gama.

## 2. Representação Arquitetural

### 2.1 Arquitetura em Camadas
A arquitetura ideal para este projeto poderia incluir a separação de camadas em módulos, com funções específicas para cada tarefa. Por exemplo, um módulo para coletar as informações do repositório, um módulo para gerar as estatísticas e um módulo para gerar o relatório. Uma possível abordagem é dividir a aplicação em três camadas: a camada de entrada, a camada de negócios e a camada de saída.

### 2.2.1 Camada de Entrada
A camada de entrada seria responsável por receber as informações de entrada da linha de comando e passá-las para a camada de negócios. Ela também poderia ser responsável por fazer a validação dos dados de entrada, garantindo que eles estejam corretos antes de passá-los para a camada de negócios.

### 2.2.2 Camada de Negócio
A camada de negócios seria responsável por processar as informações recebidas da camada de entrada e gerar as estatísticas necessárias. Essa camada seria composta por vários módulos, cada um com uma responsabilidade específica. Por exemplo, poderia haver um módulo para coletar as informações do repositório, outro módulo para gerar as estatísticas e outro módulo para consolidar essas informações em um relatório.

### 2.2.3 Camada de Saída
A camada de saída seria responsável por exibir o relatório gerado pela camada de negócios. Ela poderia ser responsável por formatar o relatório de acordo com as especificações do projeto e exibi-lo na tela ou salvá-lo em um arquivo.

### 2.2 Diagrama de Pacotes
O *diagrama de pacotes* pode ser usado para representar as camadas do sistema e como os pacotes (ou módulos) estão organizados em cada camada. Por exemplo, pode ser criado um pacote para cada camada, como a camada de acesso aos dados, a camada de lógica de negócios e a camada de interface com o usuário. Esse diagrama pode ajudar a visualizar a estrutura do sistema e como as diferentes camadas se relacionam entre si.

### 2.3 Diagrama de Sequência
O *diagrama de sequência* pode ser usado para representar as interações entre os componentes do sistema em uma determinada funcionalidade. Por exemplo, pode ser criado um diagrama de sequência para representar como o programa coleta as informações do repositório Git, como as estatísticas são geradas e como o relatório é criado. Esse diagrama pode ajudar a entender o fluxo de execução do sistema e como as diferentes camadas se comunicam entre si.

## 3. Metas e Restrições Arquiteturais

### 3.1 Suportabilidade
Este projeto poderá ser baixado através do comando pip do Python para a utilização da biblioteca.

### 3.2 Usuabilidade
A biblioteca deverá ser simples de ser utilizadas, com as funções bem definidas para cada atividade, de forma que não seja algo difícil de ser manipulado.

### 3.3 Ferramentas de Desenvolvimento 
O projeto será desenvolvimento em Python (versão 3.10), em conjunto com a biblioteca PyGit, além da ferramenta Poetry para fazer o deploy dessa biblioteca e utilizaremos o Git que a partir do git log será possível pegar as informações do repositório e do usuário.

### 3.4 Confiabilidade
A biblioteca terá uma cobertura de teste, buscando garantir que suas funcionalidades foram suficientemente testadas.
