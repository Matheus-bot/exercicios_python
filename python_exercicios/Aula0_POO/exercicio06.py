"""📌 Exercício 6. Simulação de descontos em uma compra

Crie um programa que simule um desconto progressivo em uma compra. O cliente recebe:

10% de desconto se o valor da compra for até R$ 500.

15% de desconto se o valor da compra for entre R$ 501 e R$ 1000.

20% de desconto se o valor da compra for acima de R$ 1000.

O programa deve pedir o valor total da compra e aplicar o desconto correspondente."""

preço = float(input('Valor do produto: R$'))

if preço <= 500:
  desconto = preço * (10/100)
  print(f'Recebeu 10% de desconto você irá pagar R${preço - desconto:.2f}')
elif preço > 500 and preço <= 1000:
  desconto = preço * (15/100)
  print(f'Recebeu  15% de desconto você irá pagar R${preço - desconto:.2f}')
elif preço > 1000:
  desconto = preço *(20/100)
  print((f'Você recebeu 20 % de desconto você irá pagar R{preço - desconto:.2f}'))
else:
  print('Ocorreu um erro!!!')