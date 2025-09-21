def problema_do_troco(moedas_em_reais, valor_total_em_reais):
    valor_total_em_centavos = int(round(valor_total_em_reais * 100))
    moedas_em_centavos = [int(round(m * 100)) for m in moedas_em_reais]
    
    moedas_em_centavos.sort(reverse=True)
    
    troco = {}
    valor_restante = valor_total_em_centavos

    for moeda_centavos in moedas_em_centavos:
        if valor_restante >= moeda_centavos:
            quantidade = valor_restante // moeda_centavos
            
            moeda_reais = moeda_centavos / 100.0
            troco[moeda_reais] = quantidade
            
            valor_restante -= quantidade * moeda_centavos

    if valor_restante == 0:
        return troco
    else:
        return None

def escalonamento_de_intervalos(tarefas):
    if not tarefas:
        return []

    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['fim'])
    
    agenda = []
    agenda.append(tarefas_ordenadas[0])
    ultimo_horario_fim = tarefas_ordenadas[0]['fim']
    
    for i in range(1, len(tarefas_ordenadas)):
        tarefa_atual = tarefas_ordenadas[i]
        if tarefa_atual['inicio'] >= ultimo_horario_fim:
            agenda.append(tarefa_atual)
            ultimo_horario_fim = tarefa_atual['fim']
            
    return agenda

def mochila_fracionaria(itens, capacidade):
    for item in itens:
        item['razao'] = item['valor'] / item['peso']

    itens.sort(key=lambda x: x['razao'], reverse=True)

    valor_total = 0.0
    peso_atual = 0.0
    mochila = []

    for item in itens:
        if peso_atual + item['peso'] <= capacidade:
            mochila.append({'nome': item['nome'], 'peso_adicionado': item['peso']})
            peso_atual += item['peso']
            valor_total += item['valor']
        else:
            peso_restante = capacidade - peso_atual
            fracao = peso_restante / item['peso']
            
            mochila.append({'nome': item['nome'], 'peso_adicionado': round(peso_restante, 2)})
            valor_total += item['valor'] * fracao
            peso_atual += peso_restante
            break

    return round(valor_total, 2), mochila