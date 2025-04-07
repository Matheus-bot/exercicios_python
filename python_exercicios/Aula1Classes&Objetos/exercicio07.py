"""Tarefa: Crie uma classe Aluno com os atributos nome e nota. Adicione um método de instância situacao() que retorna "Aprovado" se a nota for maior ou igual a 6 e "Reprovado" caso contrário.
Objetivo: Trabalhar com métodos de instância que utilizam condicionais."""

class Aluno:
    nota= 0
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def situacao(self):
        if self.nota >= 6:
            print(f"Nome: {self.nome} Nota: {self.nota} - Aprovado")
        else:
            print(f"Nome: {self.nome} Nota: {self.nota} - Reprovado")
            
Aluno1 = Aluno("Matheus", 10)
Aluno1.situacao()