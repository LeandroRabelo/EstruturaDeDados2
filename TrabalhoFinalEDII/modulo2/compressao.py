import heapq
from collections import defaultdict
import pickle

class NoHuffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def _calcular_frequencia(texto):
    return defaultdict(int, {char: texto.count(char) for char in set(texto)})

def _construir_arvore(frequencias):
    fila_prioridade = [NoHuffman(char, freq) for char, freq in frequencias.items()]
    heapq.heapify(fila_prioridade)

    while len(fila_prioridade) > 1:
        no_esquerdo = heapq.heappop(fila_prioridade)
        no_direito = heapq.heappop(fila_prioridade)

        freq_somada = no_esquerdo.freq + no_direito.freq
        no_pai = NoHuffman(None, freq_somada)
        no_pai.left = no_esquerdo
        no_pai.right = no_direito

        heapq.heappush(fila_prioridade, no_pai)
    
    return fila_prioridade[0]

def _gerar_codigos_recursivo(no, codigo_atual, codigos):
    if no is None:
        return

    if no.char is not None:
        codigos[no.char] = codigo_atual or "0"
        return

    _gerar_codigos_recursivo(no.left, codigo_atual + "0", codigos)
    _gerar_codigos_recursivo(no.right, codigo_atual + "1", codigos)

def _gerar_codigos(no_raiz):
    codigos = {}
    _gerar_codigos_recursivo(no_raiz, "", codigos)
    return codigos

def _codificar_texto(texto, codigos):
    return "".join([codigos[char] for char in texto])

def compactar(texto):
    if not texto:
        return "", None

    frequencias = _calcular_frequencia(texto)
    arvore = _construir_arvore(frequencias)
    codigos = _gerar_codigos(arvore)
    texto_compactado = _codificar_texto(texto, codigos)
    
    return texto_compactado, arvore

def descompactar(texto_compactado, arvore_huffman):
    if not texto_compactado or arvore_huffman is None:
        return ""

    texto_decodificado = []
    no_atual = arvore_huffman
    
    if no_atual.left is None and no_atual.right is None:
        return no_atual.char * no_atual.freq

    for bit in texto_compactado:
        if bit == '0':
            no_atual = no_atual.left
        else:
            no_atual = no_atual.right
        
        if no_atual.char is not None:
            texto_decodificado.append(no_atual.char)
            no_atual = arvore_huffman
            
    return "".join(texto_decodificado)