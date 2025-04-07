"""📌Exercício 1. Parcelamento de um produto

Uma loja oferece parcelamento de um produto, mas cobra 10% de juros ao parcelar. Peça ao usuário o preço do produto e o número de parcelas e calcule o valor total e o valor de cada parcela."""

preço = float(input('Qual o preço do produto? '))
parcelas = int(input('Em quantas vezes vai pagar? '))

if parcelas > 1:
  juros =  preço * (10/100)
  novopreço = preço + juros
  qntvezes = novopreço / parcelas
  print(f'Você pagara {parcelas}X de R${qntvezes:.2f} = R${novopreço:.2f}')
else:
  print(f"Você pagará a vista R${preço:.2f}")