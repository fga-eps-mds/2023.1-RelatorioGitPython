# Documento de Visão

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-   | :-     | :-          | :-    |
| 26/04/2023 | 0.1 | Levantamento de Requisitos | Gabriel Rosa e Lucas Lobão |
| 17/05/2023 | 0.2 | Adição dos tópicos Introdução, Objetivo e Escopo| Gabriel Rosa |
| 17/05/2023 | 0.3 | Adição dos Requisitos Funcionais, Dados, Execução e Não Funcionais| Gabriel Rosa, Lucas Lobão e Catlen Cleane |

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


### 1.4 Qual é a plataforma alvo (desktop, web, mobile)?
A plataforma alvo será o terminal, pois o projeto é por via terminal.

### 1.5 Quais são os principais concorrentes do projeto?
Os concorrentes serão as outras bibliotecas que já fazem algo parecido, como por exemplo, o GitPython, PyDriller, GitStats, GitInsights e Pygit2.

### 1.6 Quais são os recursos disponíveis para o projeto (tempo, orçamento, equipe, etc.)?
O projeto terá uma duração de um total de 12 sprints. A primeira sprint teve inicio no dia 28 de março de 2023, de maneira que a última sprint será iniciada no dia 25 de julho de 2023, totalizando 4 meses de duração de projeto. Durante esse período, haverão duas datas de entregas importantes, sendo elas denominadas releases.

### 1.7 Quais são os principais requisitos de desempenho e segurança?
- **Verificação de entrada**
Todas as entradas fornecidas pelos usuários devem ser verificadas e validadas antes de serem processadas pela biblioteca.

- **Limitação de privilégios**
A biblioteca Python deve ser projetada para limitar os privilégios dos usuários e minimizar o risco de escalada de privilégios.

- **Gerenciamento seguro de dados confidenciais**
Se a biblioteca precisar armazenar ou processar dados confidenciais, como senhas ou informações de cartão de crédito, ela deve implementar medidas de segurança fortes para garantir a integridade e confidencialidade desses dados.

- **Proteção contra vulnerabilidades conhecidas**
A biblioteca Python deve ser mantida atualizada e protegida contra vulnerabilidades conhecidas, como falhas de segurança de bibliotecas ou bibliotecas desatualizadas.

- **Testes de segurança**
A biblioteca Python deve ser submetida a testes rigorosos de segurança para garantir que ela seja resistente a ataques conhecidos e que funcionem como esperado em condições adversas.

### 1.8 Quais são as principais tecnologias a serem utilizadas no projeto?
O projeto será desenvolvimento em Python (versão 3.10), além da ferramenta Poetry para fazer o deploy dessa biblioteca e utilizaremos o Git que a partir do git log será possível pegar as informações do repositório e do usuário.

### 1.9 Quais são os principais requisitos de acessibilidade e internacionalização?
- Utilizar nomes de variáveis, funções e módulos claros e descritivos para facilitar a compreensão do código.
- Incluir comentários adequados e informações contextuais para facilitar a leitura e o entendimento do código.
- Certificar-se de que a biblioteca seja compatível com diferentes idiomas e caracteres Unicode.
- Disponibilizar documentação em diferentes idiomas, se possível.
- Oferecer suporte a diferentes sistemas de codificação de caracteres, como UTF-8 e ISO-8859-1, para garantir a compatibilidade com diferentes sistemas operacionais e plataformas.

### 1.10 Quais são os principais fluxos de uso do sistema?
- Instalar o Python 3.10.
- Criar um ambiente virtual.
- Escolher um nome para a biblioteca.
- Escrever o código da biblioteca.
- Escrever testes.
- Fazer o deploy da biblioteca.
- Manter a biblioteca.

### 1.11 Quais são as principais telas e funcionalidades que precisam ser implementadas?
Uma biblioteca em Python não possui uma interface gráfica padrão, portanto, não há "telas" específicas para serem implementadas. No entanto podemos listar algumas funcionalidades:

- Arquivos de código-fonte.
- Documentação.
- Testes.
- Configuração de pacote.
- Publicação da biblioteca.
- Atualização da biblioteca.

### 1.12 Quais são os principais cenários de teste?
- Testes unitários
- Testes de integração
- Testes de aceitação
- Testes de segurança
- Testes de compatibilidade
- Testes de usabilidade
- Testes de cobertura

### 1.13 Quais são as principais restrições e requisitos legais?
Reunião com Léo.

### 1.14 Quais são os principais riscos e mitigadores do projeto?
**Riscos**
- Falta de clareza sobre os requisitos da biblioteca.
- Má gestão do projeto.
- Falta de testes suficientes.
- Falha em garantir a compatibilidade com outras bibliotecas.
- Falta de segurança.
- Falta de documentação adequada. 
- Problemas de desempenho.
### 1.15 Quais são as principais métricas de sucesso do projeto?
- Conclusão no prazo.
- Satisfação do cliente.
- Performance. 
- Usabilidade.
- Compatibilidade