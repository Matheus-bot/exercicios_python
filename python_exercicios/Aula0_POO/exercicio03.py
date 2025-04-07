"""📌 Exercício 3. Cálculo de pontuação de jogo

Crie um programa que calcule a pontuação total de um jogador em um jogo.

A pontuação será dada por:
10 pontos por cada vitória.
5 pontos por cada empate.
0 pontos por cada derrota.
O programa deve calcular o total de pontos de acordo com o número de vitórias, empates e derrotas informados. """

vitorias = int(input('Total de vitórias: '))
empates = int(input('Total de empates: '))
derrotas = int(input('Total de derrotas: '))

tot =  (vitorias * 10) + (empates * 5)

print(f'Pontuação final: {tot}')