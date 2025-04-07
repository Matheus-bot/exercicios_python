"""📌 Exercício 16 - Calculadora

Crie uma função calculadora(a, b, operacao) que recebe dois números e uma operação (+, -, *, /) e retorna o resultado.  """

def calculadora(n1, n2, op ):
  if op == '+':
    return  n1 + n2
  elif op == '-':
    return n1 - n2
  elif op == '*':
    return  n1 * n2
  elif op == '/':
    return n1 / n2
  else:
    print('Não foi possivel calcular')


n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))

op = str(input('''Escolha:
    [+]Soma
    [-]Subtração
    [*]Multiplicação
    [/]Divisão

'''))
calculadora(n1, n2, op)
