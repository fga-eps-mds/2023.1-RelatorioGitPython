# Documento de Visão

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-   | :-     | :-          | :-    |
| 26/04/2023 | 0.1 | Levantamento de Requisitos | Gabriel Rosa e Lucas Lobão |
| 17/05/2023 | 0.2 | Adição dos tópicos Introdução, Objetivo e Escopo| Gabriel Rosa |
| 17/05/2023 | 0.3 | Adição dos Requisitos Funcionais, Dados, Execução e Não Funcionais| Gabriel Rosa, Lucas Lobão e Catlen Cleane |
| 17/05/2023 | 0.4 | Repaginação do documento de visão | Gabriel Rosa |

## 1. Introdução

### 1.1 Objetivo
Este documento tem como objetivo passar uma visão geral dos requisitos do projeto, para que os integrantes possam conhecer como a aplicação será desenvolvida. Assim, serão listados as principais funcionalidades e seus requisitos, para se obter uma melhor compreensão do escopo.

### 1.2 Escopo
Este documento aplica-se ao projeto da biblioteca em python para gerar relatório de repositórios git. Esse projeto será desenvolvido pelos alunos da disciplina Métodos de Desenvolvimento de Software, ministrada pela professora Carla Rocha, da Universidade de Brasília - Campus Gama.

## 2. Requisitos do Produto

| **Tipo** | **Descrição** |
| :-       |        :-     |
| Alta     | Requisitos indispensáveis para o funcionamento da biblioteca |
| Média    | Requisitos importantes para a biblioteca, mas caso não sejam implementadas não resultará em mal funcionamento. |
| Baixa    | Requisitos embora possam trazer algum valor a bibliteca, não são essenciais para seu funcionamento básico ou para atender às necessidades principais dos usuários. |

## 2.1 Requisitos Funcionais

| Identificador | Requisito | Depende de | Prioridade |
| :-   | :-     | :-          | :-    |
| RF01 | Permitir que um desenvolvedor possa gerar relatórios estatíscos sobre um repositório Git | -- | Alta |
| RF02 | Permitir que um desenvolvedor possa gerar relatórios estatíscos de um usuário específico | -- | Alta |
| RF03 | Permitir que um usuário gere um relatório a partir de um intervalo de tempo (semana, mês ou ano) fornecido | -- | Alta |
| RF04 | Permitir que o usuário personalize o relatório de acordo com sua necessidade | -- | Alta |
| RF05 | Permitir que o usuário gere um relaório padrão (DEFAULT) já organizado | -- | Alta | 

## 2.2 Requisitos de Dados

| Identificador | Requisito | Depende de | Prioridade |
| :-   | :-     | :-          | :-    |
| RD01 | A biblioteca deve ser capaz de pegar os dados (Nome, Data, Email, Hash, Co-authors, Tipo de Arquivo) do repositório a partir do git log | -- | Alta |
| RD02 | A biblioteca deve ser capaz de organizar esses dados para gerar o relatório | -- | Alta |

## 2.3 Requisitos de Execução 
| Identificador | Requisito | Depende de | Prioridade |
| :-   | :-     | :-          | :-    |
| RE01 | O desenvolvedor deverá passar o caminho do repositório git | -- | Alta |
| RE02 | A biblioteca deverá listar de forma decrescente que mais contribuiu | -- | Alta |
| RE03 | A biblioteca deverá filtrar commits por tipo de arquivo | -- | Baixa |
| RE04 | A biblioteca deverá relacionar o usuário com o título do commit | -- | Alta |
| RE05 | A biblioteca deverá identificar os commits que tivem co-author | -- | Alta |
| RE06 | A biblioteca deverá listar a descrição de commit por pessoa | -- | Alta |

## 2.4 Requisitos Não Funcionais 
| Identificador | Requisito |
| :-   | :-     |
| RNF01 | A linguagem da biblioteca será em Python | 
| RNF02 | Os dados serão pegos no git log |
| RNF03 | A biblioteca tem como público alvo desenvolvedores (Scrum Master) com conhecimento em programação |
| RNF04 | A biblioteca deverá ser publica no PyPI |
| RNF05 | Oferecer suporte a diferentes sistemas de codificação de caracteres, como UTF-8 e ISO-8859-1 |
| RNF06 | Garantir que a biblioteca seja Unicode |