import os
import pickle
from . import compressao
from . import gerador_log

def menu_compressao():
    caminho_dados = os.path.dirname(os.path.abspath(__file__))
    caminho_raiz_projeto = os.path.dirname(caminho_dados)
    diretorio_saida = os.path.join(caminho_raiz_projeto, "Dados")
    
    os.makedirs(diretorio_saida, exist_ok=True)

    while True:
        print("\n--- Desafio: Arquivamento com Compressão Huffman ---")
        print(f"(Arquivos de entrada e saída estarão na pasta '{diretorio_saida}/')")
        print("1. Gerar arquivo de log de exemplo")
        print("2. Comprimir um arquivo")
        print("3. Descomprimir um arquivo")
        print("0. Voltar")
        
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            gerador_log.gerar_log()
            
        elif escolha == '2':
            arquivo_input_nome = input("Digite o nome do arquivo para comprimir (ex: log_diario.txt): ").strip()
            
            caminho_original = os.path.join(diretorio_saida, arquivo_input_nome)

            if not os.path.exists(caminho_original):
                print(f"ERRO: Arquivo '{caminho_original}' não encontrado.")
                continue

            with open(caminho_original, 'r', encoding='utf-8') as f:
                texto = f.read()

            texto_compactado, arvore = compressao.compactar(texto)
            
            nome_base = os.path.basename(caminho_original)
            
            arquivo_comprimido_nome = os.path.join(diretorio_saida, nome_base + ".huff")
            arvore_nome = os.path.join(diretorio_saida, nome_base + ".tree")

            with open(arquivo_comprimido_nome, 'w', encoding='utf-8') as f:
                f.write(texto_compactado)

            with open(arvore_nome, 'wb') as f:
                pickle.dump(arvore, f)

            print("\n--- RELATÓRIO DE COMPRESSÃO ---")
            print(f"Arquivo original: {caminho_original}")
            print(f"Arquivo comprimido salvo como: {arquivo_comprimido_nome}")
            print("---------------------------------")


        elif escolha == '3':
            arquivo_comprimido = input(f"Digite o nome do arquivo .huff para descomprimir: ").strip()

            caminho_completo_comprimido = os.path.join(diretorio_saida, arquivo_comprimido)
            caminho_completo_arvore = caminho_completo_comprimido.replace('.huff', '.tree')

            if not os.path.exists(caminho_completo_comprimido):
                print(f"ERRO: Arquivo não encontrado em '{diretorio_saida}/'.")
                continue

            with open(caminho_completo_comprimido, 'r', encoding='utf-8') as f:
                texto_compactado = f.read()
            with open(caminho_completo_arvore, 'rb') as f:
                arvore = pickle.load(f)

            texto_descompactado = compressao.descompactar(texto_compactado, arvore)
            
            nome_base_sem_ext = os.path.splitext(arquivo_comprimido)[0]
            arquivo_descomprimido_nome = f"{nome_base_sem_ext}_DESCOMPRIMIDO.txt"
            caminho_saida_descomprimido = os.path.join(diretorio_saida, arquivo_descomprimido_nome)

            with open(caminho_saida_descomprimido, "w", encoding="utf-8") as f:
                f.write(texto_descompactado)
            
            print("\n--- DESCOMPRESSÃO REALIZADA ---")
            print(f"Arquivo salvo com sucesso em: '{caminho_saida_descomprimido}'")
            print("---------------------------------")
            
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")