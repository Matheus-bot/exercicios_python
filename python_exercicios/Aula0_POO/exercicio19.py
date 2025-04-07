"""📌 Exercício 19 - Média de Notas

Crie um programa que solicita 3 notas do usuário, armazena em uma lista e calcula a média. """

notas = []
for i in range(1, 4):
    notas.append(float(input('Digite a nota:')))
    print(notas)

media = sum(notas) / len(notas)

print(f'A média das notas na lista {notas} é {media:.2f} ')