''' Exercício 2- Crie uma classe Carro com os atributos modelo e ano. Use o construtor __init__ para inicializar esses atributos e crie uma instância de Carro.'''

class Carro:

    def __init__(self, modelo, ano):
        self.modelo = modelo 
        self.ano = ano 

    def exibir(self):
        print(f'{self.modelo}\n{self.ano}')

carro1 = Carro('Fusca', 2001)
carro2 = Carro('sedan', 2023)

carro2.exibir()
