"""📌 Exercício 5. Cálculo de salário líquido

Crie um programa que calcule o salário líquido de um funcionário. O salário bruto é dado pelo usuário, e o programa deve descontar:

INSS (10%)

Imposto de Renda (IR) de acordo com a faixa salarial:

Até R$ 2.000,00: isento

De R$ 2.001,00 até R$ 5.000,00: 10%

Acima de R$ 5.000,00: 20% """

bruto = float(input('Qual seu salário Bruto? '))

inss =  (10/100) * bruto

print(f'o desconto do inss: -{inss:.2f}')

if bruto <= 2000:
  print(f'Salário líquido: R${bruto - inss}')
elif bruto > 2000 and bruto <= 5000:
  ir = (10 / 100) * bruto
  print(f'IR: -{ir:.2f}')
  print(f'Salário líquido: {bruto - inss - ir:.2f}')
elif bruto > 5000:
  ir = (10 / 100) * bruto
  print(f'IR: -{ir:.2f}')
  print(f'Salário líquido: R${bruto - inss - ir:.2f}')