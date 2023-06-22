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
    
    coaut = relat_coauthor()
    #print(coaut)
    
    num_linhas = len(coaut.index)
    
    content += '| Hash / Author / Coauthor / Data |\n'

    for i in num_linhas:
        content += f'|{coaut.at[i, 0]} / {coaut.at[i, 1]} / {coaut.at[i, 2]} / {coaut.at[i][3]} |\n'
        content += '| -------- |\n'
   
    content += '/n/n'
    #print(content) 

    content += '#Relatório de Commits com Coauthor\n\n'
        
    commit = calculate_commit_average()
           
    content += '| Author / Commit/ Average |\n'
        
    num_linhas = len(commit.index)
        
    for i in num_linhas:
        content += f'|{commit.at[i, 0]} / {commit.at[i, 1]} / {commit.at[i, 2]}|\n'
        content += '| -------- |\n'
    
    content += '/n'
    
    #print(content)

    output = 'relatorio.md'

    with open(output, 'w', encoding='utf-8') as f:
       f.write(content)
