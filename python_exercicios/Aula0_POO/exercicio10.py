"""📌 Exercício 10 - Contando Vogais

Peça ao usuário para digitar uma palavra e conte quantas vogais existem nela. """

palavra = input("Digite uma palavra: ").upper()
vogais = "AEIOU"

quantidade_vogais = sum(1 for letra in palavra if letra in vogais)

print(f"A palavra '{palavra}' contém {quantidade_vogais} vogais.")

