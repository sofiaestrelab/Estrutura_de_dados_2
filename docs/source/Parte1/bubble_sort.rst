Bubble Sort
-----------

O Bubble Sort é um algoritmo de ordenação simples que organiza os elementos de uma lista comparando pares de elementos vizinhos e trocando-os de posição quando estão fora de ordem. 
A cada passagem completa pela lista, o maior (ou menor, dependendo do critério) elemento **flutua** gradualmente até sua posição correta, de forma semelhante a uma bolha subindo à superfície.

Exemplo Pseudocódigo
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :linenos:

   def bubble_sort(vetor):
       n = len(vetor)
       comparacoes = 0
       trocas = 0

       for i in range(n - 1):
           trocou = False

           for j in range(n - 1 - i):
               comparacoes += 1

               if vetor[j] > vetor[j + 1]:
                   vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                   trocas += 1
                   trocou = True

           # Se não houve troca nesta passagem, o vetor já está ordenado
           if not trocou:
               break

       return vetor, comparacoes, trocas


   # Exemplo de uso
   if __name__ == "__main__":
       dados = [5, 3, 8, 1, 9, 2]

       ordenado, num_comparacoes, num_trocas = bubble_sort(dados)

       print("Vetor ordenado:", ordenado)
       print("Número de comparações:", num_comparacoes)
       print("Número de trocas:", num_trocas)

Lógica de Ordenação
~~~~~~~~~~~~~~~~~~~~

- Compara o elemento na posição i com o elemento na posição i+1;
- Se estiverem fora de ordem, realiza a troca (swap);
- Repete esse processo até o fim do vetor, completando uma "passagem";
- Repete as passagens até que nenhuma troca seja necessária, indicando que o vetor está ordenado;
- Uma otimização comum é usar uma flag (ex: trocou = False) para encerrar o algoritmo antecipadamente caso uma passagem completa não realize nenhuma troca.

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
~~~~~~~~~~~~~~~~~~~~~~~~

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
