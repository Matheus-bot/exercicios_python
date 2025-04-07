"""Exercício 12- Crie uma classe Pessoa com um método estático validar_idade(idade) que retorna True se a idade for maior ou igual a 18 e False caso contrário. """
class Pessoa:

    def validar_idade(self, idade):
        self.idade = idade
        if idade >= 18:
            print('Maior')
        else:
            print('Menor')

pessoa1 = Pessoa()
pessoa1.validar_idade(20)

pessoa2 = Pessoa()
pessoa2.validar_idade(20)