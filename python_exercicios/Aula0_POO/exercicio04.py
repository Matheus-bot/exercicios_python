"""📌 Exercício 4. Cálculo de comissão de vendedor

Crie um programa que calcule a comissão de um vendedor, com base nas vendas realizadas. O vendedor ganha 5% de comissão sobre as vendas, mas existe um bônus de R$ 200,00 se ele vender mais de R$ 10.000,00 no mês.

Fórmula:

Comissão = 5% do valor das vendas

Se as vendas forem acima de R$ 10.000,00 adicionar o bônus de R$ 200. """

vendas = float(input('Total das vendas:'))

comissão  = (5 / 100) * vendas
bonus = 200

if vendas >= 10000:
   comissão += bonus

print(f"Você teve o total de {comissão} de comissão")