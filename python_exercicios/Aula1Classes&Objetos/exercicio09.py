""" Exercício 9- Crie uma classe Loja com o atributo de classe desconto. Adicione um método de classe aplicar_desconto() que modifica o valor do desconto para todas as instâncias.  """
class Loja:
    desconto = 0
 
    def aplicar_desconto(self):
        self.desconto = float(input('Digite o valor do desconto: '))
        print(f"O novo valor do desconto é de R${self.desconto} ")
 
    def exibir(self):
        print(f'O valor do desconto é: {self.desconto}')
 
loja1 = Loja()
loja1.exibir()
loja1.aplicar_desconto()
loja1.exibir()