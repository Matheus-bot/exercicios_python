"""Exercício 5: Crie uma classe Pessoa com os atributos nome e idade. Adicione um método de instância apresentar() que retorna uma string com o nome e a idade da pessoa.
Objetivo: Compreender como os métodos de instância operam sobre os atributos do objeto."""
 
class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
 
    def apresentar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
 
Pessoa1 = Pessoa("Marcia", 28)
Pessoa1.apresentar_info()