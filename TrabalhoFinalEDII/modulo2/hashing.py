import math

class TabelaHash:

    def __init__(self, tamanho, funcao_hash_nome):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self._funcao_hash = self._escolher_funcao(funcao_hash_nome)
        if not self._funcao_hash:
            raise ValueError(f"Função de hash '{funcao_hash_nome}' desconhecida!")

    def _escolher_funcao(self, nome):
        if nome == "transformacao_raiz":
            return self.hash_transformacao_raiz
        elif nome == "meio_quadrado":
            return self.hash_meio_quadrado
        return None

    def _chave_para_int(self, chave):
        return sum(ord(c) for c in str(chave))

    def hash_transformacao_raiz(self, chave):
        chave_int = self._chave_para_int(chave)
        if chave_int == 0: return 0
        raiz = math.sqrt(chave_int)
        parte_fracionaria = raiz - int(raiz)
        indice = int(self.tamanho * parte_fracionaria)
        return indice

    def hash_meio_quadrado(self, chave):
        chave_int = self._chave_para_int(chave)
        quadrado = chave_int ** 2
        str_quadrado = str(quadrado)
        
        tam_tabela_str = len(str(self.tamanho - 1))
        meio_str = len(str_quadrado) // 2
        
        inicio = meio_str - (tam_tabela_str // 2)
        if inicio < 0: inicio = 0
        fim = inicio + tam_tabela_str
        
        str_indice = str_quadrado[inicio:fim]
        
        if not str_indice: return 0
        
        indice = int(str_indice) % self.tamanho
        return indice

    def inserir(self, chave, valor):
        indice = self._funcao_hash(chave)
        balde = self.tabela[indice]

        for i, (k, v) in enumerate(balde):
            if k == chave:
                balde[i] = (chave, valor)
                return

        balde.append((chave, valor))

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        balde = self.tabela[indice]

        for k, v in balde:
            if k == chave:
                return v
        
        return None

    def remover(self, chave):
        indice = self._funcao_hash(chave)
        balde = self.tabela[indice]

        for i, (k, v) in enumerate(balde):
            if k == chave:
                del balde[i]
                return True
        
        return False

    def exibir_estatisticas(self):
        num_itens = sum(len(balde) for balde in self.tabela)
        fator_carga = num_itens / self.tamanho if self.tamanho > 0 else 0
        colisoes = sum(len(balde) - 1 for balde in self.tabela if len(balde) > 1)
        maior_balde = max(len(balde) for balde in self.tabela) if num_itens > 0 else 0

        print("\n--- Estatísticas do Sistema de Consulta ---")
        print(f"Tamanho do Sistema: {self.tamanho} posições")
        print(f"Número de Veículos: {num_itens}")
        print(f"Fator de Carga: {fator_carga:.2f}")
        print(f"Total de Colisões: {colisoes}")
        print(f"Tamanho da Maior Lista (Pior Caso de Busca): {maior_balde}")
        print("---------------------------------------------")