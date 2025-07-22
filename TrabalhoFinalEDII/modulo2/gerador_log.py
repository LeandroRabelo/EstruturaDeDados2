import random
import os

def gerar_log(nome_arquivo="log_diario.txt", linhas=1000):
    
    caminho_deste_script = os.path.dirname(os.path.abspath(__file__))
    caminho_raiz_projeto = os.path.dirname(caminho_deste_script)
    caminho_final = os.path.join(caminho_raiz_projeto, "Dados", nome_arquivo)
    
    os.makedirs(os.path.dirname(caminho_final), exist_ok=True)

    veiculos = [f"VEIC-{1000+i}" for i in range(10)]
    status_opcoes = ["EM_TRANSITO"] * 7 + ["PARADA_ENTREGA"] * 2 + ["ALERTA_TRAFEGO"] * 1
    
    print(f"Gerando arquivo de log em '{caminho_final}'...")
    
    with open(caminho_final, 'w', encoding='utf-8') as f:
        for i in range(linhas):
            veiculo = random.choice(veiculos)
            status = random.choice(status_opcoes)
            timestamp = f"2025-07-21 21:{random.randint(10,59)}:{random.randint(10,59)}"
            f.write(f"[{timestamp}] [{veiculo}] [STATUS:{status}]\n")
            
    print("Arquivo de log gerado com sucesso!")