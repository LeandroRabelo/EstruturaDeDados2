def problema_do_troco(moedas_em_reais, valor_total_em_reais):
    # 1. Converte tudo para centavos para trabalhar com inteiros
    valor_total_em_centavos = int(round(valor_total_em_reais * 100))
    moedas_em_centavos = [int(round(m * 100)) for m in moedas_em_reais]

    # Garante que as moedas estejam ordenadas da maior para a menor
    moedas_em_centavos.sort(reverse=True)
    
    troco = {}
    valor_restante = valor_total_em_centavos

    for moeda_centavos in moedas_em_centavos:
        if valor_restante >= moeda_centavos:
            quantidade = valor_restante // moeda_centavos
            
            # A chave do dicionário é o valor em Reais, para fácil leitura
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

    # 1. Ordena as tarefas pela hora de término
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['fim'])
    
    agenda = []
    # 2. Seleciona a primeira tarefa (a que termina mais cedo)
    agenda.append(tarefas_ordenadas[0])
    ultimo_horario_fim = tarefas_ordenadas[0]['fim']
    
    # 3. Percorre o resto das tarefas
    for i in range(1, len(tarefas_ordenadas)):
        tarefa_atual = tarefas_ordenadas[i]
        # Se a tarefa atual começar depois que a última agendada terminou...
        if tarefa_atual['inicio'] >= ultimo_horario_fim:
            agenda.append(tarefa_atual)
            ultimo_horario_fim = tarefa_atual['fim']
            
    return agenda

def mochila_fracionaria(itens, capacidade):
    # 1. Calcula a relação valor/peso para cada item
    for item in itens:
        item['razao'] = item['valor'] / item['peso']

    # 2. Ordena os itens pela razão em ordem decrescente
    itens.sort(key=lambda x: x['razao'], reverse=True)

    valor_total = 0.0
    peso_atual = 0.0
    mochila = []

    # 3. Preenche a mochila
    for item in itens:
        if peso_atual + item['peso'] <= capacidade:
            # Adiciona o item inteiro
            mochila.append({'nome': item['nome'], 'peso_adicionado': item['peso']})
            peso_atual += item['peso']
            valor_total += item['valor']
        else:
            # Adiciona uma fração do item para encher a mochila
            peso_restante = capacidade - peso_atual
            fracao = peso_restante / item['peso']
            
            mochila.append({'nome': item['nome'], 'peso_adicionado': round(peso_restante, 2)})
            valor_total += item['valor'] * fracao
            peso_atual += peso_restante
            break # A mochila está cheia

    return round(valor_total, 2), mochila