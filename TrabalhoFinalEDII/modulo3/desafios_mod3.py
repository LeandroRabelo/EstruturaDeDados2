import json
import os
from modulo3.grafo import Grafo
from modulo3.algoritmos_grafo import busca_em_profundidade, busca_em_largura, dijkstra, welch_powell, ordenacao_topologica, prim_mst

def carregar_malha_padrao(arquivo="malha_logistica.json"):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_dados = os.path.join(diretorio_atual, '..', 'Dados', arquivo)

    try:
        with open(caminho_dados, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        print(f"\nCarregando malha do arquivo '{arquivo}'...")
        
        grafo_novo = Grafo()
        for local in dados['locais']:
            grafo_novo.adicionar_local(local)
            
        for rota in dados['rotas']:
            grafo_novo.adicionar_rota(rota['origem'], rota['destino'], rota['custo'])
            
        print("Malha logística carregada com sucesso!")
        return grafo_novo

    except FileNotFoundError:
        print(f"** Erro: Arquivo '{caminho_dados}' não encontrado. **")
        print("Execute o 'gerador_malha_logistica.py' na pasta 'Dados' primeiro.")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"** Erro ao ler o arquivo JSON: {e} **")
        return None

def executar_desafio_dfs(mapa):
    print("\n--- 🔍 Desafio DFS: Rota de Inspeção Profunda ---")
    if not mapa.locais:
        print("** O mapa está vazio. Carregue uma malha logística primeiro. **")
        return
    
    inicio = input(f"Digite o centro de distribuição inicial ({', '.join(mapa.locais[:3])}, etc.): ")
    if inicio not in mapa.locais:
        print(f"** Erro: Local '{inicio}' não existe no mapa. **")
        return
        
    print(f"\n[MISSÃO]: Um inspetor precisa visitar o máximo de locais interconectados a partir de '{inicio}',")
    print("           seguindo cada rota até o fim antes de voltar. A DFS simula essa exploração.")
    input("\nPressione Enter para iniciar a busca em profundidade...")
    
    caminho_dfs = busca_em_profundidade(mapa, inicio)
    
    print("\n--- Resultado da Exploração (DFS) ---")
    print("Ordem de visita para uma exploração profunda:")
    print(" -> ".join(caminho_dfs))

def executar_desafio_bfs(mapa):
    print("\n--- 🌊 Desafio BFS: Análise de Capilaridade da Rede ---")
    if not mapa.locais:
        print("** O mapa está vazio. Carregue uma malha logística primeiro. **")
        return
        
    inicio = input(f"Digite o centro de distribuição para a análise ({', '.join(mapa.locais[:3])}, etc.): ")
    if inicio not in mapa.locais:
        print(f"** Erro: Local '{inicio}' não existe no mapa. **")
        return
        
    print(f"\n[MISSÃO]: Analisar a capilaridade da rede a partir de '{inicio}'.")
    print("           A BFS é ideal para descobrir todos os locais alcançáveis e a quantos 'saltos' (rotas) de distância eles estão.")
    input("\nPressione Enter para iniciar a busca em largura...")
    
    distancias = busca_em_largura(mapa, inicio)
    
    print("\n--- Resultado da Análise de Proximidade (BFS) ---")
    niveis = {}
    for local, dist in distancias.items():
        if dist not in niveis:
            niveis[dist] = []
        niveis[dist].append(local)
    
    for nivel, locais in sorted(niveis.items()):
        print(f"Distância de {nivel} saltos: {', '.join(locais)}")
        
def executar_desafio_dijkstra(mapa):
    print("\n--- 📈 Desafio Dijkstra: Otimização de Rota de Entrega ---")
    if not mapa.locais:
        print("** O mapa está vazio. Carregue uma malha logística primeiro. **")
        return
    
    print("Locais disponíveis:", ", ".join(mapa.locais))
    inicio = input("Digite o local de partida: ")
    fim = input("Digite o local de destino: ")
    
    if inicio not in mapa.locais or fim not in mapa.locais:
        print("** Erro: Um dos locais digitados não existe no mapa. **")
        return
        
    print(f"\n[MISSÃO]: Calcular a rota mais curta e de menor custo (distância) entre '{inicio}' e '{fim}'.")
    print("           O Algoritmo de Dijkstra garantirá o caminho mais eficiente.")
    input("\nPressione Enter para calcular a rota ótima...")
    
    caminho, custo = dijkstra(mapa, inicio, fim)
    
    print("\n--- Resultado do Cálculo de Rota (Dijkstra) ---")
    if caminho:
        print(f"✅ Rota Mais Eficiente Encontrada:")
        print(f"   Caminho: {' -> '.join(caminho)}")
        print(f"   Custo Total (Distância): {custo} km")
    else:
        print(f"❌ Não foi possível encontrar uma rota entre '{inicio}' e '{fim}'.")

