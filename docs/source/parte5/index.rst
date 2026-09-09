Matriz Aplicada - Monitoramento de Sensores
============================================

.. code-block:: python
   :linenos:

   import random

   SENSORES = 5
   HORAS = 24

   # Gera os dados automaticamente (substitui a entrada manual de 120 valores)
   random.seed(1)
   sensores = [[round(random.uniform(15, 32), 1) for _ in range(HORAS)] for _ in range(SENSORES)]

   operacoes = 0

   # 1. Média de cada sensor
   for i in range(SENSORES):
       media = sum(sensores[i]) / HORAS
       operacoes += HORAS
       print(f"Sensor {i}: media = {media:.2f}")

   # 2, 3 e 4. Maior temperatura, sensor e horário
   maior = sensores[0][0]
   sensor_maior, hora_maior = 0, 0
   for i in range(SENSORES):
       for j in range(HORAS):
           operacoes += 1
           if sensores[i][j] > maior:
               maior = sensores[i][j]
               sensor_maior, hora_maior = i, j

   print(f"\nMaior temperatura: {maior:.2f} (sensor {sensor_maior}, hora {hora_maior}h)")

   # 5. Média geral
   total = sum(sum(linha) for linha in sensores)
   media_geral = total / (SENSORES * HORAS)
   operacoes += SENSORES * HORAS
   print(f"Media geral: {media_geral:.2f}")

   # 6. Leituras acima do limite
   limite = float(input("\nLimite de temperatura: "))
   acima = sum(1 for linha in sensores for valor in linha if valor > limite)
   operacoes += SENSORES * HORAS
   print(f"Leituras acima do limite: {acima}")

   print(f"\nOperacoes de percurso: {operacoes}")

Sensor 0: media = 23.29
Sensor 1: media = 22.51
Sensor 2: media = 23.74
Sensor 3: media = 25.12
Sensor 4: media = 23.67

Maior temperatura: 31.90 (sensor 1, hora 16h)
Média geral: 23.67

Leituras acima do limite: 30

Operações de percurso: 480
