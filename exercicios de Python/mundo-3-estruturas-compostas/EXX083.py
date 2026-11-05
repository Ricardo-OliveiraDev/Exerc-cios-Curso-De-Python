from random import randint
from time import sleep
palpite = []
quantidade = int(input("Quantos palpites você quer: "))
print(f"=-=- Sorteando {quantidade} jogos... -=-=")
for quantidade_de_jogos in range(0, quantidade):
    for jogo in range(0, 6):
        numero = randint(1, 60)
        if numero in palpite:
            while numero in palpite:
                numero = randint(1, 60)
        palpite.append(numero)
    print(f"Jogo {quantidade_de_jogos + 1}: {palpite}")
    palpite.clear()
    sleep(1)
print(f"{'-=' * 5} BOA SORTE! {'-=' * 5}")