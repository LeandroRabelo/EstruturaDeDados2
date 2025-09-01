import sys

class Grafo:
    def __init__(self):
        self.locais = []
        self.mapa_indices = {}
        self.lista_adj = {}
        self.matriz_adj = []

    def adicionar_local(self, nome_local):
        if nome_local not in self.mapa_indices:
            indice = len(self.locais)
            self.locais.append(nome_local)
            self.mapa_indices[nome_local] = indice

            self.lista_adj[nome_local] = []

            for linha in self.matriz_adj:
                linha.append(0)
            self.matriz_adj.append([0] * (indice + 1))
            print(f"-> Centro de Distribuição '{nome_local}' adicionado.")
            return True
        else:
            print(f"** Erro: O local '{nome_local}' já existe. **")
            return False

    def adicionar_rota(self, origem, destino, custo, direcionada=False):
        if origem not in self.mapa_indices or destino not in self.mapa_indices:
            print(f"** Erro: Origem '{origem}' ou destino '{destino}' não encontrado. **")
            return False

        idx_origem = self.mapa_indices[origem]
        idx_destino = self.mapa_indices[destino]

        self.matriz_adj[idx_origem][idx_destino] = custo

        self.lista_adj[origem].append((destino, custo))

        if not direcionada:
            self.matriz_adj[idx_destino][idx_origem] = custo
            self.lista_adj[destino].append((origem, custo))
        
        print(f"-> Rota adicionada: {origem} <-> {destino} (Custo: {custo})")
        return True
    
    def visualizar_mapa(self):
        if not self.locais:
            print("\nO mapa está vazio. Adicione locais e rotas primeiro.")
            return

        print("\n--- Visualização da Malha Logística ---")

        print("\n📋 1. LISTA DE ADJACÊNCIAS:")
        print("-" * 30)
        for local, rotas in self.lista_adj.items():
            conexoes = " -> ".join([f"{destino}({custo})" for destino, custo in rotas])
            if not conexoes:
                conexoes = " (sem rotas de saída)"
            print(f"📍 {local}: {conexoes}")
        print("-" * 30)

        print("\n📊 2. MATRIZ DE ADJACÊNCIAS:")
        print("-" * (len(self.locais) * 8 + 1))
        
        header = " " * 12
        for local in self.locais:
            header += f"{local[:6]:<8}"
        print(header)

        for i, local in enumerate(self.locais):
            linha_str = f"{local[:10]:<12}"
            for j in range(len(self.locais)):
                linha_str += f"{self.matriz_adj[i][j]:<8}"
            print(linha_str)
        print("-" * (len(self.locais) * 8 + 1))