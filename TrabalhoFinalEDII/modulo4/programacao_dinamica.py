def mochila_01(itens, capacidade):
    n = len(itens)
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_atual = itens[i - 1]
        peso_item = item_atual['peso']
        valor_item = item_atual['valor']
        for w in range(1, capacidade + 1):
            if peso_item <= w:
                tabela[i][w] = max(
                    valor_item + tabela[i - 1][w - peso_item],
                    tabela[i - 1][w]
                )
            else:
                tabela[i][w] = tabela[i - 1][w]

    valor_maximo = tabela[n][capacidade]

    itens_selecionados = []
    w = capacidade
    for i in range(n, 0, -1):
        if tabela[i][w] != tabela[i - 1][w]:
            item_atual = itens[i - 1]
            itens_selecionados.append(item_atual['nome'])
            w -= item_atual['peso']

    itens_selecionados.reverse()
    return valor_maximo, itens_selecionados
