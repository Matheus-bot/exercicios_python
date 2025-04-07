"""📌 Exercício 8 - Contagem Regressiva

Faça um programa que conte de 10 até 1 e exiba "Feliz Ano Novo!" no final. """
from time import sleep
i = 0
for i in range(10, 0, -1):
  print(i)
  sleep(1)
  i + 1
sleep(1)
print('Feliz ano novo!!!')