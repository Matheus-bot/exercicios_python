"""📌 Exercício 15 - Criando um Menu Interativo

Crie um menu que permita ao usuário escolher opções até ele decidir sair.   """

opção = 0

while opção != 4:
    opção = int(input('''
    [1]Entrar
    [2]Alterar
    [3]Deletar
    [4]Sair
     '''))
print('Saindo do programa!!!')