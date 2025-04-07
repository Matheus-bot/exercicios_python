"""Exercício 4: Crie uma classe Animal com um atributo de classe categoria. Modifique esse atributo na classe e observe como ele afeta todas as instâncias. ."""
 
class Animal:
    def __init__ (self, categoria):
        self.categoria = categoria
 
    def exibir_info(self):
        print(f"A categoria é: {self.categoria}")
 
Animal1 = Animal("Caninos")
 
Animal1.exibir_info()
 
Animal1.categoria = "Felinos"
Animal1.exibir_info()