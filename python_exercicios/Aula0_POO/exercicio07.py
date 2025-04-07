"""📌 Exercício 7 - Tabuada

Peça para o usuário digitar um número e exiba a tabuada dele de 1 a 10. """

n = int(input('Digite um número para saber a tabuada: '))

i = 0
for i in range(1, 11, +1):
  print(f'{n} X {i} = {i * n}')
  i + 1
