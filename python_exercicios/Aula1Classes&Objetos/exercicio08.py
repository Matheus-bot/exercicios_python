"""Tarefa: Crie uma classe Funcionario com o atributo de classe bonus. Adicione um método de classe modificar_bonus(valor) que altera o valor do bônus.
Objetivo: Compreender como os métodos de classe operam sobre atributos de classe."""

class Funcionario:
    def __init__(self, bonus, valor):
        self.bonus = bonus
        self.valor = valor

    def modificar_bonus(self):
        self.valor += self.bonus
        print(f"O valor com bônus é: {self.valor}")

funcionario1 = Funcionario(15, 500)
funcionario1.modificar_bonus()
