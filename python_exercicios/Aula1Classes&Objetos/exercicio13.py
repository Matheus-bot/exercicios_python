"""Exercício 13: Atributos de Instância e Métodos

Tarefa: Crie uma classe Produto com os atributos nome e preco. Adicione um método aplicar_desconto(desconto) que aplica um desconto ao preço do produto.

"""
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        if 0 <= desconto <= 100:
            self.preco -= self.preco * (desconto / 100)
        else:
            print("Desconto inválido. O valor deve estar entre 0 e 100.")

produto = Produto("Camiseta", 100)
print(f"Preço original: R${produto.preco:.2f}")
produto.aplicar_desconto(20)  
print(f"Preço com desconto: R${produto.preco:.2f}")