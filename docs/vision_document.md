# Documento de Visão

## Histórico de Revisão

| Data | Versão | Modificação | Autor |
| :-   | :-     | :-          | :-    |
| 26/04/2023 | 0.1 | Levantamento de Requisitos | Gabriel Rosa e Lucas Lobão |
| 17/05/2023 | 0.2 | Adição dos tópicos Introdução, Objetivo e Escopo| Gabriel Rosa |

## 1. Introdução

### 1.1 Objetivo
Este documento tem como objetivo passar uma visão geral dos requisitos do projeto, para que os integrantes possam conhecer como a aplicação será desenvolvida. Assim, serão listados as principais funcionalidades e seus requisitos, para se obter uma melhor compreensão do escopo.

### 1.2 Escopo
Este documento aplica-se ao projeto da biblioteca em python para gerar relatório de repositórios git. Esse projeto será desenvolvido pelos alunos da disciplina Métodos de Desenvolvimento de Software, ministrada pela professora Carla Rocha, da Universidade de Brasília - Campus Gama.

## 1. Levantamento de Requisitos

### 1.1 Qual é o objetivo principal do projeto?
Este projeto tem como objetivo o desenvolvimento de uma biblioteca em python que auxilia na análise de repositório git. Uma ferramenta offline, que, por linha de comando, a partir do git log de um repositório, gere relatório (txt) com estatiticas de acordo com a necessidade de um usuário.

### 1.2 Quais são as funcionalidades principais do projeto?
- Pegar informações do git log, como o nome, email, issues, commits e entre outras informações.
- Tratar as informações coletadas.
- Gerar um relatório a partir das informações coletadas.
- Publicar a biblioteca no PyPI (Python Package Index).

### 1.3 Qual é o público-alvo do projeto?
- **Desenvolvedores**
Um desenvolvedor pode usar a biblioteca para gerar relatórios sobre o código-fonte de um repositório Github e identificar áreas problemáticas ou oportunidades de melhorias.

- **Gerentes de projetos**
um gerente de projeto pode usar a biblioteca para monitorar o progresso do desenvolvimento de um projeto hospedado no Github.

- **Analistas de dados**
um analista de dados pode usar a biblioteca para coletar dados de vários repositórios Github e gerar relatórios que ajudem a entender tendências ou padrões de desenvolvimento.

- **Empresas**
uma empresa que usa o Github para hospedar seu código pode usar a biblioteca para monitorar o desempenho de seus desenvolvedores e identificar áreas problemáticas que precisam de melhorias.

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