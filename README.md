# Projeto Logística Inteligente: Análise de Algoritmos

Esta documentação descreve a arquitetura e a implementação de um projeto educacional focado na análise prática de algoritmos fundamentais, divididos em módulos temáticos: Algoritmos de Busca, Otimização de Recursos (Compressão e Hashing) e Malha Logística (Grafos).

## 1. Arquitetura Geral

A arquitetura do projeto foi projetada para ser modular, separando as responsabilidades em diferentes componentes para garantir um código limpo, organizado e de fácil manutenção.

A estrutura de arquivos é a seguinte:

```
/LogisticaInteligente/
|
|-- Main.py
|-- gerador_clientes.py
|-- gerador_pedidos.py
|
|-- modulo1/
|   |-- buscas.py
|
|-- modulo2/
|   |-- compressao.py
|   |-- hashing.py
|   |-- desafios_mod2.py
|   |-- gerador_log.py
|
|-- modulo3/
|   |-- grafo.py
|   |-- algoritmos_grafo.py
|   |-- desafios_mod3.py
|
|-- modulo4/
|   |-- algoritmos_gulosos.py
|   |-- programacao_dinamica.py
|   |-- desafios_mod4.py
|
|-- Dados/
|   |-- clientes.py
|   |-- pedidos.py
|   |-- clientes.txt
|   |-- pedidos.txt
|   |-- malha_logistica.json
|   |-- gerador_clientes.py
|   |-- gerador_malha_logistica.py
|   |-- gerador_pedidos.py
|   |-- log_diario.txt
```

As responsabilidades de cada componente são:

* **`Main.py`**: É o "cérebro" e a interface do projeto. Ele gerencia o menu principal, interage com o usuário, e orquestra as chamadas para os outros módulos. É responsável por criar a experiência interativa dos "minigames".

* **`Dados/`**: Esta pasta funciona como a camada de persistência e gerenciamento de dados.
    * `clientes.py` e `pedidos.py`: Contêm as funções para manipular os dados (carregar, salvar, cadastrar, remover), interagindo diretamente com os arquivos `.txt`. O `clientes.py` tem a responsabilidade extra de manter sua lista sempre ordenada por ID.
    * Arquivos `.txt`, `.json`: Armazenam os dados brutos para os desafios.

* **`Modulo1/` (Buscas)**:
    * `buscas.py`: Contém as implementações puras e genéricas dos algoritmos de busca (Sequencial, Binária e Rabin-Karp).

* **`Modulo2/` (Otimização de Recursos)**:
    * `compressao.py` e `hashing.py`: Contêm as classes e funções puras dos algoritmos (Huffman, Tabela Hash).
    * `desafios_mod2.py`: Contém a camada de interface e gamificação, que dá um contexto de logística para os algoritmos.

* **`Modulo3/` (Grafos)**:
    * `grafo.py`: Implementa a classe `Grafo`, a estrutura de dados central que representa a malha logística, utilizando tanto lista de adjacências quanto matriz de adjacências.
    * `algoritmos_grafo.py`: Contém as implementações puras dos algoritmos de grafos (DFS, BFS, Dijkstra, Welch-Powell, Ordenação Topológica, Prim).
    * `desafios_mod3.py`: Orquestra os desafios interativos, aplicando os algoritmos de grafos a problemas de logística simulados.

* **`gerador_*.py`**: Scripts auxiliares criados para popular os arquivos de dados com uma grande massa de dados, permitindo testes de desempenho mais realistas.

## 2. Implementação e Integração dos Algoritmos

Cada algoritmo foi implementado de forma pura em seu respectivo módulo e depois integrado ao `main.py` ou a um menu de desafios como um "minigame" interativo com tema de logística.

### Busca Sequencial

* **Implementação:** A função `busca_sequencial` percorre uma lista item por item. Para fins de análise, ela retorna o item encontrado e o **número de comparações** realizadas.
* **Integração (Desafio 1):** No minigame "Localização de Carga Urgente", a lista de pedidos é **embaralhada** para simular desordem. O algoritmo então varre a lista para encontrar um ID específico, e um relatório de tempo e comparações é exibido.

