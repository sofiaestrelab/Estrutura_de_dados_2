Investigação de Buscas em Matrizes
===================================

Algoritmo de Busca Sequencial
-----------------------------

.. code-block:: python
   :linenos:

   def busca_sequencial_matriz(matriz, valor_procurado):
       comparacoes = 0
       linhas = len(matriz)
       colunas = len(matriz[0]) if linhas > 0 else 0

       for i in range(linhas):
           for j in range(colunas):
               comparacoes += 1
               if matriz[i][j] == valor_procurado:
                   return {
                       "encontrado": True,
                       "linha": i,
                       "coluna": j,
                       "comparacoes": comparacoes
                   }

       return {
           "encontrado": False,
           "linha": None,
           "coluna": None,
           "comparacoes": comparacoes
       }

   def gerar_matriz(linhas, colunas):
       # Preenche a matriz com valores sequenciais de 1 até linhas*colunas
       return [[i * colunas + j + 1 for j in range(colunas)] for i in range(linhas)]

   def executar_experimento(linhas, colunas):
       matriz = gerar_matriz(linhas, colunas)
       total_elementos = linhas * colunas

       valor_inicio = matriz[0][0]                     # primeiro elemento
       valor_fim = matriz[linhas - 1][colunas - 1]    # último elemento
       valor_inexistente = total_elementos + 1000     # garantidamente fora da matriz

       resultado_inicio = busca_sequencial_matriz(matriz, valor_inicio)
       resultado_fim = busca_sequencial_matriz(matriz, valor_fim)
       resultado_inexistente = busca_sequencial_matriz(matriz, valor_inexistente)

       return {
           "dimensao": f"{linhas}x{colunas}",
           "elementos": total_elementos,
           "inicio": resultado_inicio,
           "fim": resultado_fim,
           "inexistente": resultado_inexistente,
       }

   dimensoes = [(2, 2), (10, 10), (100, 100)]
   resultados = [executar_experimento(l, c) for l, c in dimensoes]

   for r in resultados:
       print(r)

Resultados Matrizes
--------------------

.. note::
  Os números deverão representar a quantidade de comparações realizadas.

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1
   :class: quebra-linha-dois-quatro

   * - Matriz
     - Nº de elementos
     - Busca no início
     - Busca no final
     - Valor inexistente
   * - 2 × 2
     - 4
     - 1
     - 4
     - 4
   * - 10 × 10
     - 100
     - 1
     - 100
     - 100
   * - 100 × 100
     - 10.000
     - 1
     - 10.000
     - 10.00

Perguntas sobre o programa:
---------------------------

**a)** Por que encontrar um elemento no início exige menos operações?

Porque a busca começa pela primeira posição da matriz. Quando o valor procurado está no início, ele é encontrado na primeira comparação e o algoritmo encerra a busca. Por isso, são necessárias apenas 1 comparação.

**b)** O que acontece quando o elemento procurado não existe?

Quando o valor não existe na matriz, o algoritmo precisa verificar todas as posições para confirmar que ele não está presente. Assim, o número de comparações será igual ao número total de elementos da matriz.

**c)** Qual é o pior caso da busca sequencial?

O pior caso ocorre quando o valor está na última posição da matriz ou quando ele não existe. Nessas situações, todas as posições precisam ser verificadas.

**d)** Como o aumento das dimensões da matriz influencia a quantidade de operações?

Quanto maior for a matriz, maior será a quantidade de elementos que poderão precisar ser analisados.

Por exemplo:

- Matriz 2 × 2 → 4 elementos;
- Matriz 10 × 10 → 100 elementos;
- Matriz 100 × 100 → 10.000 elementos.

Dessa forma, o número de operações aumenta conforme aumenta a quantidade de elementos da matriz.

**e)** Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?

A complexidade é O(m × n), pois o algoritmo pode precisar visitar todos os elementos da matriz uma vez, no pior caso. Quando a matriz é quadrada (m = n), isso equivale a O(n²).
