import os
import pickle
from . import compressao
from . import gerador_log
import random
import time
from .hashing import TabelaHash

FROTA_EXEMPLO = [
    {"placa": "RTM-2A33", "motorista": "Ana Júlia", "modelo": "Scania R450"},
    {"placa": "BPW-8J21", "motorista": "Bruno Costa", "modelo": "Volvo FH 540"},
    {"placa": "AXL-1C55", "motorista": "Carlos Souza", "modelo": "DAF XF"},
    {"placa": "FGH-9B78", "motorista": "Daniela Lima", "modelo": "Mercedes-Benz Actros"},
    {"placa": "JKL-5D32", "motorista": "Eduardo Reis", "modelo": "Iveco Stralis"},
    {"placa": "MNP-0E99", "motorista": "Fernanda Alves", "modelo": "MAN TGX"},
    {"placa": "QRS-4F17", "motorista": "Gustavo Borges", "modelo": "Scania S500"},
    {"placa": "TUV-7G88", "motorista": "Helena Martins", "modelo": "Volvo VM 270"},
    {"placa": "WXY-3H45", "motorista": "Isabela Rocha", "modelo": "Ford Cargo"},
    {"placa": "ZBC-6K01", "motorista": "João Victor", "modelo": "VW Constellation"},
    {"placa": "GHT-1L94", "motorista": "Kensley Alves", "modelo": "Mercedes-Benz Axor"},
    {"placa": "UJM-8M52", "motorista": "Leandro Silva", "modelo": "Scania G420"},
    {"placa": "POL-3N19", "motorista": "Lívia Andrade", "modelo": "Volvo FMX"},
    {"placa": "QWE-0P87", "motorista": "Luiz Henrique", "modelo": "Iveco Tector"},
    {"placa": "ASD-6R45", "motorista": "Mariana Souto", "modelo": "VW Meteor"},
    {"placa": "ZXC-2S23", "motorista": "Mateus Nunes", "modelo": "DAF CF"},
    {"placa": "VBN-7T11", "motorista": "Nicolas Pereira", "modelo": "Mercedes-Benz Atego"},
    {"placa": "YUI-4U89", "motorista": "Otávio Martins", "modelo": "Scania P310"},
    {"placa": "HJK-9V67", "motorista": "Rafael Gomes", "modelo": "Volvo VM 330"},
    {"placa": "ERT-5W34", "motorista": "Rian Souza", "modelo": "Iveco Daily"},
    {"placa": "DFG-1X12", "motorista": "Sophia Lima", "modelo": "Ford F-4000"},
    {"placa": "CVB-8Y90", "motorista": "Thomaz Ribeiro", "modelo": "VW Delivery"},
    {"placa": "NMK-3Z78", "motorista": "Túlio Ferreira", "modelo": "Mercedes-Benz Sprinter"},
    {"placa": "LPQ-0A56", "motorista": "Valentina Dias", "modelo": "Renault Master"},
    {"placa": "WSA-6B34", "motorista": "Arthur Barbosa", "modelo": "Fiat Ducato"},
    {"placa": "FRE-2C12", "motorista": "Beatriz Mendes", "modelo": "Peugeot Boxer"},
    {"placa": "GTF-7D90", "motorista": "Cecília Almeida", "modelo": "Citroën Jumper"},
    {"placa": "HYG-3E78", "motorista": "Davi Carvalho", "modelo": "Hyundai HR"},
    {"placa": "JHY-8F56", "motorista": "Elisa Costa", "modelo": "Kia Bongo"},
    {"placa": "KJU-4G34", "motorista": "Enzo Rodrigues", "modelo": "Scania R540"},
    {"placa": "LKI-9H12", "motorista": "Felipe Santos", "modelo": "Volvo FH 460"},
    {"placa": "MJN-1I90", "motorista": "Gabriel Oliveira", "modelo": "DAF XF 530"},
    {"placa": "NHB-6J78", "motorista": "Gael Ferreira", "modelo": "Mercedes-Benz Actros 2651"},
    {"placa": "BGT-2K56", "motorista": "Guilherme Alves", "modelo": "Iveco Hi-Way"},
    {"placa": "VFR-7L34", "motorista": "Heitor Pereira", "modelo": "MAN TGX 29.480"},
    {"placa": "CDE-3M12", "motorista": "Heloísa Lima", "modelo": "Scania S540"},
    {"placa": "XSW-8N90", "motorista": "Isabella Gomes", "modelo": "Volvo VM 220"},
    {"placa": "QAZ-4P78", "motorista": "Júlia Ribeiro", "modelo": "Ford Cargo 1119"},
    {"placa": "EDC-9R56", "motorista": "Laura Martins", "modelo": "VW Constellation 24.280"},
    {"placa": "RFV-5S34", "motorista": "Leonardo Carvalho", "modelo": "Mercedes-Benz Accelo"},
    {"placa": "TGB-1T12", "motorista": "Lorenzo Almeida", "modelo": "Iveco Tector 9-190"},
    {"placa": "YHN-6U90", "motorista": "Lucas Lopes", "modelo": "DAF CF 85"},
    {"placa": "UJM-2V78", "motorista": "Luiza Dias", "modelo": "Scania P360"},
    {"placa": "IKL-7W56", "motorista": "Manuela Barbosa", "modelo": "Volvo FMX 500"},
    {"placa": "OKM-3X34", "motorista": "Maria Mendes", "modelo": "Ford F-350"},
    {"placa": "PJU-8Y12", "motorista": "Matheus Nunes", "modelo": "VW Delivery Express"},
    {"placa": "NHY-4Z90", "motorista": "Melissa Rodrigues", "modelo": "Mercedes-Benz Atego 2426"},
    {"placa": "BGT-9A78", "motorista": "Miguel Santos", "modelo": "Scania R410"},
    {"placa": "FVB-5B56", "motorista": "Pedro Oliveira", "modelo": "Volvo VM 270 6x2"},
    {"placa": "CRF-1C34", "motorista": "Rafael Souza", "modelo": "Iveco Daily 35-150"}
]

