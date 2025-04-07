"""📌 Exercício 11 - Números Primos

Desafio: Peça ao usuário para digitar um número e informe se ele é primo.  """

numero = int(input("Digite um número: "))
if numero > 1:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break
    else:
        print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")