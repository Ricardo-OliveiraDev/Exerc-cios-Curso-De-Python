from random import choice
usuario = input("Vamos jogar pedra, papel ou tesoura! Qual você joga?:").capitalize()
jogadas = ["Pedra", "Papel", "Tesoura"]
if usuario not in jogadas:
    print("Você não sabe brincar? digite uma resposta válida seu besta!")
else:
    computador = choice(jogadas)
    print(f"Eu joguei {computador} e você jogou {usuario}! o vencedor foi: ", end="")
    if usuario == "Pedra" and computador == "Tesoura":
        print("\033[4;32mVocê ganhou\033[m!")
    elif usuario == "Papel" and computador == "Pedra":
        print("\033[4;32mVocê ganhou\033[m!")
    elif usuario == "Tesoura" and computador == "Papel":
        print("\033[4;32mVocê ganhou\033[m!")
    elif usuario == computador:
        print("\033[4;33mDeu empate\033[m!")
    else:
        print("\033[4;31mEu ganhei\033[m!")
