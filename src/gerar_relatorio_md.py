def gerar_relatorio_markdown(dados):
    relatorio = "# Relatório\n\n"  # Inicializa a variável "relatorio" com o cabeçalho do relatório

    for secao, conteudo in dados.items():  # Itera sobre os itens do dicionário "dados"
        relatorio += "## " + secao + "\n\n"  # Adiciona o cabeçalho da seção ao relatório

        if isinstance(conteudo, dict):  # Verifica se o conteúdo da seção é um dicionário

            for item, valor in conteudo.items():  # Itera sobre os itens do dicionário de conteúdo
                
                # Adiciona cada item ao relatório como uma lista
                relatorio += "- **{}**: {}\n".format(item, valor)  
            
            relatorio += "\n"  # Adiciona uma quebra de linha após cada seção do dicionário
        
        else:
            relatorio += conteudo + "\n\n"  # Adiciona o conteúdo diretamente ao relatório

    return relatorio  # Retorna o relatório formatado em Markdown

def gerar_relatorio_markdown(saida_funcao):
    relatorio = "# Relatório\n\n"  # Inicializa a variável "relatorio" com o cabeçalho do relatório

    relatorio += "## Conteúdo da outra função:\n\n"  # Adiciona um cabeçalho de seção ao relatório
    relatorio += saida_funcao + "\n\n"  # Adiciona a saída da outra função ao relatório como conteúdo

    # Outras seções e conteúdos do relatório podem ser adicionados aqui

    return relatorio  # Retorna o relatório formatado em Markdown

def outra_funcao():
    # Lógica da outra função para gerar a saída
    return "Este é o resultado da outra função."

saida = outra_funcao()  # Chama a função "outra_funcao" e armazena a saída em "saida"
relatorio_markdown = gerar_relatorio_markdown(saida)  # Gera o relatório Markdown usando a saída da função
print(relatorio_markdown)  # Imprime o relatório Markdown
