from random import randint
from time import sleep
placar = {}
for jogada in range(1, 5):
    placar[f'jogador{jogada}'] = randint(1, 6)
    sleep(1)
    print(f"Jogador {jogada} tirou {placar[f'jogador{jogada}']}")
print('-=' * 20)
print('== RANKING DOS JOGADORES ==')
#irei terminar depois pois a função que resolve ainda não foi estudada, mas a ideia é ordenar o dicionário e printar o ranking dos jogadores em ordem decrescente de pontuação.