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

Porque a busca sequencial percorre a matriz elemento por elemento, na ordem em que os loops aninhados a varrem (linha 0, coluna 0 primeiro). Como o algoritmo interrompe a busca assim que encontra o valor procurado (retorno antecipado), se o elemento está na primeira posição, basta uma única comparação para localizá-lo, independentemente do tamanho da matriz — como confirmado pelos resultados (sempre 1 comparação para busca no início, em todos os tamanhos testados).

**b)** O que acontece quando o elemento procurado não existe?

O algoritmo é obrigado a percorrer todos os elementos da matriz, linha por linha e coluna por coluna, sem nunca satisfazer a condição de parada antecipada. Isso significa que o número de comparações é sempre igual ao número total de elementos da matriz (m × n) — exatamente o mesmo comportamento observado na busca pelo valor no final da matriz, já que em ambos os casos é necessário varrer a matriz inteira (ou quase inteira).

**c)** Qual é o pior caso da busca sequencial?

O pior caso ocorre quando o valor procurado está na última posição da matriz (última linha, última coluna) ou quando o valor não existe. Em ambas as situações, o algoritmo realiza o número máximo possível de comparações: m × n, onde m é o número de linhas e n é o número de colunas.

**d)** Como o aumento das dimensões da matriz influencia a quantidade de operações?

No pior caso, o número de comparações cresce proporcionalmente ao total de elementos (m × n). Isso ficou evidente nos testes: ao aumentar as dimensões 10 vezes (de 10×10 para 100×100), o número de comparações aumentou 100 vezes — um crescimento quadrático, já que a matriz cresce em duas dimensões ao mesmo tempo.

**e)** Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?

A complexidade é O(m × n), pois o algoritmo pode precisar visitar todos os elementos da matriz uma vez, no pior caso. Quando a matriz é quadrada (m = n), isso equivale a O(n²).