def executar_desafio_coloracao(mapa):
    print("\n--- 🎨 Desafio de Coloração: Alocação de Docks de Carga ---")
    print("[MISSÃO]: Centros de distribuição vizinhos não podem ter entregas da mesma transportadora no mesmo dia para evitar congestionamento.")
    print("           O algoritmo de coloração determinará o número mínimo de 'dias/transportadoras' (cores) necessários para operar sem conflitos.")
    input("\nPressione Enter para calcular a alocação ótima...")

    coloring, num_cores = welch_powell(mapa)
    
    print("\n--- Resultado da Alocação (Welch-Powell) ---")
    print(f"✅ Número mínimo de 'cores' (dias/transportadoras) necessárias: {num_cores}")
    
    dias = {}
    for local, cor in coloring.items():
        if cor not in dias:
            dias[cor] = []
        dias[cor].append(local)
        
    for dia, locais in sorted(dias.items()):
        print(f"  - Dia/Transportadora {dia}: {', '.join(locais)}")

def executar_desafio_ordenacao(mapa_logistico):
    print("\n--- 📅 Desafio de Ordenação Topológica: Sequenciamento de Carregamento de Contêiner ---")
    print("[MISSÃO]: Um contêiner precisa ser carregado com diferentes tipos de mercadorias.")
    print("           A ordem é crítica para a segurança: itens pesados no fundo, frágeis por último, e alguns produtos não podem ser vizinhos.")
    print("           Vamos usar a Ordenação Topológica para gerar um plano de carregamento seguro e eficiente.")
    input("\nPressione Enter para construir o grafo de regras de carregamento e encontrar a sequência...")

    grafo_carga = Grafo()
    
    etapas = [
        "Maquinario Pesado (Fundo)",
        "Eletronicos",
        "Alimentos Secos",
        "Tambores Quimicos (Area Isolada)",
        "Vidraria (Fragil)",
        "Preencher Espacos Vazios com Isopor",
        "Lacre e Inspecao Final"
    ]
    for etapa in etapas:
        grafo_carga.adicionar_local(etapa)

    print("\n[SISTEMA]: Construindo o mapa de dependências direcionadas do plano de carga...")

    grafo_carga.adicionar_rota("Maquinario Pesado (Fundo)", "Eletronicos", 1, direcionada=True)
    grafo_carga.adicionar_rota("Eletronicos", "Vidraria (Fragil)", 1, direcionada=True)
    grafo_carga.adicionar_rota("Alimentos Secos", "Lacre e Inspecao Final", 1, direcionada=True)
    grafo_carga.adicionar_rota("Tambores Quimicos (Area Isolada)", "Lacre e Inspecao Final", 1, direcionada=True)
    grafo_carga.adicionar_rota("Vidraria (Fragil)", "Preencher Espacos Vazios com Isopor", 1, direcionada=True)
    grafo_carga.adicionar_rota("Preencher Espacos Vazios com Isopor", "Lacre e Inspecao Final", 1, direcionada=True)
    
    print("\nVisualização do Grafo de Regras de Carregamento (Lista de Adjacências):")
    grafo_carga.visualizar_mapa()

    input("\nPressione Enter para executar o algoritmo de Kahn e gerar o plano...")

    ordem = ordenacao_topologica(grafo_carga)
    
    print("\n--- Resultado do Sequenciamento (Kahn's Algorithm) ---")
    if ordem:
        print("✅ Plano de Carregamento Válido Gerado:")

        for i, passo in enumerate(ordem):
            print(f"   Passo {i+1}: {passo}")
            
    else:
        print("❌ ERRO: Foi detectado um ciclo de dependências nas regras! (Ex: Carga A deve vir antes de B, e B antes de A). O plano é inválido.")

