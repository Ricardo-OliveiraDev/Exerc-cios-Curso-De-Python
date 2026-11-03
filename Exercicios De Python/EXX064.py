from random import randint
vitorias = 0
while True:
    jogada = int(input("Vamos jogar par ou impar! Digite um número: "))
    parouimpar = input("Você quer par ou impar?[I/P]:").strip().lower()[0]
    computador = randint(0,10)
    soma = jogada + computador
    if soma % 2 == 0:
        print(f"Eu joguei {computador} e você jogou {jogada} então deu {soma} que é par!")
        if parouimpar == "p":
            print("Parabéns você ganhou!")
            vitorias += 1
        elif parouimpar == "i":
            print("Você perdeu!")
            break
    else:
        print(f"Eu joguei {computador} e você jogou {jogada} então deu {soma} que é impar!")
        if parouimpar == "i":
            print("Parabéns você ganhou!")
            vitorias += 1
        elif parouimpar == "p":
            print("Você perdeu!")
            break
print("--------------------------------------------------------")
print(f"Você teve o total de {vitorias} vitorias consecutivas!")