Análise e Conclusão
===================

Ao longo desta atividade, foram desenvolvidos e testados experimentalmente
diferentes algoritmos e estruturas de dados — ordenação (Bubble Sort e Quick
Sort), busca sequencial em matriz, manipulação de arrays unidimensionais
(temperaturas) e matrizes bidimensionais (sensores). Em todos os casos, a
proposta não foi apenas implementar os algoritmos, mas **medir, comparar e
interpretar** a quantidade de operações realizadas — comparações, trocas e
percursos — permitindo observar, na prática, conceitos que muitas vezes são
discutidos apenas de forma teórica.

O aumento do tamanho da estrutura de dados influencia a quantidade de operações?
--------------------------------------------------------------------------------

Sim, e de forma bastante evidente em todos os experimentos realizados. Na
busca sequencial em matriz, o número de comparações no pior caso cresceu
exatamente na mesma proporção do número de elementos: de 4 (matriz 2×2) para
100 (matriz 10×10) e para 10.000 (matriz 100×100) — um crescimento
diretamente ligado ao produto m × n. Nos algoritmos de ordenação, o efeito
foi ainda mais expressivo: ao aumentar o array de 10 para 1.000 elementos
(100 vezes maior), o Bubble Sort passou de 44 para 499.122 comparações — um
crescimento de mais de 11.000 vezes. Isso confirma que **o tamanho da
entrada é o principal fator que determina o custo computacional** de um
algoritmo, mas também mostra que **a forma como esse custo cresce depende
diretamente da complexidade do algoritmo**, e não apenas do tamanho dos
dados.

Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?
---------------------------------------------------------------------------------------

Não. Esse foi um dos pontos mais claros observados no experimento de
ordenação. Para entradas pequenas (10 e 20 elementos), a diferença entre os
dois algoritmos era perceptível, mas não drástica. À medida que o tamanho do
array aumentou para 1.000 elementos, porém, a diferença se tornou enorme: o
Bubble Sort realizou quase 50 vezes mais comparações que o Quick Sort
(499.122 contra 10.385). Isso acontece porque os dois algoritmos possuem
**complexidades assintóticas diferentes** — O(n²) para o Bubble Sort e
O(n log n) para o Quick Sort (em média) —, e essa diferença só se torna
visível de forma acentuada quando o volume de dados é suficientemente
grande. Ou seja, **algoritmos com complexidades diferentes crescem em
ritmos diferentes**, e quanto maior a entrada, mais essa diferença se
amplia — um comportamento que a notação Big O descreve exatamente para
isso: prever como o custo se comporta no limite, e não em casos pontuais e
pequenos.

Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?
--------------------------------------------------------------------------------------------------

Porque o resultado final — o array ordenado — é **idêntico** para qualquer
algoritmo correto, independentemente de sua eficiência. Bubble Sort e Quick
Sort, aplicados aos mesmos dados, produzem exatamente a mesma saída (foi
inclusive validado nos testes com ``assert``). Se a análise se limitasse a
conferir se o vetor está ordenado corretamente, os dois algoritmos
pareceriam equivalentes — quando, na realidade, um deles pode ser dezenas
ou centenas de vezes mais custoso que o outro para a mesma tarefa. É
justamente por isso que esta atividade priorizou a contagem de
**operações internas** (comparações, trocas, percursos) em vez de apenas
validar a saída: são essas métricas que revelam o verdadeiro custo do
processamento, especialmente quando o volume de dados cresce. Em
aplicações reais, essa diferença se traduz diretamente em tempo de
execução, consumo de recursos e escalabilidade — aspectos que passam
despercebidos se a avaliação for baseada apenas em "o resultado está
certo?".

Conclusão geral
----------------

Os experimentos realizados ao longo desta atividade — desde a ordenação de
arrays até a manipulação de matrizes bidimensionais — reforçam, de forma
prática, um princípio central da Ciência da Computação: **a eficiência de
um algoritmo não pode ser avaliada apenas pela corretude do resultado, mas
pela forma como o custo de execução se comporta à medida que o volume de
dados cresce**. A análise de complexidade computacional (Big O) não é um
exercício abstrato: ela descreve, com precisão, padrões de crescimento que
foram efetivamente observados nos dados coletados — seja no crescimento
quadrático do Bubble Sort e da busca sequencial em matrizes, seja no
crescimento log-linear do Quick Sort. Compreender essa relação é essencial
para escolher a estrutura de dados e o algoritmo mais adequados para cada
contexto, equilibrando simplicidade, uso de memória e desempenho conforme
as exigências reais de cada aplicação.
