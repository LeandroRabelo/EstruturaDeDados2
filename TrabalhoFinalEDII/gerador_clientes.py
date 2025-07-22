import random
import os

NOMES = [
    "Miguel", "Arthur", "Gael", "Heitor", "Theo", "Davi", "Gabriel", "Bernardo", "Samuel", "João",
    "Helena", "Alice", "Laura", "Maria", "Valentina", "Sophia", "Isabella", "Heloísa", "Lívia", "Júlia",
    "Lucas", "Pedro", "Guilherme", "Enzo", "Rafael", "Matheus", "Nicolas", "Lorenzo", "Gustavo", "Felipe",
    "Manuela", "Luiza", "Cecília", "Elisa", "Yasmin", "Mariana", "Antonella", "Melissa", "Catarina", "Beatriz"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes",
    "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes", "Dias", "Barbosa", "Mendes", "Nunes"
]

CIDADES = [
    "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza", "Curitiba", "Manaus", "Recife",
    "Porto Alegre", "Brasília", "Goiânia", "Belém", "São Luís", "Maceió", "Campo Grande", "Teresina", "João Pessoa",
    "Natal", "Aracaju", "Cuiabá", "Florianópolis", "Vitória", "Campinas", "Santos", "Ribeirão Preto", "Uberlândia"
]

NUMERO_CLIENTES = 10000
ID_INICIAL = 101
DIRETORIO_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
NOME_ARQUIVO = os.path.join(DIRETORIO_DO_PROJETO,'Dados', 'clientes.txt')

def gerar_clientes():
    """Gera uma lista de clientes e salva em um arquivo .txt."""
    clientes = []
    print(f"Gerando {NUMERO_CLIENTES} clientes...")

    for i in range(NUMERO_CLIENTES):
        id_cliente = ID_INICIAL + i
        nome = random.choice(NOMES)
        sobrenome = random.choice(SOBRENOMES)
        nome_completo = f"{nome} {sobrenome}"
        cidade = random.choice(CIDADES)
        
        linha = f"{id_cliente},{nome_completo},{cidade}"
        clientes.append(linha)

    os.makedirs(os.path.dirname(NOME_ARQUIVO), exist_ok=True)
    
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        f.write("\n".join(clientes))

    print(f"✅ Arquivo '{NOME_ARQUIVO}' criado com sucesso com {len(clientes)} clientes.")
    print(f"   Os IDs vão de {ID_INICIAL} a {ID_INICIAL + NUMERO_CLIENTES - 1}.")

if __name__ == "__main__":
    gerar_clientes()