def executar_desafio_mst(mapa):
    print("\n--- 🌳 Desafio da Árvore Geradora Mínima: Rede de Fibra Óptica ---")
    print("[MISSÃO]: Conectar todos os centros de distribuição com uma rede de fibra óptica.")
    print("           O custo para passar o cabo entre duas cidades é a distância entre elas.")
    print("           O algoritmo de Prim calculará a rede de menor custo total que conecta todos, sem criar caminhos redundantes (ciclos).")
    input("\nPressione Enter para calcular a rede de custo mínimo...")
    
    mst, custo_total = prim_mst(mapa)
    
    print("\n--- Resultado do Planejamento da Rede (Prim's Algorithm) ---")
    print(f"✅ Rede de custo mínimo encontrada com sucesso!")
    print(f"   Custo Total de Instalação: {custo_total} (unidades de custo)")
    print("   Conexões da Rede:")
    for origem, destino, custo in mst:
        print(f"     - {origem} <--> {destino} (Custo: {custo})")

def menu_submodulo1(mapa):
    while True:
        print("\n--- [Submódulo 1: Fundamentos e Representação] ---")
        print("1. Visualizar Mapa (Lista e Matriz)")
        print("2. Adicionar Novo Centro de Distribuição (Local)")
        print("3. Adicionar Nova Rota")
        print("0. Voltar ao menu de Grafos")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            mapa.visualizar_mapa()
        elif opcao == '2':
            nome_local = input("Digite o nome do novo Centro de Distribuição: ")
            if nome_local:
                mapa.adicionar_local(nome_local)
        elif opcao == '3':
            origem = input("Digite o local de origem: ")
            destino = input("Digite o local de destino: ")
            try:
                custo = int(input("Digite o custo/distância da rota: "))
                mapa.adicionar_rota(origem, destino, custo)
            except ValueError:
                print("** Erro: O custo deve ser um número inteiro. **")
        elif opcao == '0':
            break
        else:
            print("** Opção inválida. **")

def menu_submodulo2(mapa):
    while True:
        print("\n--- [Submódulo 2: Navegação e Caminhos Ótimos] ---")
        print("1. Desafio de Exploração (DFS)")
        print("2. Desafio de Proximidade (BFS)")
        print("3. Desafio da Rota Mais Rápida (Dijkstra)")
        print("0. Voltar ao menu de Grafos")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            executar_desafio_dfs(mapa)
        elif opcao == '2':
            executar_desafio_bfs(mapa)
        elif opcao == '3':
            executar_desafio_dijkstra(mapa)
        elif opcao == '0':
            break
        else:
            print("** Opção inválida. **")

def menu_submodulo3(mapa):
    """Menu para os desafios de Otimização de Processos."""
    while True:
        print("\n--- [Submódulo 3: Otimização de Caminho e Processo] ---")
        print("1. Desafio de Alocação de Recursos (Coloração)")
        print("2. Desafio de Sequenciamento de Tarefas (Ordenação Topológica)")
        print("3. Desafio de Rede de Custo Mínimo (Árvore Geradora Mínima)")
        print("0. Voltar ao menu de Grafos")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            executar_desafio_coloracao(mapa)
        elif opcao == '2':
            executar_desafio_ordenacao(mapa)
        elif opcao == '3':
            executar_desafio_mst(mapa)
        elif opcao == '0':
            break
        else:
            print("** Opção inválida. **")

def menu_desafios_grafos():
    mapa = Grafo()
    print("\nBem-vindo ao Módulo de Grafos. Um mapa vazio foi criado.")
    print("Use a opção 'Carregar Malha Logística' para começar.")
    
    while True:
        print("\n--- 🗺️ Módulo 3: Desafios de Malha Logística (Grafos) ---")
        print("\nSelecione uma ação ou um submódulo para explorar:")
        print("1. Carregar Malha Logística Padrão (Substitui o mapa atual)")
        print("---------------------------------------------------------")
        print("2. Acessar [Submódulo 1: Fundamentos e Representação]")
        print("3. Acessar [Submódulo 2: Navegação e Caminhos Ótimos]")
        print("4. Acessar [Submódulo 3: Otimização de Processos]")
        print("---------------------------------------------------------")
        print("0. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            mapa_carregado = carregar_malha_padrao()
            if mapa_carregado:
                mapa = mapa_carregado
        elif opcao == '2' or opcao == '3' or opcao == '4':
            if not mapa.locais:
                print("\n** ATENÇÃO: O mapa está vazio. Carregue uma malha primeiro (Opção 1). **")
                continue
            
            if opcao == '2':
                menu_submodulo1(mapa)
            elif opcao == '3':
                menu_submodulo2(mapa)
            elif opcao == '4':
                menu_submodulo3(mapa)
        elif opcao == '0':
            print("Retornando ao Menu Principal...")
            break
        else:
            print("** Opção inválida. Tente novamente. **")