### Busca Binária

* **Implementação:** A função `busca_binaria` implementa o "dividir para conquistar" em uma lista **pré-ordenada**, retornando o item e o número de comparações.
* **Integração (Desafio 2):** No minigame "Auditoria Rápida", a busca é feita em uma lista de clientes **ordenada**. Para destacar a eficiência, o desempenho da Busca Binária é comparado diretamente com a Busca Sequencial no mesmo alvo, apresentando uma **tabela comparativa** de métricas.

### Busca Rabin-Karp

* **Implementação:** A função `busca_rabin_karp` implementa a busca de um padrão de texto usando *hashing* e a técnica de *rolling hash* para evitar recálculos. Retorna os índices de **todas** as ocorrências.
* **Integração (Desafio 3):** No minigame "Rastreamento de Lote", um grande "manifesto de carga" é gerado dinamicamente. O algoritmo é usado para encontrar todas as menções de um lote específico (ex: `LOTE-XR-734`), e o resultado é apresentado de forma amigável, indicando **linha e caractere**.

### Compressão de Huffman

* **Implementação:** A função `compactar` calcula a frequência de caracteres, constrói a árvore de Huffman usando uma fila de prioridade, gera os códigos e serializa a árvore (essencial para a descompressão).
* **Integração (Desafio 1):** No minigame "O Pacto de Transmissão de Dados", o usuário pode comprimir um arquivo de log, visualizar a taxa de redução de dados e depois descompactá-lo para verificar a integridade do processo.

### Hashing

* **Implementação:** A classe `TabelaHash` implementa hashing com tratamento de colisões por **Encadeamento Separado**. Foram implementadas as funções de hash **Transformação da Raiz** e **Meio-Quadrado**.
* **Integração (Desafio 2):** No minigame "Central de Operações em Tempo Real", o usuário pode criar uma Tabela Hash, populá-la com veículos e simular uma busca de emergência por placa, medindo o tempo de acesso e analisando estatísticas como fator de carga e colisões.

### Busca em Profundidade (DFS)

* **Implementação:** A função `busca_em_profundidade` implementa uma busca recursiva que explora o grafo seguindo cada "ramo" até o fim antes de retroceder.
* **Integração (Desafio de Rota de Inspeção):** Simula um inspetor que precisa visitar o máximo de locais interconectados a partir de um ponto inicial, seguindo cada rota até o fim. O resultado mostra a **ordem de visita** da exploração.

### Busca em Largura (BFS)

* **Implementação:** A função `busca_em_largura` utiliza uma fila para explorar o grafo "camada por camada", descobrindo primeiro todos os vizinhos diretos, depois os vizinhos dos vizinhos, e assim por diante.
* **Integração (Análise de Capilaridade):** O desafio analisa a capilaridade da rede a partir de um centro de distribuição, mostrando todos os locais alcançáveis e a **quantos 'saltos' (rotas) de distância** eles estão, agrupados por nível de distância.

### Algoritmo de Dijkstra

* **Implementação:** A função `dijkstra` usa uma fila de prioridade para encontrar o caminho de menor custo (peso) entre dois vértices em um grafo ponderado.
* **Integração (Otimização de Rota de Entrega):** O desafio calcula a rota mais curta e de menor custo (em km) entre um ponto de partida e um destino, apresentando o **caminho ótimo** e seu **custo total**.

### Coloração de Grafo (Welch-Powell)

* **Implementação:** A função `welch_powell` implementa um algoritmo guloso para colorir os vértices de um grafo, onde os vértices com maior grau (mais conexões) são coloridos primeiro.
* **Integração (Alocação de Docks de Carga):** Simula um problema onde centros de distribuição vizinhos não podem receber entregas da mesma transportadora no mesmo dia. O algoritmo calcula o **número mínimo de "cores" (dias/transportadoras)** necessárias para operar sem conflitos.

### Ordenação Topológica (Kahn's Algorithm)

