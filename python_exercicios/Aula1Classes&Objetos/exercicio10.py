"""Exercício 10- Crie uma classe Pessoa com o método de classe criar_pessoa(nome, idade) que cria e retorna uma instância de Pessoa. """
 
class Pessoa:
    def criar_pessoa(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f'Nome: {self.nome}, idade: {self.idade}')
 
pessoa1 = Pessoa()
pessoa1.criar_pessoa('Math', 21)