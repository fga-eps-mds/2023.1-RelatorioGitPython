#from gitInfo import *
#from commit_palavra import *
from verificar_tipo_arquivo import *
from coauthor import relat_coauthor
from average_commit import *
import pandas as pd

def gerar_relatorio():

    #content = '#Relatório Geral\n\n'

    #pegando arquivo texto/md de extenção de arquivo --------
    #content += check_extension()
    #content += texto
    #print(content)

    #content += '\n\n'
    #content += '#Relatório de Commits com Coauthor\n\n'
    
    coaut = relat_coauthor()
    print(coaut)

    
    #content += '| Hash / Author / Coauthor / Data |\n'

    num_linhas = len(coaut.index)
    print(num_linhas)
'''
    for  in coaut:
        content += f'| {author} / {coaut} / {date} / {hash} |\n'
        content += '| -------- | \n'

    print(content)'''  
    #media_commits = calculate_commit_average()
    #print(media_commits)
