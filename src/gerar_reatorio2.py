#from gitInfo import *
#from commit_palavra import *
from verificar_tipo_arquivo import *
from coauthor import relat_coauthor
from average_commit import *
import pandas as pd

def gerar_relatorio():

    content = '#Relatório Geral\n\n'

    #pegando arquivo texto/md de extenção de arquivo
    content += check_extension()
    #content += texto
    #print(content)

    content += '\n\n'

    content += '#Relatório de Commits com Coauthor\n\n'
    
    # Parte funcionando COAUTHOR ------------------------------------------
    
    coaut = relat_coauthor()
    #print(coaut)
    
    num_linhas = len(coaut.index)
    
    content += '| Hash | Author | Coauthor | Data |\n'
    content += '|------|--------|----------|------|\n'

    for indice, linha in coaut.iterrows():
        content += f'|{indice}'
        for coluna, valor in linha.iteritems():
            content += f'|{valor}'
            nada = {coluna}
        content += '|\n'

    #print(content)
    content += '\n\n'
    
    # Parte funcionando COAUTHOR ------------------------------------------

    # Parte Média ---------------------------------------------------------

    content += '#Commits por pessoa e Média Geral\n\n'

    commits = calculate_commit_average()
    
    num_linhas = len(commits.index)
    
    content += '| índice | Author | Commits | Avarege |\n'
    content += '|--------|--------|---------|---------|\n'

    for indice, linha in commits.iterrows():
        content += f'|{indice}'
        for coluna, valor in linha.iteritems():
            content += f'|{valor}'
            nada = {coluna}
        content += '|\n'


    content += '\n\n'
    print(content)

    output = 'relatorio.md'

    with open(output, 'w', encoding='utf-8') as f:
        f.write(content)