def menu_compressao():
    """Interface de usuário gamificada para o desafio de compressão de Huffman."""
    
    # Lógica de caminho absoluto para definir a pasta 'Dados' como o local de trabalho
    caminho_deste_script = os.path.dirname(os.path.abspath(__file__))
    caminho_raiz_projeto = os.path.dirname(caminho_deste_script)
    diretorio_dados = os.path.join(caminho_raiz_projeto, "Dados")
    
    os.makedirs(diretorio_dados, exist_ok=True)

    while True:
        print("\n" + "="*60)
        print("--- DESAFIO 1: O PACTO DE TRANSMISSÃO DE DADOS (HUFFMAN) ---")
        print("="*60)
        print("\n[CENA]: A nova frota de veículos envia logs de status a cada minuto.")
        print("        O custo com a transmissão de dados está saindo do controle.")
        print("\n[MISSÃO]: Usar a compressão de Huffman para 'encolher' os pacotes de dados")
        print("        antes de serem enviados, economizando custos e banda.")
        
        print("\n--- Central de Comunicação ---")
        print(f"(Os pacotes de dados (logs) estão na pasta '{diretorio_dados}/')")
        print("1. Simular recebimento de novo Pacote de Dados (Gerar Log)")
        print("2. Comprimir Pacote de Dados para Transmissão")
        print("3. Ler Pacote de Dados Comprimido (Descomprimir)")
        print("0. Voltar")
        
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            gerador_log.gerar_log()
            input('\nPressione Enter para continuar...')
            
        elif escolha == '2':
            arquivo_input_nome = input("Digite o nome do pacote de dados a comprimir (ex: log_diario.txt): ").strip()
            
            caminho_original = os.path.join(diretorio_dados, arquivo_input_nome)

            if not os.path.exists(caminho_original):
                print(f"ERRO: Pacote de dados '{caminho_original}' não encontrado.")
                continue

            with open(caminho_original, 'r', encoding='utf-8') as f:
                texto = f.read()

            print("\n[SISTEMA]: Analisando frequências de caracteres e construindo a Árvore de Huffman...")
            time.sleep(1)
            texto_compactado, arvore = compressao.compactar(texto)
            print("[SISTEMA]: Compressão finalizada.")
            
            nome_base = os.path.basename(caminho_original)
            arquivo_comprimido_nome = os.path.join(diretorio_dados, nome_base + ".huff")
            arvore_nome = os.path.join(diretorio_dados, nome_base + ".tree")

            with open(arquivo_comprimido_nome, 'w', encoding='utf-8') as f: f.write(texto_compactado)
            with open(arvore_nome, 'wb') as f: pickle.dump(arvore, f)

            tamanho_original_bytes = os.path.getsize(caminho_original)
            tamanho_comprimido_bits = len(texto_compactado)
            tamanho_original_bits = tamanho_original_bytes * 8
            
            if tamanho_original_bits == 0: reducao = 0
            else: reducao = 100 * (1 - (tamanho_comprimido_bits / tamanho_original_bits))

            print("\n--- RELATÓRIO DO PACTO DE TRANSMISSÃO ---")
            print(f"Tamanho Original do Pacote: {tamanho_original_bytes / 1024:.2f} KB")
            print(f"Tamanho Após Compressão:   {tamanho_comprimido_bits / 8 / 1024:.2f} KB (Teórico)")
            print(f"Taxa de Redução de Dados:   {reducao:.2f}%")
            print("-----------------------------------------")
            print(f"[CONCLUSÃO]: O pacote de dados agora está {reducao:.2f}% menor!")
            print("             Transmissão mais rápida, barata e confiável.")

            input('\nPressione Enter para continuar...')
            
        elif escolha == '3':
            arquivo_comprimido = input(f"Digite o nome do pacote .huff para ler: ").strip()
            
            caminho_completo_comprimido = os.path.join(diretorio_dados, arquivo_comprimido)
            caminho_completo_arvore = caminho_completo_comprimido.replace('.huff', '.tree')

            if not os.path.exists(caminho_completo_comprimido):
                print(f"ERRO: Pacote não encontrado em '{diretorio_dados}/'.")
                continue

            print("\n[SISTEMA]: Lendo pacote comprimido e reconstruindo dados com a Árvore de Huffman...")
            time.sleep(1)
            with open(caminho_completo_comprimido, 'r') as f: texto_compactado = f.read()
            with open(caminho_completo_arvore, 'rb') as f: arvore = pickle.load(f)

            texto_descompactado = compressao.descompactar(texto_compactado, arvore)

            nome_base_sem_ext = os.path.splitext(arquivo_comprimido)[0]
            arquivo_descomprimido_nome = f"{nome_base_sem_ext}_DESCOMPRIMIDO.txt"
            caminho_saida_descomprimido = os.path.join(diretorio_dados, arquivo_descomprimido_nome)

            with open(caminho_saida_descomprimido, "w", encoding="utf-8") as f: f.write(texto_descompactado)
            
            print("\n--- LEITURA DO PACOTE CONCLUÍDA ---")
            print(f"✅ Dados 100% restaurados e salvos em: '{caminho_saida_descomprimido}'")
            print("------------------------------------")
            
            input('\nPressione Enter para continuar...')
            
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")
            
