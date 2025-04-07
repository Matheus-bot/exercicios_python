'''Exercício 3 - Crie uma classe Produto com os atributos nome e preco. Crie uma instância de Produto e modifique o atributo preco.'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
 
    def exibir_info (self):
        print(f"Nome: {self.nome}, Preço: {self.preco}")
 
Produto1 = Produto("Capacete", 200.00)
Produto1.exibir_info()
 
Produto1.preco = 700.00
Produto1.exibir_info()