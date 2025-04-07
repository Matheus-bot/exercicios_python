"""Exercício 11-  Crie uma classe Calculadora com um método estático somar(a, b) que retorna a soma de dois números."""

class Calculadora:
    def somar(self, a, b):
        self.a = a
        self.b = b
        soma = a + b
        print(f"O resultado da soma é: {soma}")
 
calculo1 = Calculadora()
calculo1.somar(10,20)