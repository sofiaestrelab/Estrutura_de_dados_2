Experimento de Ordenação
========================

Programa de teste com Bubble e Quick Sort
------------------------------------------

.. code-block:: python
   :linenos:

   import random
   import time
   import copy

   def bubble_sort(vetor):
       v = vetor[:]
       n = len(v)
       comparacoes = 0
       trocas = 0
       for i in range(n - 1):
           trocou = False
           for j in range(n - 1 - i):
               comparacoes += 1
               if v[j] > v[j + 1]:
                   v[j], v[j + 1] = v[j + 1], v[j]
                   trocas += 1
                   trocou = True
           if not trocou:
               break
       return v, comparacoes, trocas


   def quick_sort(vetor):
       v = vetor[:]
       contadores = {"comparacoes": 0, "trocas": 0}

       def particionar(inicio, fim):
           pivo = v[fim]
           i = inicio - 1
           for j in range(inicio, fim):
               contadores["comparacoes"] += 1
               if v[j] <= pivo:
                   i += 1
                   v[i], v[j] = v[j], v[i]
                   contadores["trocas"] += 1
           v[i + 1], v[fim] = v[fim], v[i + 1]
           contadores["trocas"] += 1
           return i + 1

       def _quick_sort(inicio, fim):
           if inicio < fim:
               p = particionar(inicio, fim)
               _quick_sort(inicio, p - 1)
               _quick_sort(p + 1, fim)

       _quick_sort(0, len(v) - 1)
       return v, contadores["comparacoes"], contadores["trocas"]


   random.seed(42)
   tamanhos = [10, 20, 1000]
   resultados = []

   for n in tamanhos:
       array_original = [random.randint(1, 10000) for _ in range(n)]
       copia1 = copy.deepcopy(array_original)   # cópia para o Bubble Sort
       copia2 = copy.deepcopy(array_original)   # cópia para o Quick Sort

       inicio_b = time.perf_counter()
       ordenado_b, comp_b, troc_b = bubble_sort(copia1)
       tempo_b = time.perf_counter() - inicio_b

       inicio_q = time.perf_counter()
       ordenado_q, comp_q, troc_q = quick_sort(copia2)
       tempo_q = time.perf_counter() - inicio_q

       # Garante que ambos os algoritmos chegaram ao mesmo resultado
       assert ordenado_b == ordenado_q == sorted(array_original)

       resultados.append({
           "tamanho": n,
           "bubble_comp": comp_b, "bubble_troc": troc_b, "bubble_tempo": tempo_b,
           "quick_comp": comp_q, "quick_troc": troc_q, "quick_tempo": tempo_q,
       })

   for r in resultados:
       print(r)

Perguntas sobre o programa:
---------------------------

**a)** Qual algoritmo realizou menos operações para 10 elementos?

O Quick Sort, com 29 comparações e 19 trocas, contra 44 comparações e 19 trocas do Bubble Sort. As trocas ficaram empatadas, mas o Quick Sort precisou de menos comparações para chegar ao mesmo resultado.

**b)** O comportamento permaneceu igual para 20 elementos?

Sim, a tendência se manteve e ficou ainda mais evidente: o Bubble Sort saltou para 189 comparações e 84 trocas, enquanto o Quick Sort ficou em apenas 58 comparações e 43 trocas. A diferença entre os dois algoritmos aumentou proporcionalmente mais rápido para o Bubble Sort.

**c)** O que aconteceu quando o tamanho aumentou para 1.000 elementos?

A diferença se tornou drástica. O Bubble Sort realizou 499.122 comparações e 239.681 trocas, enquanto o Quick Sort realizou apenas 10.385 comparações e 5.850 movimentações

**d)** Qual algoritmo apresentou maior crescimento da quantidade de operações?

O Bubble Sort. Enquanto o array cresceu 100 vezes (de 10 para 1.000 elementos), suas comparações cresceram cerca de 11.000 vezes (de 44 para 499.122)

**e)** Os resultados experimentais são coerentes com as complexidades teóricas estudadas?

Sim. Para n=1.000, o Bubble Sort realizou 499.122 comparações, próximo de n² (1.000.000), e o Quick Sort realizou 10.385, próximo de n log₂n (≈9.970). Os dados confirmam as complexidades O(n²) e O(n log n).

**f)** Em qual situação você escolheria Bubble Sort?

Para fins didáticos, vetores muito pequenos ou já quase ordenados, onde seu melhor caso O(n) se aplica.

**g)** Em qual situação você escolheria Quick Sort?

Para aplicações reais com volumes de dados moderados a grandes, onde desempenho é prioridade.
