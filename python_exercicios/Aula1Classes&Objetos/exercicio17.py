"""Exercício 17: Atributos de Instância em Várias Instâncias
Tarefa: Crie uma classe Aluno com os atributos nome e nota. Crie várias instâncias e modifique os atributos de cada uma de forma independente.
Objetivo: Compreender a independência dos atributos de instância entre diferentes objetos."""

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome 
        self.nota = nota

aluno1 = Aluno('Matheus', 9)
aluno2 = Aluno('Marcelo', 8)
aluno3 = Aluno('Carlos', 4)

print(f'Aluno: {aluno1.nome} nota : {aluno1.nota}')
print(f'Aluno: {aluno2.nome} nota : {aluno2.nota}')
print(f'Aluno: {aluno3.nome} nota : {aluno3.nota}')

aluno1.nota = 10
aluno2.nota = 2
aluno3.nome = 'joaquina'

print(f'Aluno: {aluno1.nome} nota : {aluno1.nota}')
print(f'Aluno: {aluno2.nome} nota : {aluno2.nota}')
print(f'Aluno: {aluno3.nome} nota : {aluno3.nota}')
