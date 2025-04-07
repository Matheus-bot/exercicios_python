"""Exercício 6: Método de Instância Modificando Atributos
Tarefa: Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método de instância depositar(valor) que aumenta o saldo da conta.
."""

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        novo_saldo = self.saldo + valor
        print(f'O novo saldo é {novo_saldo}')

conta = ContaBancaria("Matheus", 10400)

conta.depositar(23000)
