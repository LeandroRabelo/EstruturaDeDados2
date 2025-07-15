# Projeto Logística Inteligente: Fase 2 - Análise de Algoritmos de Busca

Esta documentação descreve a arquitetura e a implementação da Fase 2 do projeto, focada na análise prática de três algoritmos de busca fundamentais: Busca Sequencial, Busca Binária e Rabin-Karp.

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
|-- Modulo1/
|   |-- buscas.py
|
|-- Dados/
    |-- clientes.py
    |-- pedidos.py
    |-- clientes.txt
    |-- pedidos.txt
```

As responsabilidades de cada componente são:

* **`Main.py`**: É o "cérebro" e a interface do projeto. Ele gerencia o menu principal, interage com o usuário, e orquestra as chamadas para os outros módulos. É responsável por criar a experiência interativa dos "minigames".

* **`Dados/`**: Esta pasta funciona como a camada de persistência e gerenciamento de dados.
    * `clientes.py` e `pedidos.py`: Contêm as funções para manipular os dados (carregar, salvar, cadastrar, remover), interagindo diretamente com os arquivos `.txt`. O `clientes.py` tem a responsabilidade extra de manter sua lista sempre ordenada por ID.
    * `clientes.txt` e `pedidos.txt`: Armazenam os dados brutos.

* **`Modulo1/`**: É a nossa "caixa de ferramentas" de algoritmos.
    * `buscas.py`: Contém as implementações puras e genéricas dos algoritmos de busca (Sequencial, Binária e Rabin-Karp), sem nenhuma dependência do resto do sistema.

* **`gerador_*.py`**: Scripts auxiliares criados para popular os arquivos `.txt` com uma grande massa de dados (Pode-se definir a quantidade de Clientes e Pedidos), permitindo testes de desempenho mais realistas.

## 2. Implementação e Integração dos Algoritmos

Cada algoritmo foi implementado em `Modulo1/buscas.py` e depois integrado ao `Main.py` como um "desafio" interativo com tema de logística.

### Busca Sequencial

* **Implementação:** A função `busca_sequencial` percorre uma lista item por item, do início ao fim. Para fins de análise, ela foi programada para retornar não só o item encontrado (ou `None`), mas também o **número de comparações** realizadas.
* **Integração (Desafio 1):** No minigame "Localização de Carga Urgente", a `Main.py`:
    1.  Carrega a lista de pedidos do arquivo `pedidos.txt`.
    2.  **Embaralha** a lista com `random.shuffle()` para simular um cenário realista de desordem.
    3.  Escolhe um pedido aleatório como alvo.
    4.  Chama a `busca_sequencial` e mede o tempo de execução.
    5.  Exibe um relatório com o resultado, o número de comparações e o tempo.

### Busca Binária

* **Implementação:** A função `busca_binaria` implementa o algoritmo de "dividir para conquistar". Ela exige que a lista esteja **pré-ordenada**. A cada passo, ela compara o alvo com o elemento do meio e descarta metade da lista, reduzindo drasticamente o espaço de busca. Ela também retorna o item e o número de comparações.
* **Integração (Desafio 2):** No minigame "Auditoria Rápida", a `Main.py`:
    1.  Carrega a lista **ordenada** de clientes do `clientes.txt`.
    2.  Escolhe um cliente alvo (propositalmente na segunda metade da lista para destacar a diferença).
    3.  Executa a `busca_binaria` para encontrar o alvo.
    4.  Executa também a `busca_sequencial` no mesmo alvo com a lista desordenada para fins de comparação.
    5.  Apresenta uma **tabela comparativa** mostrando as métricas de comparações e tempo de ambos os algoritmos.

### Busca Rabin-Karp

* **Implementação:** A função `busca_rabin_karp` implementa a busca de um padrão de texto (Lote) em um texto maior (Manifest). Sua eficiência vem do uso de *hashing*, convertendo o padrão e "janelas" do texto em números para comparações rápidas. A técnica de *rolling hash* evita o recálculo completo do hash a cada passo. A função retorna uma lista com os índices de **todas** as ocorrências encontradas.
* **Integração (Desafio 3):** No minigame "Rastreamento de Lote", a `Main.py`:
    1.  **Gera dinamicamente** um grande texto simulando um "manifesto de carga" com 100 itens(Pode-se aumentar o valor).
    2.  Insere um padrão de texto específico (ex: `LOTE-XR-734`) em posições predeterminadas.
    3.  Chama a `busca_rabin_karp` para obter a lista de índices das ocorrências.
    4.  Processa esses índices para apresentar um relatório amigável, informando a **linha e o caractere** de cada ocorrência encontrada.

## 3. Análise de Complexidade e Eficiência

A análise teórica da complexidade (Big O) foi claramente confirmada pelos resultados práticos observados nos desafios.

### Busca Sequencial

* **Complexidade Teórica:** **O(n) - Linear**. No pior caso, o tempo de execução cresce na mesma proporção que o número de itens (`n`) na lista.
* **Eficiência Observada:** No Desafio 1, supondo 1200 pedidos, vimos o número de comparações variar de 1 (melhor caso, o item é o primeiro) a 1200 (pior caso, o item é o último ou não existe). Isso confirma perfeitamente a natureza linear do algoritmo: para encontrar um item no final, foi preciso olhar todos os outros antes.

### Busca Binária

* **Complexidade Teórica:** **O(log n) - Logarítmica**. O tempo de execução cresce de forma muito lenta, pois o algoritmo descarta metade dos dados a cada passo.
* **Eficiência Observada:** No Desafio 2, a diferença foi gritante. Para encontrar um cliente em uma lista ordenada de 500, a Busca Binária precisou de no máximo **9 comparações** (pois `log₂(500) ≈ 8.96`). Em contraste, a Busca Sequencial precisou de centenas de comparações para o mesmo alvo. A tabela comparativa demonstrou na prática que a Busca Binária era dezenas de vezes mais eficiente, provando o imenso valor de se manter os dados organizados quando a busca é uma operação frequente.

### Busca Rabin-Karp

* **Complexidade Teórica:** Em média, **O(n + m)**, onde `n` é o tamanho do texto e `m` o do padrão. É linear em relação ao tamanho do texto, o que é muito eficiente. No pior caso (cenários com muitas colisões de hash), pode degradar para **O(nm)**.
* **Eficiência Observada:** O Desafio 3 demonstrou sua aplicação prática. A eficiência não foi medida em comparação com os outros algoritmos (pois o problema é diferente), mas em sua capacidade de realizar uma tarefa complexa (encontrar todas as ocorrências de um padrão) de forma rápida em um texto grande. A técnica de *rolling hash* permitiu que a varredura do manifesto de 100 itens fosse quase instantânea.