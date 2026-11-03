from random import randint
numero = randint(0, 5)
resposta = int(input("Tente adivinhar o número que estou pensando de 0 a 5!\nQue número você acha que estou pensando ?: "))
if resposta == numero:
    print("PARÁBENS VOCÊ ACERTOU!")
else:
    print(f"VOCÊ ERROU! O NÚMERO ERA {numero} TENTE NOVAMENTE!")
