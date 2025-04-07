"""📌 Exercício 21 - Lista de Compras

Crie um programa onde o usuário pode adicionar itens a uma lista de compras e exibir os itens ao final.  """


compras = []

while True:
    produtos = str(input('Nome do produto'))
    compras.append(produtos)

    resp = str(input('Quer continuar? [S|N]'))
    if resp in 'Nn':
      break
print('Lista de Compras:')
tamanho = len(compras)

for i , produto  in enumerate(compras):
    print(f'{i+1} - {produto}')