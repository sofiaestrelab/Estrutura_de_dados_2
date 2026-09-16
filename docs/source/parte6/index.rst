Análise e Conclusão
====================

Ao longo desta atividade, foram implementados e analisados diferentes
algoritmos e estruturas de dados, incluindo os métodos de ordenação Bubble
Sort e Quick Sort, a busca sequencial em matrizes, o uso de arrays
unidimensionais para o armazenamento de temperaturas e matrizes
bidimensionais para representar dados de sensores.

Além de verificar se os algoritmos produziam os resultados esperados, foram
observadas e contabilizadas diferentes operações, como comparações, trocas e
percursos pelos elementos. Dessa forma, foi possível relacionar os resultados
obtidos na prática com os conceitos de complexidade de algoritmos estudados
teoricamente.


O aumento do tamanho da estrutura de dados influencia a quantidade de operações?
-----------------------------------------------------------------------------------

Sim. Os experimentos demonstraram que o aumento da quantidade de elementos
provoca um aumento no número de operações realizadas.

Na busca sequencial em matrizes, por exemplo, uma matriz de 2×2 possui apenas
4 elementos, enquanto uma matriz de 10×10 possui 100 e uma matriz de 100×100
possui 10.000 elementos. No pior caso, quando o valor procurado está na
última posição ou não está presente, é necessário verificar todos os
elementos da matriz. Por isso, a quantidade de comparações cresce de acordo
com o número total de posições, representado por ``m × n``.

Nos algoritmos de ordenação, também foi possível observar um aumento
significativo das operações conforme o tamanho do array aumentou. No
experimento realizado, o Bubble Sort apresentou um crescimento muito maior
na quantidade de comparações do que o Quick Sort para conjuntos de dados
maiores.

Esses resultados mostram que o tamanho da entrada influencia diretamente o
custo de execução. Entretanto, o impacto desse aumento também depende da
complexidade do algoritmo utilizado.


Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?
-----------------------------------------------------------------------------------------

Não. Os dois algoritmos apresentam formas diferentes de crescimento.

O Bubble Sort possui complexidade ``O(n²)`` nos casos médio e pior, enquanto o
Quick Sort apresenta complexidade média ``O(n log n)``. Por esse motivo, a
diferença entre os algoritmos tende a ficar mais evidente conforme a
quantidade de elementos aumenta.

Nos testes realizados, essa diferença foi observada principalmente no array
com 1.000 elementos. O Bubble Sort realizou uma quantidade muito maior de
comparações, enquanto o Quick Sort apresentou um número menor de operações.

Isso demonstra, na prática, que algoritmos com diferentes complexidades
podem apresentar comportamentos bastante distintos quando aplicados a
conjuntos de dados maiores. Em entradas pequenas, essa diferença pode ser
menos perceptível, mas tende a aumentar conforme o tamanho da entrada cresce.


Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?
---------------------------------------------------------------------------------------------------

Analisar somente o resultado final não é suficiente porque diferentes
algoritmos podem produzir exatamente o mesmo resultado, mas utilizar
quantidades diferentes de operações para chegar até ele.

No caso do Bubble Sort e do Quick Sort, ambos conseguem ordenar corretamente
o mesmo conjunto de dados. Portanto, observar apenas o array final não
permite identificar qual algoritmo realizou mais comparações ou trocas.

Por isso, durante a atividade também foram analisadas as operações internas
dos algoritmos. Essa análise permite compreender melhor o custo de cada
método e observar como seu comportamento muda conforme o tamanho da entrada.

Dessa forma, a corretude do resultado é importante, mas não é o único fator
que deve ser considerado. A quantidade de operações e a forma como elas
crescem com o tamanho dos dados também são importantes para analisar a
eficiência de um algoritmo.


Conclusão geral
---------------

Os experimentos realizados permitiram observar, na prática, a relação entre
o tamanho dos dados, a quantidade de operações e a complexidade dos
algoritmos.

A busca sequencial em matrizes apresentou crescimento proporcional à
quantidade de elementos no pior caso, enquanto o Bubble Sort apresentou um
crescimento mais acentuado devido à sua complexidade ``O(n²)``. Já o Quick
Sort apresentou, nos testes realizados, um crescimento menor, compatível com
sua complexidade média ``O(n log n)``.

A análise dos arrays e das matrizes também mostrou a importância dos índices,
dos loops e dos diferentes tipos de percurso para acessar e processar os
dados. Assim, foi possível perceber que a escolha de um algoritmo não deve
considerar apenas se ele produz o resultado correto, mas também como seu
custo de execução se comporta conforme a quantidade de dados aumenta.

Portanto, a atividade contribuiu para compreender de forma prática conceitos
de estruturas de dados, ordenação, busca, contagem de operações e
complexidade computacional. Esses conceitos são importantes para desenvolver
programas mais organizados e compreender as consequências do crescimento do
volume de dados durante a execução de um algoritmo.
