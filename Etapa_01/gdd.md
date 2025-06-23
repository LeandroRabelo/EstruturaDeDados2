# 📦 Gerenciador de Cargas e Entregas – Logística Inteligente

## 🎯 Tema do Projeto e Justificativa

**Tema:** Gerenciador de Cargas e Entregas – **“Logística Inteligente”**

**Justificativa:**  
Empresas de transporte e logística enfrentam desafios constantes na otimização de rotas, alocação de cargas, redução de custos e aumento da eficiência operacional. Este projeto visa desenvolver um sistema que simula um ambiente real de logística, permitindo que empresas planejem suas operações de forma inteligente e eficiente.

O sistema oferecerá cadastro de clientes, motoristas, veículos, centros de distribuição e pedidos. A partir dessas informações, será possível gerar rotas otimizadas, realizar alocação de cargas considerando restrições (peso, volume, prazos) e acompanhar o desempenho das operações.

---

## 🔧 Visão Geral das Funcionalidades

- Cadastro de clientes, motoristas, veículos, pedidos e centros de distribuição.
- Geração de rotas otimizadas entre centros e clientes.
- Alocação eficiente de cargas aos veículos com base em peso, volume e prioridade.
- Análise de custos, tempo e desempenho das entregas.
- Compressão de dados históricos e geração de relatórios.
- Sistema de busca rápida de informações (clientes, pedidos, rotas, motoristas).
- Simulação de cenários logísticos considerando restrições complexas.

---

## 📚 Integração da Ementa

| Tópico                            | Aplicação no Software                                                                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Teoria da Complexidade (NP)**    | Planejamento de múltiplas rotas com restrições de capacidade, janelas de entrega e menor custo (Caixeiro Viajante + Problema de Mochila).                 |
| **Busca Sequencial e Binária**     | Localização de clientes, motoristas, veículos e pedidos na base de dados.                                                                                 |
| **Busca em Texto / Hashing**       | Pesquisa rápida por código de rastreio, CEP, nome ou dados cadastrais. Hashing para otimização de acesso e localização de dados.                          |
| **Compressão (RLE, Huffman)**      | Compressão de dados históricos, relatórios e logs operacionais para reduzir espaço de armazenamento.                                                      |
| **Grafos**                         | Representação da malha urbana e rodoviária. Cálculo de menores caminhos (Dijkstra, A*), fluxo máximo, conectividade e acessibilidade entre locais.       |
| **Algoritmos Gulosos**             | Alocação de cargas nos veículos de forma rápida, priorizando peso, volume ou tempo de entrega (Mochila Fracionária, Escalonamento de Intervalos).         |
| **Programação Dinâmica**           | Otimização de cargas com restrições fixas (Mochila 0/1), planejamento de sequências de entrega com múltiplas restrições (tempo, custo, capacidade).       |

---

## 🗺️ Mapa dos Módulos e Algoritmos

| Módulo                    | Algoritmos Aplicados                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Gestão de Entregas**     | Busca sequencial/binária para pedidos, clientes, veículos. <br> Hashing para códigos de rastreio e CEP.                      |
| **Otimização de Rotas**    | Grafos: Dijkstra, A*, Busca em Largura para menor caminho. <br> Fluxo máximo para balanceamento entre centros e entregas.    |
| **Alocação de Cargas**     | Algoritmos Gulosos (Mochila Fracionária) para alocar rapidamente. <br> Programação Dinâmica (Mochila 0/1) para restrições fixas.|
| **Planejamento Global**    | Teoria da Complexidade (NP): Roteamento de veículos, Caixeiro Viajante com restrições (peso, tempo, custo).                   |
| **Análise de Dados**       | Compressão com Huffman e RLE dos dados históricos e relatórios. <br> Geração de relatórios e estatísticas.                   |
| **Busca e Gerenciamento**  | Busca em texto e hashing para consultas rápidas de clientes, motoristas, centros, rotas e pedidos.                           |

---

## 📊 Fluxo do Software (Exemplo)

1. **Cadastro:**  
   - Clientes, motoristas, veículos, centros de distribuição e pedidos.

2. **Recebimento de Pedidos:**  
   - Dados de origem, destino, peso, volume, prioridade.

3. **Otimização:**  
   - Geração de rotas com grafos (Dijkstra/A*).  
   - Definição de quais veículos realizarão quais entregas (Mochila, Gulosos, Programação Dinâmica).  
   - Planejamento geral considerando restrições (NP).

4. **Execução da Simulação:**  
   - Realização das entregas simuladas.  
   - Cálculo de tempo, custos, consumo e desempenho.

5. **Análise e Relatórios:**  
   - Visualização de históricos comprimidos, gráficos de desempenho, gargalos e sugestões de melhorias.

---

