import random
from modulo4.algoritmos_gulosos import problema_do_troco, escalonamento_de_intervalos, mochila_fracionaria
from modulo4.programacao_dinamica import mochila_01

def desafio_troco():
    """Desafio 1: Caixa de Adiantamentos para Motoristas."""
    print("\n--- Desafio: Caixa de Adiantamentos para Motoristas ---")
    print("Simulando a necessidade de um adiantamento para despesas de viagem.")
    print("O sistema deve calcular a menor quantidade de cédulas e moedas para o troco.\n")
    
    sistema_monetario_reais = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    while True:
        try:
            valor_str = input("Digite o valor do adiantamento para o motorista (ex: 388.78): ")
            valor_adiantamento = float(valor_str)
            if valor_adiantamento < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    resultado_troco = problema_do_troco(sistema_monetario_reais, valor_adiantamento)

    if resultado_troco:
        print(f"\nPara um adiantamento de R$ {valor_adiantamento:.2f}, o caixa deve entregar:")
        total_items = 0
        for valor, qtd in sorted(resultado_troco.items(), reverse=True):
            print(f"- {qtd} nota(s)/moeda(s) de R$ {valor:.2f}")
            total_items += qtd
        print(f"\nTotal de {total_items} cédulas/moedas entregues.")
    else:
        print("\nNão foi possível calcular o troco com as moedas fornecidas.")

    input("\nPressione Enter para voltar ao menu...")

def desafio_escalonamento():
    """Desafio 2: Agenda da Doca de Carregamento."""
    print("\n--- Desafio: Agenda da Doca de Carregamento ---")
    print("Um centro de distribuição precisa agendar o máximo de tarefas de carregamento")
    print("em uma única doca, sem sobreposição de horários.\n")

    nomes_tarefas = ["Carga de Grãos", "Descarga de Eletrônicos", "Manutenção", 
                     "Carga de Perecíveis", "Inspeção", "Descarga Têxtil", 
                     "Carga Refrigerada", "Coleta de Resíduos"]
    solicitacoes_doca = []
    horario_base = 8.0
    for _ in range(random.randint(5, 8)):
        nome = random.choice(nomes_tarefas)
        inicio = round(random.uniform(horario_base, horario_base + 3), 1)
        fim = round(inicio + random.uniform(1.5, 3.0), 1)
        solicitacoes_doca.append({'nome': nome, 'inicio': inicio, 'fim': fim})
        horario_base = inicio + 0.5

    print("Solicitações aleatórias recebidas para a doca hoje:")
    for tarefa in sorted(solicitacoes_doca, key=lambda x: x['inicio']):
        print(f"- {tarefa['nome']}: das {tarefa['inicio']}h às {tarefa['fim']}h")

    agenda_otimizada = escalonamento_de_intervalos(solicitacoes_doca)

    print("\n--- Agenda Otimizada ---")
    print(f"O sistema selecionou {len(agenda_otimizada)} tarefas para maximizar a utilização da doca:")
    for tarefa in agenda_otimizada:
        print(f"-> {tarefa['nome']}: agendado das {tarefa['inicio']}h às {tarefa['fim']}h")
        
    input("\nPressione Enter para voltar ao menu...")

def desafio_mochila_fracionaria():
    """Desafio 3: Otimização de Carregamento a Granel."""
    print("\n--- Desafio: Otimização de Carregamento a Granel (Mochila Fracionária) ---")
    print("Um caminhão graneleiro com capacidade limitada precisa ser carregado com diferentes")
    print("produtos (que podem ser fracionados) para maximizar o valor total da carga.\n")

    nomes_produtos = ["Minério de Ferro", "Soja", "Milho", "Bauxita", "Fertilizantes", "Sal"]
    produtos_a_granel = []
    for nome in random.sample(nomes_produtos, random.randint(3, 4)):
        peso = random.randint(8000, 20000)
        valor = peso * random.uniform(1.2, 1.8)
        produtos_a_granel.append({'nome': nome, 'peso': peso, 'valor': round(valor, 2)})
    
    capacidade_caminhao = random.randint(20000, 35000)

    print(f"Capacidade do caminhão: {capacidade_caminhao} kg")
    print("Produtos disponíveis no armazém:")
    for p in produtos_a_granel:
        print(f"- {p['nome']}: Estoque de {p['peso']} kg, valendo R$ {p['valor']:.2f}")
    
    valor_max, carga_otimizada = mochila_fracionaria(produtos_a_granel, capacidade_caminhao)

    print("\n--- Plano de Carregamento Otimizado ---")
    print(f"Valor máximo da carga: R$ {valor_max:.2f}")
    print("O sistema recomenda carregar:")
    for item in carga_otimizada:
        print(f"- {item['peso_adicionado']:.2f} kg de {item['nome']}")

    input("\nPressione Enter para voltar ao menu...")

def desafio_mochila_01():
    """Desafio 4: Consolidação de Carga de Alto Valor."""
    print("\n--- Desafio: Consolidação de Carga de Alto Valor (Mochila 0/1) ---")
    print("Uma van com limite de peso precisa ser carregada com pacotes indivisíveis.")
    print("O objetivo é escolher quais pacotes levar para maximizar o valor da entrega,\nrespeitando a capacidade máxima.\n")

    nomes_pacotes = ["Notebook Gamer", "Console", "Sistema de Som", "Peças de Motor",
                     "Equip. Médico", "Roteador Industrial", "Drone Profissional"]
    pacotes = []
    for nome in random.sample(nomes_pacotes, random.randint(4, 5)):
        peso = random.randint(2, 12)
        valor = peso * random.randint(200, 800)
        pacotes.append({'nome': nome, 'peso': peso, 'valor': valor})
    
    capacidade_van = random.randint(15, 25)

    print("Pacotes de alto valor para transporte:")
    for p in pacotes:
        print(f"- {p['nome']}: {p['peso']} kg, Prioridade/Valor R$ {p['valor']}")
    print(f"\nCapacidade da van: {capacidade_van} kg")
    
    valor_otimo, carga_otima = mochila_01(pacotes, capacidade_van)
    
    print("\n--- Solução Ótima Encontrada (Programação Dinâmica) ---")
    print(f"O valor máximo da carga que pode ser transportada é: R$ {valor_otimo}")
    print("O sistema recomenda carregar os seguintes itens para garantir a solução perfeita:")
    for nome_item in carga_otima:
        print(f"- {nome_item}")

    input("\nPressione Enter para voltar ao menu...")

def menu_modulo4():
    """Menu principal para os desafios do Módulo 4."""
    while True:
        print("\n--- Módulo 4: Otimização Avançada de Cargas e Tarefas ---")
        print("\n[--- Algoritmos Gulosos: Decisões Rápidas ---]")
        print("1. Desafio do Troco: Caixa de Adiantamentos")
        print("2. Desafio de Escalonamento: Agenda da Doca")
        print("3. Desafio da Mochila Fracionária: Carga a Granel")
        print("\n[--- Programação Dinâmica: A Solução Perfeita ---]")
        print("4. Desafio da Mochila 0/1: Carga de Alto Valor")
        print("-----------------------------------------------------")
        print("0. Voltar ao Menu Principal")

        escolha = input("Escolha um desafio: ")

        if escolha == '1':
            desafio_troco()
        elif escolha == '2':
            desafio_escalonamento()
        elif escolha == '3':
            desafio_mochila_fracionaria()
        elif escolha == '4':
            desafio_mochila_01()
        elif escolha == '0':
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")