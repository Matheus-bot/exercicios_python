"""📌 Exercício 17 - Verificar Número Par ou Ímpar

Crie uma função eh_par(numero) que recebe um número e retorna True se for par e False se for ímpar."""

def eh_par(n1):
  if n1 % 2 == 0:
    print('O número é par')
  else:
    print('O número é impar')

n1 = int(input('Digite um número'))
eh_par(n1)