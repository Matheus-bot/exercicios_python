"""📌 Exercício 18- Média de Notas

Crie uma função calcular_media(notas) que recebe uma lista de notas e retorna a média. """

def calcular_media(n1, n2, n3, ):

    media = (n1 + n2  + n3) / 3
    return media

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = calcular_media(n1, n2, n3)

print(f'A media das notas é: {media:.2f}')

