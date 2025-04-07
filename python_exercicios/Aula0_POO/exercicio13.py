"""📌 Exercício 13 - Contador de tentativas

Modifique o programa anterior para contar quantas tentativas o usuário precisou até acertar.  """

from random import randint
numero = randint(1,10)
n = int(input('Advinhe o número [1-10]'))

cont = 0
while n != numero:
  n = int(input('Adivinhe o número [1-10]'))
  cont += 1
print('Acertou')
print(f'Você precisou de {cont+1} Vezes para acertar')