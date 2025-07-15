import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CLIENTES = os.path.join(DIRETORIO_ATUAL, 'clientes.txt')

def carregar_clientes():
    clientes = []
    try:
        with open(ARQUIVO_CLIENTES, 'r', encoding='utf-8') as f:
            for linha in f:
                if not linha.strip():
                    continue
                valores = linha.strip().split(',')
                cliente = {
                    'id': int(valores[0]),
                    'nome': valores[1],
                    'cidade': valores[2]
                }
                clientes.append(cliente)
    except FileNotFoundError:
        return []
    return clientes

def salvar_clientes(clientes):
    with open(ARQUIVO_CLIENTES, 'w', encoding='utf-8') as f:
        for cliente in clientes:
            f.write(f"{cliente['id']},{cliente['nome']},{cliente['cidade']}\n")

def cadastrar_cliente(nome, cidade):
    clientes = carregar_clientes()
    novo_id = 101 if not clientes else clientes[-1]['id'] + 1
    novo_cliente = {'id': novo_id, 'nome': nome, 'cidade': cidade}
    clientes.append(novo_cliente)
    salvar_clientes(clientes)
    print(f"✅ Cliente '{nome}' cadastrado com sucesso com o ID {novo_id}.")
    return novo_cliente

def remover_cliente(id_cliente_remover):
    try:
        id_alvo = int(id_cliente_remover)
    except ValueError:
        print(f"❌ ID inválido. Por favor, forneça um número.")
        return False

    clientes = carregar_clientes()
    clientes_atualizados = [cli for cli in clientes if cli['id'] != id_alvo]
    if len(clientes_atualizados) < len(clientes):
        salvar_clientes(clientes_atualizados)
        print(f"🗑️ Cliente com ID {id_alvo} foi removido com sucesso.")
        return True
    else:
        print(f"❌ Cliente com ID {id_alvo} não encontrado.")
        return False