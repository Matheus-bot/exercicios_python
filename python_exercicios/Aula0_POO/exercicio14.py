"""📌 Exercício 14 - Validando Entrada do Usuário

Peça para o usuário digitar um número positivo. 
Se ele digitar um valor negativo, peça novamente até ele digitar corretamente."""

n = int(input('Digite um número positivo '))

while True:
    n = int(input('Digite um número positivo '))
    if n >= 1:
      break
