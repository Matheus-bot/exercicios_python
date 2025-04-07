"""📌 Exercício 20 - Números Pares

Crie um programa que armazena números de 1 a 10 em uma lista e exibe apenas os pares. """

numeros = []


for n in range(1, 11):
    numeros.append(n)
    if n % 2 == 0 :
        print(f'{n} ', end ='')

print(numeros)
