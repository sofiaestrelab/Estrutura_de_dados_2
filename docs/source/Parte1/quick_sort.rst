Quick Sort
-----------

O Quick Sort é um algoritmo de ordenação baseado na estratégia de **dividir para conquistar**, ele seleciona um elemento como **pivô**, particiona o vetor de modo que os elementos menores que o pivô fiquem à sua esquerda e os maiores fiquem à sua direita, e então aplica recursivamente o mesmo processo às duas partições resultantes.

.. note::

    O pivô funciona como uma âncora de comparação, ou seja, um elemento de referência escolhido para organizar o vetor.

Exemplo de Pseudocódigo
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :linenos:

   def quick_sort(vetor, inicio=0, fim=None, comparacoes=0, trocas=0):
       if fim is None:
           fim = len(vetor) - 1

       if inicio < fim:
           # Particiona o vetor e obtém a posição final do pivô
           posicao_pivo, comparacoes, trocas = particionar(vetor, inicio, fim, comparacoes, trocas)

           # Ordena recursivamente os elementos antes e depois do pivô
           _, comparacoes, trocas = quick_sort(vetor, inicio, posicao_pivo - 1, comparacoes, trocas)
           _, comparacoes, trocas = quick_sort(vetor, posicao_pivo + 1, fim, comparacoes, trocas)

       return vetor, comparacoes, trocas


   def particionar(vetor, inicio, fim, comparacoes, trocas):
       pivo = vetor[fim]  # Escolhe o último elemento como pivô
       i = inicio - 1      # Índice do menor elemento

       for j in range(inicio, fim):
           comparacoes += 1

           if vetor[j] <= pivo:
               i += 1
               vetor[i], vetor[j] = vetor[j], vetor[i]
               trocas += 1

       # Coloca o pivô na posição correta
       vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
       trocas += 1

       return i + 1, comparacoes, trocas


   # Exemplo de uso
   if __name__ == "__main__":
       dados = [5, 3, 8, 1, 9, 2]

       ordenado, num_comparacoes, num_trocas = quick_sort(dados)

       print("Vetor ordenado:", ordenado)
       print("Número de comparações:", num_comparacoes)
       print("Número de trocas:", num_trocas)

Lógica de Ordenação
~~~~~~~~~~~~~~~~~~~~

- Escolhe um elemento do vetor como pivô (pode ser o primeiro, o último, o elemento central ou um valor aleatório, dependendo da estratégia adotada);
- Particiona o vetor: percorre os elementos, colocando os menores que o pivô de um lado e os maiores do outro;
- Posiciona o pivô em sua posição final correta (entre as duas partições);
- Aplica recursivamente o mesmo processo às sublistas à esquerda e à direita do pivô;
- A recursão termina quando as sublistas possuem 0 ou 1 elemento, que já estão, por definição, ordenadas.

Complexidade Melhor Caso
~~~~~~~~~~~~~~~~~~~~~~~~

**O(n log n)** — ocorre quando o pivô escolhido divide consistentemente o vetor em duas partições de tamanhos aproximadamente iguais a cada partição.

Complexidade Médio Caso
~~~~~~~~~~~~~~~~~~~~~~~~

**O(n log n)** — na prática, mesmo com escolhas de pivô não ideais, o algoritmo tende a se comportar de forma próxima ao caso ideal, o que o torna, em média, um dos algoritmos de ordenação mais rápidos.

Complexidade Pior Caso
~~~~~~~~~~~~~~~~~~~~~~

**O(n²)** — ocorre quando o pivô escolhido é sistematicamente o menor ou o maior elemento da partição (por exemplo, ao ordenar um vetor já ordenado usando sempre o primeiro elemento como pivô), gerando partições extremamente desbalanceadas.

Vantagens e Limitações:
~~~~~~~~~~~~~~~~~~~~~~

Vantagens:
  - Excelente desempenho médio, geralmente superior a outros algoritmos O(n log n) na prática, devido a fatores como localidade de referência e baixo overhead por comparação;
  - Ordenação in-place (não exige memória auxiliar significativa, ao contrário do Merge Sort);
  - Amplamente utilizado e otimizado em bibliotecas padrão de diversas linguagens.

Limitações:
   - O pior caso é O(n²), o que pode ser problemático em cenários adversos ou com entradas específicas;
   - Não é estável em sua implementação clássica (a ordem relativa de elementos iguais pode não ser preservada);
   - O desempenho depende fortemente da estratégia de escolha do pivô;
   - É sensível a estouro de pilha (stack overflow) em recursões muito profundas, no caso de vetores muito grandes e mal particionados.

Sobre o uso do algoritmo
~~~~~~~~~~~~~~~~~~~~~~~~

Quando usar:
   - Grandes volumes de dados, onde o desempenho médio O(n log n) é vantajoso;
   - Aplicações de propósito geral, sendo inclusive a base de implementações padrão de ordenação em diversas linguagens;
   - Cenários em que o uso eficiente de memória é importante (ordenação in-place).

Quando não usar:
   - Aplicações que exigem garantia de desempenho no pior caso (nesses casos, Merge Sort ou Heap Sort, que garantem O(n log n) sempre, são mais indicados);
   - Situações em que a estabilidade da ordenação é um requisito obrigatório;
   - Entradas já ordenadas ou quase ordenadas, quando a estratégia de escolha do pivô não é adequada (ex: sempre escolher o primeiro elemento), podendo degradar o desempenho para O(n²).   

