def busca_sequencial(lista, chave, valor_buscado):
    comparacoes = 0
    for item in lista:
        comparacoes += 1
        if item[chave] == valor_buscado:
            return item, comparacoes
    return None, comparacoes

def busca_binaria(lista_ordenada, chave, valor_buscado):
    inicio = 0
    fim = len(lista_ordenada) - 1
    comparacoes = 0

    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        valor_meio = lista_ordenada[meio][chave]

        if valor_meio == valor_buscado:
            return lista_ordenada[meio], comparacoes
        elif valor_buscado < valor_meio:
            fim = meio - 1
        else:
            inicio = meio + 1

    return None, comparacoes

def busca_rabin_karp(texto_completo, padrao_buscado):
    n = len(texto_completo)
    m = len(padrao_buscado)
    if n < m:
        return []

    d = 256
    q = 101
    h = pow(d, m - 1, q)
    hash_padrao = 0
    hash_texto_janela = 0
    ocorrencias = []

    for i in range(m):
        hash_padrao = (d * hash_padrao + ord(padrao_buscado[i])) % q
        hash_texto_janela = (d * hash_texto_janela + ord(texto_completo[i])) % q

    for i in range(n - m + 1):
        if hash_padrao == hash_texto_janela:
            if texto_completo[i:i+m] == padrao_buscado:
                ocorrencias.append(i)

        if i < n - m:
            hash_texto_janela = (
                d * (hash_texto_janela - ord(texto_completo[i]) * h) + ord(texto_completo[i + m])
            ) % q
            if hash_texto_janela < 0:
                hash_texto_janela += q

    return ocorrencias