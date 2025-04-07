"""📌 Exercício 12 - Adivinhação

O programa escolhe um número aleatório entre 1 e 10, e o usuário tem que adivinhar. Ele só para quando o número correto for digitado. """

from random import randint
numero = randint(1,10)
n = int(input('Advinhe o número [1-10]'))

while n != numero:
  n = int(input('Adivinhe o número [1-10]'))
print('Acertou')