* **Implementação:** A função `ordenacao_topologica` implementa o algoritmo de Kahn, que utiliza os graus de entrada dos vértices para determinar uma ordenação linear de um grafo acíclico direcionado (DAG).
* **Integração (Sequenciamento de Carregamento):** O desafio cria um grafo de dependências para o carregamento de um contêiner (ex: itens pesados antes de frágeis). A ordenação topológica gera um **plano de carregamento passo a passo** que respeita todas as regras de precedência.

### Árvore Geradora Mínima (Prim)

* **Implementação:** A função `prim_mst` implementa o algoritmo de Prim, que constrói uma Árvore Geradora Mínima (MST) para um grafo ponderado, encontrando um subconjunto de arestas que conecta todos os vértices com o menor custo total possível.
* **Integração (Rede de Fibra Óptica):** Simula o planejamento de uma rede de fibra para conectar todos os centros de distribuição. O algoritmo calcula as conexões necessárias para formar uma rede de **custo total mínimo**, sem criar ciclos redundantes.

## 3. Análise de Complexidade e Eficiência

A análise teórica da complexidade (Big O) foi claramente confirmada pelos resultados práticos observados nos desafios.

### Busca Sequencial

* **Complexidade Teórica:** **O(n) - Linear**.
* **Eficiência Observada:** No Desafio 1, com 1200 pedidos, o número de comparações variou de 1 a 1200, confirmando a natureza linear: para encontrar um item no final, foi preciso olhar todos os outros antes.

### Busca Binária

* **Complexidade Teórica:** **O(log n) - Logarítmica**.
* **Eficiência Observada:** No Desafio 2, para uma lista de 500 clientes, a Busca Binária precisou de no máximo **9 comparações** (`log₂(500) ≈ 8.96`), enquanto a Sequencial precisou de centenas. A tabela comparativa provou o imenso valor de se manter os dados organizados.

### Busca Rabin-Karp

* **Complexidade Teórica:** Em média, **O(n + m)** (linear). No pior caso, **O(nm)**.
* **Eficiência Observada:** O Desafio 3 demonstrou sua capacidade de realizar uma tarefa complexa (encontrar todas as ocorrências de um padrão) de forma quase instantânea em um texto grande, graças à técnica de *rolling hash*.

### Compressão de Huffman

* **Complexidade Teórica:** **O(N + K log K)**, onde `N` é o tamanho do texto e `K` o número de caracteres únicos.
* **Eficiência Observada:** Em logs com textos repetitivos, a taxa de redução de dados superou 50%, representando uma economia direta de custos de armazenamento e de banda para transmissão de dados.

### Hashing

* **Complexidade Teórica:** Caso médio de **O(1)** (tempo constante) para busca, inserção e remoção. Pior caso de **O(M)**.
* **Eficiência Observada:** A busca por uma placa na "Central de Operações" é **instantânea**, com tempo medido em microssegundos. O resultado não sofre alteração perceptível, provando que o acesso não depende do tamanho da coleção de dados.

### Buscas em Grafo (DFS e BFS)

* **Complexidade Teórica:** **O(V + E)**, onde `V` é o número de vértices (locais) e `E` o de arestas (rotas). A performance é linear em relação ao tamanho do grafo.
* **Eficiência Observada:** As buscas nos desafios de inspeção e capilaridade são executadas de forma muito rápida, mesmo em um mapa com dezenas de locais e rotas, validando a eficiência do percorrimento completo do grafo.

### Dijkstra

* **Complexidade Teórica:** **O((V + E) log V)** com uma fila de prioridade.
* **Eficiência Observada:** No desafio de otimização de rota, o algoritmo calcula o caminho mais curto entre duas cidades em uma fração de segundo, demonstrando sua viabilidade para sistemas de navegação em tempo real que precisam de respostas rápidas.

### Algoritmos Gulosos (Welch-Powell, Prim)

* **Complexidade Teórica:** Welch-Powell é **O(V²)**, e Prim é **O(E log V)**.
* **Eficiência Observada:** Os desafios de alocação e da rede de fibra óptica mostram que, embora esses algoritmos possam ser mais complexos, eles fornecem soluções ótimas ou muito boas para problemas de otimização complexos (NP-difíceis) em um tempo de execução prático e eficiente. Eles encontram rapidamente uma solução viável sem precisar testar todas as combinações possíveis.