# Exercício Python 083: gerador de palpites da Mega Sena. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
from random import randint
from time import sleep
palpite = []
quantidade = int(input("Quantos palpites você quer: "))
print(f"=-=- Sorteando {quantidade} jogos... -=-=")
for n_jogos in range(quantidade):
    for _ in range(6):
        numero = randint(1, 60)
        while numero in palpite:
            numero = randint(1, 60)
        palpite.append(numero)
    palpite.sort()
    print(f"Jogo {n_jogos + 1}: {palpite}")
    palpite.clear()
    sleep(1)
print(f"{'-=' * 5} BOA SORTE! {'-=' * 5}")