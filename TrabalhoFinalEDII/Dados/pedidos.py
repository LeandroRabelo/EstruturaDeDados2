import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PEDIDOS = os.path.join(DIRETORIO_ATUAL, 'pedidos.txt')

def carregar_pedidos():
    pedidos = []
    try:
        with open(ARQUIVO_PEDIDOS, 'r', encoding='utf-8') as f:
            for linha in f:
                if not linha.strip():
                    continue
                valores = linha.strip().split(',')
                pedido = {
                    'id': int(valores[0]),
                    'produto': valores[1],
                    'id_cliente': int(valores[2])
                }
                pedidos.append(pedido)
    except FileNotFoundError:
        return []
    return pedidos

def salvar_pedidos(pedidos):
    with open(ARQUIVO_PEDIDOS, 'w', encoding='utf-8') as f:
        for pedido in pedidos:
            f.write(f"{pedido['id']},{pedido['produto']},{pedido['id_cliente']}\n")

def cadastrar_pedido(produto, id_cliente):
    pedidos = carregar_pedidos()
    if not pedidos:
        novo_id = 9001
    else:
        id_maximo = max(p['id'] for p in pedidos)
        novo_id = id_maximo + 1
    novo_pedido = {
        'id': novo_id,
        'produto': produto,
        'id_cliente': int(id_cliente)
    }
    pedidos.append(novo_pedido)
    salvar_pedidos(pedidos)
    print(f"✅ Pedido para o produto '{produto}' cadastrado com o ID {novo_id}.")
    return novo_pedido

def remover_pedido(id_pedido_remover):
    try:
        id_alvo = int(id_pedido_remover)
    except ValueError:
        print(f"❌ ID inválido. Por favor, forneça um número.")
        return False
    pedidos = carregar_pedidos()
    pedidos_atualizados = [p for p in pedidos if p['id'] != id_alvo]
    if len(pedidos_atualizados) < len(pedidos):
        salvar_pedidos(pedidos_atualizados)
        print(f"🗑️ Pedido com ID {id_alvo} foi removido com sucesso.")
        return True
    else:
        print(f"❌ Pedido com ID {id_alvo} não encontrado.")
        return False

if __name__ == "__main__":
    print("--- Testando o módulo de pedidos ---")

    if os.path.exists(ARQUIVO_PEDIDOS):
        os.remove(ARQUIVO_PEDIDOS)

    print("\n1. Cadastrando pedidos...")
    cadastrar_pedido("Notebook Gamer", 101)
    cadastrar_pedido("Monitor 4K", 103)
    cadastrar_pedido("Teclado Mecanico", 102)

    print("\n2. Exibindo pedidos cadastrados...")
    lista_pedidos = carregar_pedidos()
    for p in lista_pedidos:
        print(f"   - {p}")

    print("\n3. Removendo o pedido com ID 9002...")
    remover_pedido(9002)

    print("\n4. Exibindo lista final de pedidos...")
    lista_final = carregar_pedidos()
    for p in lista_final:
        print(f"   - {p}")

    print("\n5. Cadastrando novo pedido...")
    cadastrar_pedido("Mouse sem Fio", 101)

    print("\n6. Exibindo lista após nova inserção...")
    lista_final = carregar_pedidos()
    for p in lista_final:
        print(f"   - {p}")
