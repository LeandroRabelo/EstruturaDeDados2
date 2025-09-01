import json
import random
import os

def gerar_malha_logistica(num_cidades=15, num_rotas=30, arquivo_saida="malha_logistica.json"):
    cidades_brasil = [
        "Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza",
        "Brasilia", "Curitiba", "Manaus", "Recife", "Porto Alegre", "Goiania",
        "Belem", "Vitoria", "Florianopolis", "Cuiaba", "Campo Grande", "Natal",
        "Teresina", "Joao Pessoa", "Aracaju"
    ]

    num_cidades = min(num_cidades, len(cidades_brasil))
    locais = random.sample(cidades_brasil, num_cidades)
    
    rotas = []
    pares_criados = set()

    for i in range(len(locais) - 1):
        origem = locais[i]
        destino = locais[i+1]
        if tuple(sorted((origem, destino))) not in pares_criados:
            custo = random.randint(100, 2000)
            rotas.append({"origem": origem, "destino": destino, "custo": custo})
            pares_criados.add(tuple(sorted((origem, destino))))

    while len(rotas) < num_rotas:
        origem, destino = random.sample(locais, 2)
        if origem != destino and tuple(sorted((origem, destino))) not in pares_criados:
            custo = random.randint(100, 2000)
            rotas.append({"origem": origem, "destino": destino, "custo": custo})
            pares_criados.add(tuple(sorted((origem, destino))))

    malha = {
        "locais": locais,
        "rotas": rotas
    }

    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(diretorio_script, arquivo_saida)

    with open(caminho_completo, 'w', encoding='utf-8') as f:
        json.dump(malha, f, indent=4, ensure_ascii=False)

    print(f"Malha logística com {len(locais)} cidades e {len(rotas)} rotas gerada com sucesso!")
    print(f"Arquivo salvo em: {caminho_completo}")

if __name__ == "__main__": 
    print("Iniciando gerador de malha logística...")
    gerar_malha_logistica(num_cidades=15, num_rotas=30)