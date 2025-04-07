"""Exercício 14: Atributo de Classe e Método Estático

Tarefa: Crie uma classe Banco com um atributo de classe taxa_juros. Adicione um método estático calcular_juros(saldo) que calcula os juros sobre um saldo, considerando a taxa de juros da classe.

"""
class Banco:
    def __init__(self, taxa, saldo):
        self.taxa = taxa
        self.saldo = saldo
    
    def calcular_juros(self):
        novosaldo = self.saldo + (self.saldo * self.taxa / 100) 
        print(f'Com juros ficou: {novosaldo}')


saldocomjuros = Banco(100, 300)

saldocomjuros.calcular_juros()