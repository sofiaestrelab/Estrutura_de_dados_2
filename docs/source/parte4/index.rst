Investigação do Array
=====================

Programa:
~~~~~~~~

.. code-block:: python
   :linenos:

   import random

   TAMANHO = 10

   def main():
       temperatura = [0.0] * TAMANHO
       operacoes = 0  # contador de operações de percurso (acessos ao array)

       # 1. Receber as 10 temperaturas
       print("Digite 10 temperaturas:")
       for i in range(TAMANHO):
           temperatura[i] = float(input(f"Temperatura[{i}]: "))

       # 2. Mostrar todos os elementos armazenados
       print("\nIndice:      ", end="")
       for i in range(TAMANHO):
           print(f"{i:5d} ", end="")

       print("\nTemperatura: ", end="")
       for i in range(TAMANHO):
           print(f"{temperatura[i]:5.1f} ", end="")
           operacoes += 1  # acesso ao array para exibição
       print("\n")

       # 3. Calcular a média
       soma = 0.0
       for i in range(TAMANHO):
           soma += temperatura[i]
           operacoes += 1  # acesso ao array para somar
       media = soma / TAMANHO

       # 4 e 6. Identificar o maior valor e seu índice
       maior = temperatura[0]
       indice_maior = 0
       for i in range(1, TAMANHO):
           operacoes += 1  # comparação
           if temperatura[i] > maior:
               maior = temperatura[i]
               indice_maior = i

       # 5 e 7. Identificar o menor valor e seu índice
       menor = temperatura[0]
       indice_menor = 0
       for i in range(1, TAMANHO):
           operacoes += 1  # comparação
           if temperatura[i] < menor:
               menor = temperatura[i]
               indice_menor = i

       # 8. Contar quantos valores estão acima da média
       acima_da_media = 0
       for i in range(TAMANHO):
           operacoes += 1  # comparação
           if temperatura[i] > media:
               acima_da_media += 1

       # Resultados
       print(f"Media: {media:.2f}")
       print(f"Maior valor: {maior:.1f} (indice {indice_maior})")
       print(f"Menor valor: {menor:.1f} (indice {indice_menor})")
       print(f"Quantidade de valores acima da media: {acima_da_media}")
       print(f"\nNumero aproximado de operacoes de percurso realizadas: {operacoes}")

   if __name__ == "__main__":
       main()

Exemplo de execução
-------------------

Considerando as temperaturas:

.. list-table::
   :header-rows: 1
   :widths: 20 30

   * - Índice
     - Temperatura
   * - 0
     - 19,5 °C
   * - 1
     - 21,0 °C
   * - 2
     - 18,2 °C
   * - 3
     - 25,3 °C
   * - 4
     - 20,0 °C
   * - 5
     - 22,1 °C
   * - 6
     - 17,8 °C
   * - 7
     - 24,4 °C
   * - 8
     - 23,6 °C
   * - 9
     - 20,9 °C

Resultados
----------

* **Média:** 21,28 °C
* **Maior temperatura:** 25,3 °C
* **Índice do maior:** 3
* **Menor temperatura:** 17,8 °C
* **Índice do menor:** 6
* **Valores acima da média:** 4

Quantidade de operações
-----------------------

O programa realiza aproximadamente **58 operações contabilizadas**, considerando os acessos aos elementos do array e as comparações realizadas durante o processamento.

Esse número representa o critério de contagem adotado no experimento. Outras formas de contabilizar operações podem produzir valores diferentes.

A contagem pode ser dividida da seguinte forma:

* 10 acessos para receber as temperaturas;
* 10 acessos para exibir os valores;
* 10 acessos para calcular a média;
* 9 comparações para encontrar o maior valor;
* 9 comparações para encontrar o menor valor;
* 10 comparações para verificar os valores acima da média.

Total:

.. math::

   10 + 10 + 10 + 9 + 9 + 10 = 58

Complexidade
------------

O algoritmo possui complexidade **O(n)**.

Isso ocorre porque os principais procedimentos percorrem o array de forma linear. Mesmo existindo vários ``for``, eles são executados separadamente e cada um percorre uma quantidade proporcional a ``n``.

Como o array possui apenas 10 posições, o número de operações é pequeno. Porém, se o tamanho do array aumentasse, a quantidade de operações também aumentaria proporcionalmente.

A relação pode ser representada da seguinte forma:

.. code-block:: text

   Aumento do tamanho do array
               ↓
      Aumento das operações
               ↓
          Complexidade O(n)

