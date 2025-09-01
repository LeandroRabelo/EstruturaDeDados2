import random
import os

PRODUTOS = [
    "Smartphone Z10", "Notebook Pro S", "Cadeira Gamer Confort", "Monitor UltraWide 34", "Teclado Luminoso",
    "Mouse Vertical Ergonômico", "Fone com Cancelamento de Ruído", "Webcam Full HD", "Impressora a Laser", "Tablet 11 polegadas",
    "Smartwatch Fit Pro", "Kit de Chaves de Precisão", "Panela de Arroz Elétrica", "Máquina de Café em Cápsulas", "Livro: Estruturas de Dados",
    "Sapato Social de Couro", "Mochila Executiva Antifurto", "SSD Externo 2TB", "Lâmpada Inteligente Wi-Fi", "Câmera de Vigilância IP",
    "Climatizador de Ar", "Aspirador de Pó Robô", "Roteador Mesh 3-pack", "Caixa de Som Bluetooth Xtreme", "Filtro de Água de Torneira",
    "Mesa Digitalizadora", "Microfone Condensador USB", "Cadeira de Escritório Tela Mesh", "Projetor Portátil LED", "Batedeira Planetária"
]

NUMERO_PEDIDOS = 1200
ID_PEDIDO_INICIAL = 9001

ID_CLIENTE_MIN = 101
ID_CLIENTE_MAX = 600
DIRETORIO_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO = os.path.join(DIRETORIO_DO_PROJETO, 'pedidos.txt')

def gerar_pedidos():
    """Gera uma lista de pedidos e salva em um arquivo .txt."""
    pedidos = []
    print(f"Gerando {NUMERO_PEDIDOS} pedidos...")

    for i in range(NUMERO_PEDIDOS):
        id_pedido = ID_PEDIDO_INICIAL + i
        produto = random.choice(PRODUTOS)
        
        id_cliente = random.randint(ID_CLIENTE_MIN, ID_CLIENTE_MAX)
        
        linha = f"{id_pedido},{produto},{id_cliente}"
        pedidos.append(linha)

    os.makedirs(os.path.dirname(NOME_ARQUIVO), exist_ok=True)
    
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        f.write("\n".join(pedidos))

    print(f"✅ Arquivo '{NOME_ARQUIVO}' criado com sucesso com {len(pedidos)} pedidos.")
    print(f"   Os IDs dos pedidos vão de {ID_PEDIDO_INICIAL} a {ID_PEDIDO_INICIAL + NUMERO_PEDIDOS - 1}.")

if __name__ == "__main__":
    gerar_pedidos()