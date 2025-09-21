def mochila_01(itens, capacidade):
    n = len(itens)
    # Cria uma tabela para armazenar os resultados dos subproblemas
    # tabela[i][w] guardará o valor máximo para os primeiros 'i' itens
    # com uma capacidade 'w'.
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Constrói a tabela de baixo para cima
    for i in range(1, n + 1):
        item_atual = itens[i - 1]
        peso_item = item_atual['peso']
        valor_item = item_atual['valor']
        for w in range(1, capacidade + 1):
            if peso_item <= w:
                # Decide se vale a pena incluir o item atual
                tabela[i][w] = max(
                    valor_item + tabela[i - 1][w - peso_item], # Inclui o item
                    tabela[i - 1][w]                           # Não inclui o item
                )
            else:
                # O item atual não cabe, então o valor é o mesmo da linha anterior
                tabela[i][w] = tabela[i - 1][w]

    # O valor máximo estará na última célula da tabela
    valor_maximo = tabela[n][capacidade]

    # Agora, vamos descobrir quais itens foram selecionados (backtracking)
    itens_selecionados = []
    w = capacidade
    for i in range(n, 0, -1):
        # Se o valor mudou da linha i-1 para i, significa que o item i foi incluído
        if tabela[i][w] != tabela[i - 1][w]:
            item_atual = itens[i - 1]
            itens_selecionados.append(item_atual['nome'])
            w -= item_atual['peso']

    itens_selecionados.reverse()
    return valor_maximo, itens_selecionados
