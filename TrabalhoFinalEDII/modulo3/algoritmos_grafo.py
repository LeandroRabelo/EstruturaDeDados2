import heapq

def busca_em_profundidade(grafo, inicio, visitados=None, caminho=None):
    if visitados is None:
        visitados = set()
    if caminho is None:
        caminho = []
        
    if inicio not in visitados:
        visitados.add(inicio)
        caminho.append(inicio)
        for vizinho, _ in sorted(grafo.lista_adj[inicio]):
            if vizinho not in visitados:
                busca_em_profundidade(grafo, vizinho, visitados, caminho)
    return caminho

def busca_em_largura(grafo, inicio):
    if inicio not in grafo.locais:
        return {}
        
    visitados = {inicio}
    fila = [(inicio, 0)]
    niveis_distancia = {inicio: 0}
    
    while fila:
        local_atual, nivel = fila.pop(0)
        
        for vizinho, _ in sorted(grafo.lista_adj[local_atual]):
            if vizinho not in visitados:
                visitados.add(vizinho)
                niveis_distancia[vizinho] = nivel + 1
                fila.append((vizinho, nivel + 1))
                
    return niveis_distancia

def dijkstra(grafo, inicio, fim):
    if inicio not in grafo.locais or fim not in grafo.locais:
        return None, float('inf')

    custos = {local: float('inf') for local in grafo.locais}
    custos[inicio] = 0
    caminho_anterior = {local: None for local in grafo.locais}
    
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        custo_atual, local_atual = heapq.heappop(fila_prioridade)
        
        if custo_atual > custos[local_atual]:
            continue

        if local_atual == fim:
            break

        for vizinho, peso in grafo.lista_adj[local_atual]:
            novo_custo = custo_atual + peso
            if novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                caminho_anterior[vizinho] = local_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))

    caminho = []
    local = fim
    while local is not None:
        caminho.insert(0, local)
        local = caminho_anterior[local]

    if caminho[0] == inicio:
        return caminho, custos[fim]
    else:
        return None, float('inf')
    
def welch_powell(grafo):
    if not grafo.locais:
        return {}

    nodes = sorted(grafo.lista_adj, key=lambda v: len(grafo.lista_adj[v]), reverse=True)
    
    coloring = {}
    color_num = 0

    for node in nodes:
        if node not in coloring:
            color_num += 1
            coloring[node] = color_num

            for other_node in nodes:
                if other_node not in coloring:
                    is_adjacent = False
                    for neighbor, _ in grafo.lista_adj[other_node]:
                        if neighbor in coloring and coloring.get(neighbor) == color_num:
                            is_adjacent = True
                            break
                    if not is_adjacent:
                        coloring[other_node] = color_num
                        
    return coloring, color_num

def ordenacao_topologica(grafo):
    grau_entrada = {v: 0 for v in grafo.lista_adj}
    for v in grafo.lista_adj:
        for vizinho, _ in grafo.lista_adj[v]:
            grau_entrada[vizinho] += 1
            
    fila = [v for v in grafo.lista_adj if grau_entrada[v] == 0]
    
    ordem = []
    
    while fila:
        v = fila.pop(0)
        ordem.append(v)
        
        for vizinho, _ in grafo.lista_adj[v]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)
                
    if len(ordem) == len(grafo.lista_adj):
        return ordem
    else:
        return None

def prim_mst(grafo):
    if not grafo.locais:
        return [], 0

    mst = []
    custo_total = 0
    visitados = set()

    inicio = grafo.locais[0]

    arestas = []
    for vizinho, custo in grafo.lista_adj[inicio]:
        heapq.heappush(arestas, (custo, inicio, vizinho))
        
    visitados.add(inicio)

    while arestas and len(visitados) < len(grafo.locais):
        custo, origem, destino = heapq.heappop(arestas)
        
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, custo))
            custo_total += custo
            
            for prox_vizinho, prox_custo in grafo.lista_adj[destino]:
                if prox_vizinho not in visitados:
                    heapq.heappush(arestas, (prox_custo, destino, prox_vizinho))
                    
    return mst, custo_total
