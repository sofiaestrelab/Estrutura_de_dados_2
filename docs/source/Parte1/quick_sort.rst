Quick Sort
-----------

O Quick Sort é um algoritmo de ordenação baseado na estratégia de **dividir para conquistar**, ele seleciona um elemento como **pivô**, particiona o vetor de modo que os elementos menores que o pivô fiquem à sua esquerda e os maiores fiquem à sua direita, e então aplica recursivamente o mesmo processo às duas partições resultantes.

.. note::

    O pivô funciona como uma âncora de comparação, ou seja, um elemento de referência escolhido para organizar o vetor.

**Exemplo**

 Array:

 8  3  5  1  7

 Escolhendo 7 como pivô:
 
 3 5 1 | 7 | 8

 Depois, as partes da esquerda e da direita são ordenadas recursivamente.

Exemplo de Pseudocódigo
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :linenos:

   def quick_sort(vetor, inicio, fim):

    # Verifica se ainda existem elementos para ordenar
    if inicio < fim:

        # Escolhe o último elemento como pivô
        posicao_pivo = particionar(vetor, inicio, fim)

        # Ordena a parte esquerda
        quick_sort(vetor, inicio, posicao_pivo - 1)

        # Ordena a parte direita
        quick_sort(vetor, posicao_pivo + 1, fim)


    def particionar(vetor, inicio, fim):

        # O último elemento será o pivô
        pivo = vetor[fim]
    
        # Índice da posição dos elementos menores
        i = inicio - 1

        # Percorre os elementos antes do pivô
        for j in range(inicio, fim):

        # Se o elemento for menor ou igual ao pivô
        if vetor[j] <= pivo:

            i = i + 1

            # Troca os elementos
            vetor[i], vetor[j] = vetor[j], vetor[i]

    # Coloca o pivô em sua posição correta
    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]

    # Retorna a posição final do pivô
    return i + 1

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