def menu_hashing():
    tabela_hash = None

    while True:
        print("\n" + "="*60)
        print("--- DESAFIO 2: CENTRAL DE OPERAÇÕES EM TEMPO REAL (HASHING) ---")
        print("="*60)

        if tabela_hash is None:
            print("\n[CENA]: O Centro de Controle Operacional (CCO) precisa de acesso instantâneo")
            print("        aos dados da frota para emergências e fiscalizações.")
            print("\n[MISSÃO]: Construir e configurar o 'Índice de Acesso Rápido' para a frota.")
            print("\n1. Iniciar e configurar o Índice de Acesso Rápido (Tabela Hash)")
        else:
            print("\n[SISTEMA]: Índice de Acesso Rápido ATIVO.")
            print("1. Cadastrar novo veículo no Índice (Manual)")
            print("2. Popular Índice com Frota de 50 Veículos (Automático)")
            print("3. EMERGÊNCIA: Consultar veículo em Posto de Fiscalização")
            print("4. Descomissionar veículo do Índice (Remover)")
            print("5. Analisar Eficiência do Índice (Estatísticas)")
            print("6. Reiniciar Índice")

        print("0. Voltar ao Menu de Otimização")

        escolha = input("Escolha uma opção: ").strip()

        if tabela_hash is None:
            if escolha == '1':
                try:
                    tamanho = int(input("Digite o tamanho do Índice (ex: 128 posições): "))
                    print("\nModelos de Organização (Funções de Hash) para Leandro:")
                    print(" a) Transformação da Raiz")
                    print(" b) Meio-Quadrado")
                    func_escolha = input("Escolha o modelo (a/b): ").lower()
                    
                    if func_escolha == 'a': nome_func = "transformacao_raiz"
                    elif func_escolha == 'b': nome_func = "meio_quadrado"
                    else:
                        print("Opção de modelo inválida.")
                        continue
                    
                    tabela_hash = TabelaHash(tamanho, nome_func)
                    print(f"\n✅ Índice de Acesso Rápido configurado com {tamanho} posições usando '{nome_func}'!")
                    input('\nPressione Enter para continuar...')
                except ValueError:
                    print("Erro: O tamanho deve ser um número inteiro.")
            elif escolha == '0':
                break
            else:
                print("Opção inválida.")
        else:
            if escolha == '1':
                placa = input("Digite a PLACA do veículo (ex: ABC-1234): ").upper()
                motorista = input("Digite o NOME do motorista: ")
                modelo = input("Digite o MODELO do veículo: ")
                valor = {"motorista": motorista, "modelo": modelo, "placa": placa}
                tabela_hash.inserir(placa, valor)
                print(f"Veículo com placa '{placa}' cadastrado no Índice.")
                input('\nPressione Enter para continuar...')

            elif escolha == '2':
                print("\n[SISTEMA]: Populando o Índice com a frota de 50 veículos...")
                count = 0
                for veiculo in FROTA_EXEMPLO:
                    tabela_hash.inserir(veiculo["placa"], veiculo)
                    count += 1
                print(f"\n✅ Índice populado com sucesso com {count} veículos!")

            elif escolha == '3':
                veiculos_cadastrados = [item[0] for balde in tabela_hash.tabela for item in balde]
                if not veiculos_cadastrados:
                    print("\n[AVISO]: Nenhum veículo cadastrado para simular a emergência.")
                    continue
                placa_alvo = random.choice(veiculos_cadastrados)
                print("\n[ALERTA URGENTE]: O telefone toca! Um veículo foi parado na fiscalização!")
                time.sleep(1.5)
                print(f"[OPERADOR]: 'Preciso dos dados do veículo de placa {placa_alvo} IMEDIATAMENTE!'")
                time.sleep(1)
                input("\nPressione Enter para usar o Índice de Acesso Rápido...")
                t_inicio = time.perf_counter()
                resultado = tabela_hash.buscar(placa_alvo)
                t_fim = time.perf_counter()
                tempo_total = t_fim - t_inicio
                print("\n--- ✅ Consulta Realizada ---")
                print(f"Placa: {resultado['placa']}")
                print(f"Motorista: {resultado['motorista']}")
                print(f"Modelo: {resultado['modelo']}")
                print(f"\n⏱️ Tempo de busca no Índice: {tempo_total:.8f} segundos.")
                input('\nPressione Enter para continuar...')

            elif escolha == '4':
                placa = input("Digite a placa do veículo a ser descomissionado: ").upper()
                if tabela_hash.remover(placa):
                    print(f"Veículo '{placa}' removido do Índice.")
                else:
                    print(f"Veículo '{placa}' não encontrado no Índice.")
                    input('\nPressione Enter para continuar...')

            elif escolha == '5':
                tabela_hash.exibir_estatisticas()

            elif escolha == '6':
                tabela_hash = None
                print("Índice de Acesso Rápido reiniciado.")
                input('\nPressione Enter para continuar...')
            
            elif escolha == '0':
                break
            else:
                print("Opção inválida.")