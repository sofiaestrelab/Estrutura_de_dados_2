Investigação do Array
=====================

Programa
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


Indice:          0     1     2     3     4     5     6     7     8     9 
Temperatura:  19.5  21.0  18.2  25.3  20.0  22.1  17.8  24.4  23.6  20.9 

Média: 21.28
Maior valor: 25.3 (indice 3)
Menor valor: 17.8 (indice 6)
Quantidade de valores acima da média: 4

Número aproximado de operações de percurso realizadas: 48
