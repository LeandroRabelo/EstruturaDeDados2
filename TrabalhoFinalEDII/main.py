import time
import random
from Dados.clientes import carregar_clientes, cadastrar_cliente, remover_cliente
from Dados.pedidos import carregar_pedidos, cadastrar_pedido, remover_pedido
from modulo1.buscas import busca_sequencial, busca_binaria, busca_rabin_karp
from modulo2.desafios_mod2 import menu_compressao, menu_hashing


def executar_desafio_1():
    print("\n" + "="*50)
    print("--- DESAFIO 1: LOCALIZAÇÃO DE CARGA URGENTE ---")
    print("="*50)
    
    print("\n[CENA]: O pátio de recebimento está cheio. Mais de mil pacotes descarregados...")
    time.sleep(1.5)
    
    pedidos = carregar_pedidos()
    if not pedidos:
        print("!!! ERRO: Arquivo 'pedidos.txt' está vazio ou não foi encontrado.")
        input("Pressione Enter para voltar...")
        return
        
    print(f"[SISTEMA]: {len(pedidos)} pacotes não triados na base de dados.")
    time.sleep(1.5)
    
    pedido_urgente = random.choice(pedidos)
    id_alvo = pedido_urgente['id']
    
    print("\n[ALERTA]: Solicitação de última hora!")
    print(f"[MISSÃO]: Encontre o PEDIDO URGENTE com o ID: {id_alvo}")
    time.sleep(1)
    
    input("\nPressione Enter para iniciar a BUSCA SEQUENCIAL no pátio...")
    
    print("\nIniciando varredura item por item...")
    time.sleep(1)
    
    t_inicio = time.perf_counter()
    random.shuffle(pedidos)
    item_encontrado, comparacoes = busca_sequencial(pedidos, 'id', id_alvo)
    t_fim = time.perf_counter()
    
    tempo_total = t_fim - t_inicio

    for i in range(min(comparacoes, 20)):
        print(f"  Verificando pacote ID {pedidos[i]['id']}...")
        time.sleep(0.02)
    
    if comparacoes > 20:
        print("  ...")
        time.sleep(0.5)

    print("\n" + "-"*50)
    print("--- ANÁLISE DE DESEMPENHO (BUSCA SEQUENCIAL) ---")
    if item_encontrado:
        print(f"✅ SUCESSO! Pacote {item_encontrado['id']} encontrado.")
        print(f"   Produto: {item_encontrado['produto']}")
    else:
        print("❌ FALHA! Pacote não localizado.")
        
    print(f"\n📈 Comparações Realizadas: {comparacoes}")
    print(f"⏱️ Tempo de Execução: {tempo_total:.6f} segundos")
    print("-"*50)
    
    input("\nPressione Enter para voltar ao menu de desafios...")

