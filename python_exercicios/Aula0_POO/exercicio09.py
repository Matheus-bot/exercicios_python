"""📌 Exercício 9 - Somando Números Pares

Some todos os números pares de 1 a 100 e exiba o resultado. """

soma_pares = sum(i for i in range(1, 101) if i % 2 == 0)

print(f"A soma de todos os números pares de 1 a 100 é: {soma_pares}")