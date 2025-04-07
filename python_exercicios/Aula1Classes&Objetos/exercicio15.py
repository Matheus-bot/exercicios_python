"""Exercício 15: Método de Instância com Atributos Privados

Tarefa: Crie uma classe ContaBancaria com o atributo privado __saldo e um método depositar(valor) que aumenta o saldo."""

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo


    def depositar(self, valor_deposito):
        self.__saldo += valor_deposito
        print(f'O valor atual com o deposito é: {self.__saldo}')

conta = ContaBancaria(100)
conta.depositar(3000)