def executar_desafio_2():
    print("\n" + "="*55)
    print("--- DESAFIO 2: AUDITORIA RÁPIDA NO ARMAZÉM ORDENADO ---")
    print("="*55)
    
    print("\n[CENA]: Você é o auditor. Os dados dos clientes estão em um catálogo digital,")
    print("        perfeitamente ORDENADO por ID, pronto para consulta.")
    time.sleep(2)
    
    clientes = carregar_clientes()
    if not clientes:
        print("!!! ERRO: Arquivo 'clientes.txt' está vazio ou não foi encontrado.")
        input("Pressione Enter para voltar...")
        return
        
    print(f"[SISTEMA]: {len(clientes)} clientes carregados na base de dados ordenada.")
    time.sleep(1.5)
    
    alvo_idx = random.randint(len(clientes) // 2, len(clientes) - 1)
    cliente_alvo = clientes[alvo_idx]
    id_alvo = cliente_alvo['id']

    print("\n[ALERTA]: Auditoria solicitada!")
    print(f"[MISSÃO]: Localize o cliente com o ID: {id_alvo} o mais rápido possível.")
    time.sleep(1)
    
    input("\nPressione Enter para iniciar a AUDITORIA com AMBOS os algoritmos...")

    t_inicio_bin = time.perf_counter()
    item_bin, comps_bin = busca_binaria(clientes, 'id', id_alvo)
    t_fim_bin = time.perf_counter()
    tempo_bin = t_fim_bin - t_inicio_bin

    t_inicio_seq = time.perf_counter()
    random.shuffle(clientes)
    item_seq, comps_seq = busca_sequencial(clientes, 'id', id_alvo)
    t_fim_seq = time.perf_counter()
    tempo_seq = t_fim_seq - t_inicio_seq
    
    print("\n" + "-"*60)
    print("--- ANÁLISE DE DESEMPENHO COMPARATIVA ---")
    print(f"Alvo: Cliente ID {id_alvo} ('{item_bin['nome']}')")
    print("\n+------------------+------------------+--------------------+")
    print("| MÉTRICA          | BUSCA BINÁRIA    | BUSCA SEQUENCIAL   |")
    print("+------------------+------------------+--------------------+")
    print(f"| Comparações      | {comps_bin:<16} | {comps_seq:<18} |")
    print(f"| Tempo (s)        | {tempo_bin:<16.6f} | {tempo_seq:<18.6f} |")
    print("+------------------+------------------+--------------------+")

    if comps_bin > 0:
        eficiencia = comps_seq / comps_bin
        print(f"\n✅ CONCLUSÃO: A Busca Binária foi {eficiencia:.1f} vezes mais eficiente!")
    
    print("-"*60)
    input("\nPressione Enter para voltar ao menu de desafios...")

def executar_desafio_3():
    print("\n" + "="*55)
    print("--- DESAFIO 3: RASTREAMENTO DE LOTE EM MANIFESTOS ---")
    print("="*55)

    padrao_alvo = "LOTE-XR-734"
    produtos_exemplo = [
        "Smartphone Z10", "Notebook Pro S", "Cadeira Gamer Confort", "Monitor UltraWide 34", "Teclado Luminoso",
        "Mouse Vertical", "Fone com Ruído", "Webcam Full HD", "Impressora Laser", "Tablet 11", "SSD Externo 2TB"
    ]
    
    linhas_manifesto = []
    header = f"""DATA: {time.strftime('%d/%m/%Y')} - MANIFESTO DE CARGA TR-{random.randint(1000, 9999)}
ORIGEM: Centro de Distribuição São Paulo | DESTINO: Armazém Regional Curitiba
VEÍCULO: Placa XYZ-{random.randint(1000, 9999)} | TOTAL DE VOLUMES: 100
--- LISTA DE ITENS ---"""
    linhas_manifesto.append(header)

    for i in range(100):
        lote = f"LOTE-{random.choice(['AB','CD','EF'])}-{random.randint(100,999)}-{random.choice(['XY','YZ','ZA'])}"
        if i in [17, 53, 89]:
            lote = padrao_alvo
        id_item = 9001 + i
        produto = random.choice(produtos_exemplo)
        id_cliente = random.randint(101, 600)
        linha_item = f"ID: {id_item}, PROD: {produto}, LOTE: {lote}, CLIENTE: {id_cliente}"
        linhas_manifesto.append(linha_item)

    linhas_manifesto.append("--- FIM DO DOCUMENTO ---")
    manifesto = "\n".join(linhas_manifesto)

    print("\n[CENA]: Você é o analista de conformidade. Um alerta de recall foi emitido.")
    time.sleep(1.5)
    print(f"[MISSÃO]: Encontrar todas as menções do lote de produto '{padrao_alvo}' em um grande manifesto de carga.")
    time.sleep(1.5)
    print("\n[SISTEMA]: Um manifesto com 100 itens de carga foi carregado para análise.")
    
    ver_manifesto = input("Deseja visualizar o manifesto completo antes da busca? (s/n): ").lower()
    if ver_manifesto == 's':
        print("\n--- Manifesto de Carga a ser Analisado ---")
        print(manifesto)
        print("----------------------------------------")

    input("\nPressione Enter para iniciar a varredura com o Rabin-Karp...")

    t_inicio = time.perf_counter()
    indices_encontrados = busca_rabin_karp(manifesto, padrao_alvo)
    t_fim = time.perf_counter()
    tempo_total = t_fim - t_inicio

    print("\n" + "-"*55)
    print("--- RESULTADO DA ANÁLISE (RABIN-KARP) ---")
    if not indices_encontrados:
        print(f"✅ Nenhuma ocorrência do padrão '{padrao_alvo}' foi encontrada.")
    else:
        print(f"✅ SUCESSO! Encontradas {len(indices_encontrados)} ocorrências do padrão '{padrao_alvo}':")
        for idx in indices_encontrados:
            linha_num = manifesto[:idx].count('\n') + 1
            pos_linha_inicio = manifesto.rfind('\n', 0, idx) + 1
            pos_caractere = idx - pos_linha_inicio
            linha_completa = manifesto.splitlines()[linha_num-1].strip()
            print(f"\n   - Localizado na Linha {linha_num}, Caractere {pos_caractere}")
            print(f"     Contexto: {linha_completa}")
    
    print(f"\n⏱️ Tempo de Varredura: {tempo_total:.6f} segundos")
    print("-"*55)
    input("\nPressione Enter para voltar ao menu de desafios...")

def menu_desafios():
    while True:
        print("\n--- Menu de Desafios de Busca ---")
        print("1. Desafio 1: Busca Sequencial (Pátio de Carga)")
        print("2. Desafio 2: Busca Binária (Armazém Ordenado)")
        print("3. Desafio 3: Rabin-Karp (Rastreamento de Lote)")
        print("0. Voltar ao menu principal")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            executar_desafio_1()
        elif escolha == '2':
            executar_desafio_2()
        elif escolha == '3':
            executar_desafio_3()
        elif escolha == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_gerenciar_clientes():
    while True:
        print("\n--- Gerenciar Clientes ---")
        print("1. Listar todos os clientes")
        print("2. Cadastrar novo cliente")
        print("3. Remover cliente por ID")
        print("0. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            print("\n-- Lista de Clientes --")
            clientes = carregar_clientes()
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | Cidade: {cliente['cidade']}")
            input("\nPressione Enter para continuar...")
        elif escolha == '2':
            print("\n-- Cadastrar Novo Cliente --")
            nome = input("Digite o nome do cliente: ")
            cidade = input("Digite a cidade do cliente: ")
            cadastrar_cliente(nome, cidade)
            input("\nPressione Enter para continuar...")
        elif escolha == '3':
            print("\n-- Remover Cliente --")
            id_remover = input("Digite o ID do cliente a ser removido: ")
            remover_cliente(id_remover)
            input("\nPressione Enter para continuar...")
        elif escolha == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")

def menu_gerenciar_pedidos():
    while True:
        print("\n--- Gerenciar Pedidos ---")
        print("1. Listar todos os pedidos")
        print("2. Cadastrar novo pedido")
        print("3. Remover pedido por ID")
        print("0. Voltar ao menu principal")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            print("\n-- Lista de Pedidos --")
            pedidos = carregar_pedidos()
            if not pedidos:
                print("Nenhum pedido cadastrado.")
            else:
                for pedido in pedidos:
                    print(f"ID Pedido: {pedido['id']} | Produto: {pedido['produto']} | ID Cliente: {pedido['id_cliente']}")
            input("\nPressione Enter para continuar...")
        elif escolha == '2':
            print("\n-- Cadastrar Novo Pedido --")
            produto = input("Digite o nome do produto: ")
            id_cliente = input("Digite o ID do cliente para este pedido: ")
            cadastrar_pedido(produto, id_cliente)
            input("\nPressione Enter para continuar...")
        elif escolha == '3':
            print("\n-- Remover Pedido --")
            id_remover = input("Digite o ID do pedido a ser removido: ")
            remover_pedido(id_remover)
            input("\nPressione Enter para continuar...")
        elif escolha == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")

def menu_otimizacao():
    while True:
        print("\n--- Módulo 2: Otimização de Recursos ---")
        print("1. Desafio de Compressão (Huffman)")
        print("2. Desafio de Acesso Rápido (Hashing)")
        print("0. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            menu_compressao()
        elif escolha == '2':
            menu_hashing()
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")
            
def main():
    while True:
        print("\n--- Logística Inteligente - Menu Principal ---")
        print("1. Módulo 1: Desafios de Busca")
        print("2. Módulo 2: Desafios de Otimização")
        print("3. Gerenciar Clientes")
        print("4. Gerenciar Pedidos")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            menu_desafios()
        elif escolha == '2':
            menu_otimizacao()
        elif escolha == '3':
            menu_gerenciar_clientes()
        elif escolha == '4':
            menu_gerenciar_pedidos()
        elif escolha == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            
if __name__ == "__main__":
    main()