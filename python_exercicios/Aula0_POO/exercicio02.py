"""📌 Exercício 2. Controle de estoque

Crie um sistema para controlar o estoque de produtos. O programa deve pedir a quantidade inicial de um produto, a quantidade vendida e a quantidade recebida. Calcule a quantidade final em estoque."""

quantidadeinicial = int(input('Qual a quantidade inicial de produtos? '))
quantidadevenda = int(input('Qual a quantidade de venda? '))
quantidaderecebida = int(input('Qual a quantidade recebida? '))

total = quantidadeinicial - quantidadevenda + quantidaderecebida

print(f'A quantidade total do estoque é: {total}')